# insert data：insert data 的過程若無此資料庫或 table(collection)，會自動幫忙創建
from pymongo import MongoClient
import requests

client = MongoClient()

for page in range(1, 4):
    r = requests.get('https://24h.pchome.com.tw/search/v4.3/all/results?q=%E6%9B%B2%E9%9D%A2%E8%9E%A2%E5%B9%95&page={}&sort=rnk/dc'.format(page))
    if r.status_code == 200:
        print(page)
        d = r.json()
        prods = d['Prods']    
        if prods == [ ]:
            break
        for prod in prods:
            client.pchome.products.insert_one(prod)
    else:
        print(r.status_code)