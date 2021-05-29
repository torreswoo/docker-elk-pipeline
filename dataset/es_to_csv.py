# -*- coding: utf8 -*-
import csv
from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=["localhost:9200"])
data = es.search(
        index="test_data",
        size=10000,
        body={
            "query" : {
                "match_all" : {
                    }
                }
            }
        )

csv_columns = ['customer_address', 'customer_age', 'customer_gender', 'order_id', 'order_주문시간', 'product_가격', 'product_개수', 'product_분류', '결제카드', '구매사이트', '평점']
csv_file = './test_dataset.csv'

with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for document in [x['_source'] for x in data['hits']['hits']]:
        writer.writerow(document)
