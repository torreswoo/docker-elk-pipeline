import os
import sys
import socket
import struct
import random
import datetime

from elasticsearch import Elasticsearch
from mappings import mappings

DATA_NUM = 1000
ES_INDEX_NAME = 'test_data'
ES_URL = 'localhost:9200'

def setup_index():

  # 01. ES client
  es_client = Elasticsearch(ES_URL)

  # 02. index 생성
  if es_client.indices.exists(ES_INDEX_NAME):
    print("index가 이미 존재합니다.")
    return

  es_client.indices.create(ES_INDEX_NAME)
  print("index가 생성되었습니다")

  # 03. mappings 적용
  es_client.indices.put_mapping(
    index=ES_INDEX_NAME,
    body=mappings,
  )
  print("mapping이 생성되었습니다")

  #
  n = int(DATA_NUM)

  for i in range(1, n+1):
    #
    order_id = i
    
    # 고객 나이
    age = random.choice(range(17, 65))

    # 고객 성별
    sex = random.choices(
      ['남성','여성'], 
      weights=[0.4, 0.6], k=1)[0]

    # 상품 카테고리
    item = random.choice(
      ['청바지', '자켓','팬츠','셔츠','원피스','스커트','코트','스웨터','티셔츠','가디건','니트','블라우스'])
    
    # 도시
    city = random.choices(
      ["서울특별시", "경상남도", "경상북도", "전라남도", "전라북도", "충청남도", "충청북도", "세종특별자치시", "강원도", "경기도", "울산광역시", "대전광역시", "광주광역시", "인천광역시", "대구광역시", "부산광역시", "제주특별자치도"], 
      weights=[0.3, 0.08, 0.03, 0.06, 0.07, 0.08, 0.03, 0.09, 0.063, 0.0205, 0.0305, 0.03, 0.05, 0.03, 0.001, 0.03, 0.005], k=1)[0]

    # 구매 사이트
    site = random.choices(
      ['11번가', '옥션', 'G마켓', '쿠팡', 'Naver', 'Kakao', '이마트'], 
      weights=[0.3, 0.1, 0.3, 0.12, 0.1, 0.05, 0.03], k=1)[0]

    # 판매자 평점
    rate = random.choices(
      [1, 2, 3, 4, 5], 
      weights=[0.3, 0.1, 0.3, 0.2, 0.1], k=1)[0]

    # 상품 가격
    price = random.choice(range(3000, 80000, 1500))

    # 상품 개수
    quantity = random.choice([1, 2, 3, 4, 5, 6, 7])

    # 결제 카드
    card = random.choices(
      ['우리', '신한', '국민', '하나', '롯데', '시티', '삼성'], 
      weights=[0.3, 0.1, 0.3, 0.12, 0.1, 0.05, 0.03], k=1)[0]

    #
    date = datetime.datetime(
      random.choice(range(2020, 2021)), 
      random.choices(range(1, 8), weights=[0.2, 0.1, 0.05, 0.05, 0.07, 0.03, 0.02], k=1)[0], 
      random.choice(range(1, 29)), 
      random.choice(range(0, 24)), 
      random.choice(range(0, 60)), 
      random.choice(range(0, 60)))
    
    document = dict()
    document['order_id'] = order_id
    document['order_주문시간'] = date
    # doc['order_배달시간'] = delivery_date
    # doc['예약여부'] = reserve
    # doc['customer_ip'] = ip
    document['customer_gender'] = sex
    document['customer_age'] = age
    document['customer_address'] = city
    # doc['product_위치'] = loc
    document['product_분류'] = item
    document['product_가격'] = price
    document['product_개수'] = quantity
    document['결제카드'] = card
    document['구매사이트'] = site
    document['평점'] = rate
    
    es_client.index(index=ES_INDEX_NAME, body=document)


if __name__ == "__main__":
    setup_index()

    print("완료")