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


## Filebeat

### Filebeat - local setup
```
$ curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.1.0-darwin-x86_64.tar.gz
$ tar -xvf filebeat-7.1.0-darwin-x86_64.tar.gz

$ cd filebeat-7.1.0-darwin-x86_64

$ ./filebeat setup --dashboards
$ ./filebeat export config
$ ./filebeat export template --es.version 7.6.2 --index filebeat-*
$ ./filebeat modules enable nginx
$ sudo chown root filebeat.yml
$ sudo chown root modules.d/nginx.yml
$ sudo chown root module/nginx/access/manifest.yml
$ sudo chown root module/nginx/error/manifest.yml

$ ./filebeat -e

```
### Filebeat - docker setup


### Filebeat - nginx log (w/Filebeat) -> logstash -> elasticsearch
```
docker-compose -f docker-compose.filebeat.yml up
```