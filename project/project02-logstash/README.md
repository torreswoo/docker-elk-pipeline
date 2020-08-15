# project02

- FILE -> logstash -> elasticsearch
<img width="1391" alt="" src="https://user-images.githubusercontent.com/11022719/86531824-837a7500-beff-11ea-8d04-c5f06235283f.png">

- http://localhost:5601/
- http://localhost:9200/
- http://localhost:9600/

```
docker-compose -f docker-compose.logstash02.yml up
docker-compose -f docker-compose.logstash02.yml up --force-recreate --build 
docker-compose up
docker-compose ls
docker ps
docker volume ls

curl -X POST 'http://127.0.0.1:5000' -d '{ "id" : 1, "order_number" : 12, "customer_no": 23781, "category": "셔츠"}'
```

## Logstash

### Logstash - File input plugin

### Logstash Pattern
- https://github.com/logstash-plugins/logstash-patterns-core/tree/master/patterns
