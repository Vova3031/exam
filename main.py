import requests
import lxml
from bs4 import BeautifulSoup
import openpyxl

user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
headers = {"User-agent" : user}
sess = requests.Session()
cter = 0
book = openpyxl.Workbook()
sht = book.active
file = open('resault.txt', "a", encoding = "utf-8")
f = open('resault.xlsx', 'r+')
f.truncate(0)
f.close()
for j in range (1,50):
  link = f"https://kups.club/?page={j}/"
  resp = sess.get(link, headers = headers)
  soup = BeautifulSoup(resp.text, "html.parser")
  prods = soup.findAll("div", class_ = 'col-lg-4 col-md-4 col-sm-6 portfolio-item')
  for prod in prods:
    cter += 1
    title = prod.find("h3", class_ = "card-title").text
    price = prod.find("p", class_ = "card-text").text
    try:
      spons_t = prod.find("a", class_="text-black link-default")
      if spons_t:
          spons_txt = spons_t.text.strip()
          spons_img = spons_t.find('img', alt=True)
          spons = spons_img['alt'].strip() if spons_img and 'alt' in spons_img.attrs else spons_txt
      else:
          spons = None
    except Exception as e:
      print("error")
      sponsor = None
    sht[f"A{cter}"] = title
    sht[f"B{cter}"] = price
    sht[f"C{cter}"] = spons.strip() if spons else None
    file.write(f"Product No {cter}\n")
    file.write(f"Name: {title} {price} Sponsor: {spons}\n")
book.save('resault.xlsx')
book.close()