# project06
- nginx log (w/Filebeat) -> kafka -> logstash -> elasticsearch -> kibana

![image](https://user-images.githubusercontent.com/11022719/90950109-97673f80-e489-11ea-981d-c51f54d7e299.png)

- http://localhost:5601/
- http://localhost:9200/
- http://localhost:8080/

```
docker-compose -f docker-compose.project.yml up
docker-compose -f docker-compose.project.yml up --force-recreate --build 
docker-compose up
docker-compose ls
docker ps
docker volume ls
```
