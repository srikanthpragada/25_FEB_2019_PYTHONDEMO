import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.flipkart.com")
bs = BeautifulSoup(resp.text,"html.parser")

for img in bs.find_all("img"):
    if 'src' in img.attrs:
       print(img['src'])
