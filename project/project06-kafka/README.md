# project06
- nginx log (w/Filebeat) -> kafka -> logstash -> elasticsearch -> kibana

![image](https://user-images.githubusercontent.com/11022719/90950109-97673f80-e489-11ea-981d-c51f54d7e299.png)

- http://localhost:5601/ (kibana)
- http://localhost:9200/ (Elasticsearch)
- http://localhost:8080/ (nginx, index.html)
- http://localhost:9000/ (kafka-manager)
```
mkdir -p ./beats/filebeat-project/log/nginx
docker-compose -f docker-compose.project.yml up
docker-compose -f docker-compose.project.yml up --force-recreate --build 
docker-compose up
docker-compose ls
docker ps
docker volume ls
```

### kafka Manager setting

![스크린샷 2020-10-26 오전 10 38 20](https://user-images.githubusercontent.com/11022719/97125573-b62ece80-1777-11eb-9eed-7da2209f2d9f.png)
