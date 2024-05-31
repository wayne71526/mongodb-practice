## query
from pymongo import MongoClient
import pprint

# 與 mongodb 連線
client = MongoClient("localhost", 27017)

# getting database
db = client.pchome

# getting collection
col = db.products


# 列出所有資料
# data = col.find()
# for d in data:
#     pprint.pprint(d)


# 列出一筆資料
# data = col.find_one()
# pprint.pprint(d)


# 字串中包含
name_condition = {"Name": {'$regex' : ".*ASUS.*"}}
data = col.find(name_condition);
# for d in data:
#     pprint.pprint(d['Name'])
    
    
# 字串中包含且不區分大小寫
name_condition = {"Name": {'$regex' : ".*asus.*", '$options': 'i'}}
data = col.find(name_condition)
# for d in data:
#     print(d['Name'], d['Price'])    


# 產品大於10000
price_condition = {'Price': {'$gt': 10000}}
data = col.find(price_condition)
# for d in data:
#     print(d['Name'], d['Price'])
    

# and example
data = col.find({'$and': [name_condition, price_condition]})
# for d in data:
#     print(d['Name'], d['Price'])


# update one
col.update_one({'Name': '【SAMSUNG三星】C34G55TWWC 34型 Odyssey G5 曲面電競螢幕'}, {'$set': {'Price': 8000}})
data = col.find_one({'Name': '【SAMSUNG三星】C34G55TWWC 34型 Odyssey G5 曲面電競螢幕'})
# pprint.pprint(data)


# upsert：如果沒有符合 filter 的 document，則創造 1 document
col.update_one({'Name': 'Wayne'}, {'$set': {'Price': 6000}}, upsert = True)
data = col.find_one({'Name': 'Wayne'})
# pprint.pprint(data)


# delete_one
col.delete_one({'Name': 'Wayne'})