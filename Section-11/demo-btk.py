from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from csv import writer

# Tarayıcı ayarları
options = Options()
options.add_argument("--headless")  # Tarayıcıyı arka planda çalıştır
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://www.btkakademi.gov.tr/portal/catalog?categoryId=353"
driver.get(url)

# Sayfanın yüklenmesi için bekle
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

element = soup.find(id="gbt_catalog-main-right-course")
if element:
    kurslar = element.find_all(class_="ant-ribbon-wrapper css-tpassh")
    print(f"{len(kurslar)} kurs bulundu.")
else:
    print("Belirtilen ID ile bir öğe bulunamadı.")
    driver.quit()
    exit()

# CSV dosyasına yaz
with open("kurslar.csv", "w", encoding="utf-8", newline="") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["link", "image", "title", "seviye", "like", "ogrenci"])

    for kurs in kurslar:
        anchor = kurs.a
        link = anchor.get("href")
        image = anchor.img.get("src")
        title = anchor.find(class_="font-medium text-base").string.strip() if anchor.find(class_="font-medium text-base") else ""
        seviye = anchor.find(class_="txt-secondary font-medium").string.strip() if anchor.find(class_="txt-secondary font-medium") else ""

        sayilar = anchor.next_sibling.next_sibling.get_text(separator="-").split("-")
        like = sayilar[0].strip() if len(sayilar) > 0 else ""
        ogrenci = sayilar[1].strip() if len(sayilar) > 1 else ""

        csv_writer.writerow([link, image, title, seviye, like, ogrenci])

driver.quit()
