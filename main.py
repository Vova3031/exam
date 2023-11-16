import requests
from bs4 import BeautifulSoup

url = "https://cash-backer.club/shops"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

shops = soup.find_all("div", class_="shop")

with open("cashback_data.txt", "w", encoding="utf-8") as file:
    for shop in shops:
        company_name = shop.find("h2", class_="shop-title").find("a").text.strip()
        cashback_amount = shop.find("span", class_="cashback-amount").text.strip()

        print(f"Назва кампанії: {company_name}")
        print(f"Розмір кешбеку: {cashback_amount}")
        print()

        file.write(f"Назва кампанії: {company_name}\n")
        file.write(f"Розмір кешбеку: {cashback_amount}\n")
        file.write("\n")

print("Дані були успішно зібрані та записані у файл cashback_data.txt.")
