from bs4 import BeatifulSoup
import requests

r = requests.get("https://store.steampowered.com/app/1091500/Cyberpunk_2077/")
soup = BeatifulSoup(r.content, "lxml")

precio = soup.find('div', class_= "discount_original_price").text
print(precio.strip())

nombre = soup.find('div', class_= "apphub_AppName").text
print(nombre)