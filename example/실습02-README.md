## Kibana - Devtool

```bash
DELETE /log-2020-07-21
GET /log-2020-07-21/_mapping

POST /log-2020-07-21/_doc/1
{  
    "projectName" : "카카오",
    "logType": "web-log",
    "logSource": "장바구니",
    "logTime":"2020-07-21T06:07:49",
    "host": "host01",
    "body": "[2020-07-21T06:07:49.332Z] GET /beats HTTP/1.1 200 7691 - Mozilla/5.0 (X11; Linux x86_64; rv:6.0a1) Gecko/20110421 Firefox/6.0a1"
}
POST /log-2020-07-21/_doc/2
{  
    "projectName" : "카카오",
    "logType": "web-log",
    "logSource": "장바구니2",
    "logTime":"2020-07-21T08:07:49",
    "host": "host02",
    "body": "[2020-07-21T06:07:49.332Z] GET /beats HTTP/1.1 200 7691 - Mozilla/5.0 (X11; Linux x86_64; rv:6.0a1) Gecko/20110421 Firefox/6.0a1"
}

GET log-2020-07-21/_search
```

## templates & index 정보확인
```bash
# templates 정보확인
GET /_cat/templates?v 
# index 정보확인 
GET /_cat/indices?v

# test_index 인덱스 생성 & 정보확인
PUT test_index
GET /test_index/_stats 
GET /test_index/_settings 
GET /test_index/_mapping
```

## String - keywork & text
```bash
PUT _template/test_template
{
  "index_patterns": [
    "test_index"
  ],
  "mappings": {
    "properties": {
      "book_name01": {
        "type": "keyword"
      },
      "book_name02": {
        "type": "text"
      }
    }
  }
}

POST test_index/_doc
{
  "book_name01": " 검색엔진 완전 정복",
  "book_name02": " 검색엔진 완전 정복"
}

GET /test_index/_search
{
  "query": {
    "term": {
      "book_name01": "완전"
    }
  }
}


GET /test_index/_search
{
  "query": {
    "term": {
      "book_name02": "완전"
    }
  }
}
```

## Date
```bash
PUT my_index
{
  "mappings": {
    "properties": {
      "date": {
        "type": "date" 
      }
    }
  }
}

PUT my_index/_doc/1
{ "date": "2015-01-01" } 

PUT my_index/_doc/2
{ "date": "2015-01-01T12:10:30Z" } 

PUT my_index/_doc/3
{ "date": 1420070400001 } 

GET my_index/_search
{
  "sort": { "date": "asc"} 
}

```

## Geo Point
```bash


PUT my_index02
{
  "mappings": {
    "properties": {
      "location": {
        "type": "geo_point"
      }
    }
  }
}

# 02. save Document
PUT my_index02/_doc/1
{
  "text": "Geo-point as an object",
  "location": { 
    "lat": 41.12,
    "lon": -71.34
  }
}

PUT my_index02/_doc/2
{
  "text": "Geo-point as a string",
  "location": "41.12,-71.34" 
}

PUT my_index02/_doc/3
{
  "text": "Geo-point as a geohash",
  "location": "drm3btev3e86" 
}

PUT my_index02/_doc/4
{
  "text": "Geo-point as an array",
  "location": [ -71.34, 41.12 ] 
}

PUT my_index02/_doc/5
{
  "text": "Geo-point as a WKT POINT primitive",
  "location" : "POINT (-71.34 41.12)" 
}

# 03. search
GET my_index02/_search
{
  "query": {
    "geo_bounding_box": { 
      "location": {
        "top_left": {
          "lat": 41.5,
          "lon": -72
        },
        "bottom_right": {
          "lat": 40,
          "lon": -74
        }
      }
    }
  }
}
```

## template을 index생성 전에 적용
```bash
# test_index_mapping_api 인덱스에 test_template_mapping_api 템플릿 생성
PUT _template/test_template_mapping_api
{
  "index_patterns": [
    "test_index_mapping_api"
  ],
  "mappings": {
    "properties": {
      "book_name": {
        "type": "keyword"
      },
      "description": {
        "type": "text"
      },
      "price": {
        "type": "integer"
      },
      "location": {
        "type": "geo_point"
      },
      "order_time": {
        "type": "date"
      }
    }
  }
}

POST test_index_mapping_api/_doc/1
{
  "book_name": "검색엔진 완전 정복",
  "description": "이 책은 검색엔진에 관현 책이며, 완전 정복 책으로 베스트 셀러 10위이다.",
  "price": 25000,
  "location": "41.12,-71.35",
  "order_time": "2020-07-25T12:10:30Z"
}

GET test_index_mapping_api/_search
{
  "query": {
    "match_all": {}
  }
}

GET test_index_mapping_api/_search
{
  "query": {
    "term": {
      "book_name": "검색엔진 완전 정복"
    }
  }
}

GET test_index_mapping_api/_search
{
  "query": {
    "term": {
      "description": "완전"
    }
  }
}
```
