```
docker-compose up
docker-compose ls
docker ps
docker volume ls
```


# Logstash
- http://localhost:9600/
- http input : https://www.elastic.co/guide/en/logstash/current/plugins-inputs-http.html

```
# pipeline/logstash.conf
# pipeline/logstash02.conf
curl -X POST 'http://127.0.0.1:5000' -d '{ "id" : 1, "order_number" : 12, "customer_no": 23781, "category": "셔츠"}'

# pipeline/logstash02.conf
```
