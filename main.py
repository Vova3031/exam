f = open('output.txt', 'r+')
f.truncate(0)
f.close()

import requests
import lxml
from bs4 import BeautifulSoup

user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
headers = {"User-agent" : user}
sess = requests.Session()
counter = 0
space = "  "

print("Starting...")
for j in range (0,7):
  url = f"https://cash-backer.club/shops?page={j}"
  resp = sess.get(url, headers = headers)

  if resp.status_code == 200:
    soup = BeautifulSoup(resp.text, "html.parser")
    prods = soup.findAll("div", class_ = 'col-lg-2 col-md-3 shop-list-card pseudo-link no-link')
    for prod in prods:
      counter += 1
      title = prod.find("div", class_ = "shop-title").text
      cashb = prod.find("div", class_ = "shop-rate").text
      #zapis
      with open('output.txt', "a", encoding = "utf-8") as file:
        file.write(f"Shop No {counter}\n")
        file.write(f"{space}Name: {title}\n")
        file.write(f"{space}Cashback: {cashb}\n")
    if j == 4:
      print("Finishing...")
  else:
    print("ERROR on start")
    break
print("Done")