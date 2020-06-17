import json
import csv
import re

from pymongo import MongoClient


client = MongoClient()
db = client.db
collection = db.test_collection

def read_data(csv_file):
    # with open(csv_file, encoding='utf8') as csvfile:
    #     reader = csv.DictReader(csvfile, delimiter=',')

    with open(csv_file, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=',')
        next(rows)
        parsed_data = list(rows)
        #print(parsed_data)

    consert_list = [
        {'artist': item[0],
         'price': int(item[1]),
         'place': item[2], 'date': item[3]
         }
        for item in parsed_data
    ]
    #print(consert_list)


    post_id = collection.concert.insert_many(consert_list)
    print(post_id)
    print(post_id.inserted_ids)
    #print(db.list_collection_names())
    #print(collection.count_documents({'price': {'$lt': 10}}))
    a = collection.find()
    print(a)



def find_cheapest():
    collection.concert.find().sort([("price", 1)])
    print("\n Всех элементов бд по цене \n")
    for resalts in  collection.concert.find().sort([("price", 1)]):
         print(resalts)


def new_find_by_name(name):
    print("\n Поиск по имени \n")
    regex = re.compile(str(name))
    for item in collection.concert.find({"artist": regex}).sort([("price", 1)]):
        print(item)


# Запись в бд
read_data('artists.csv')

# Вывод исполнителей по стоимости
find_cheapest()


new_find_by_name('Seconds to')
collection.concert.drop()


