import os
import requests
from bs4 import BeautifulSoup
import wget

url = "https://www.geeksandijan.uz/" 

if not os.path.exists("geeks_images"):
    os.makedirs("geeks_images")

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

images = soup.find_all("img")

for img in images:
    img_url = img["src"]

    if not img_url.startswith("http"):
        img_url = url + img_url

    try:
        print(f"Yuklanmoqda: {img_url}")
        wget.download(img_url, out="geeks_images/")
        print("\nYuklab olindi!")
    except Exception as e:
        print(f"Xato: {e}")

print("Barcha rasmlar muvaffaqiyatli yuklab olindi!")