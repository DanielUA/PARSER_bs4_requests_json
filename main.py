import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json


# ua = UserAgent(os="Linux")
# x = ua.getChrome
# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#
# req = requests.get(url)
# src = req.text
# with open("index.html", mode="w") as file:
#     file.write(src)

with open("index.html", mode="r") as file:
    src = file.read()
all_categories_dict = {}
soup = BeautifulSoup(src, "lxml")
all_product_hrefs = soup.find_all(class_="mzr-tc-group-item-href")
for item in all_product_hrefs:
    item_text = item.text
    item_href = "https://health-diet.ru" + item["href"]
    all_categories_dict[item_text] = [item_href]

with open("all_categories.json", mode="w") as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)




