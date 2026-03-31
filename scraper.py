import requests
url = "https://books.toscrape.com/"
res = requests.get(url)
print(res.status_code)
# print(res.text)
from bs4 import BeautifulSoup
soup = BeautifulSoup(res.text, 'lxml')
data=[]
title = soup.title.text
print("page Title:", title)
books = soup.find_all("article",class_="product_pod")

for book in books:
    book_title=book.h3.a["title"]
    price=book.find('p',class_="price_color").text
    rating=book.find('p',class_="star-rating")["class"][1]
    data.append({
        "title": book_title,
        "price": price,
        "rating": rating
    })
for item in data:
    print(item)
    
import json

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

resp=requests.get("https://fakestoreapi.com/Products")
print(resp.status_code)
if resp.status_code == 200:
    api_data = resp.json()
else:
    api_data = []
    print("API request failed")
with open("api_data.json", "w") as file:
    json.dump(api_data, file, indent=4)