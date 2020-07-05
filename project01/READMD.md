# project01

- HTTP -> logstash -> elasticsearch

- http://localhost:5601/
- http://localhost:9200/
- http://localhost:9600/
- http://localhost:5000/

```
docker-compose -f docker-compose.logstash01.yml up
docker-compose -f docker-compose.logstash01.yml up --force-recreate --build 
docker-compose up
docker-compose ls
docker ps
docker volume ls

curl -X POST 'http://127.0.0.1:5000' -d '{ "id" : 1, "order_number" : 12, "customer_no": 23781, "category": "셔츠"}'
```

## Logstash

### Logstash - HTTP input plugin
- http input : https://www.elastic.co/guide/en/logstash/current/plugins-inputs-http.html

```
# pipeline/logstash.conf
# pipeline/logstash02.conf
curl -X POST 'http://127.0.0.1:5000' -d '{ "id" : 1, "order_number" : 12, "customer_no": 23781, "category": "셔츠"}'

# pipeline/logstash02.conf
```