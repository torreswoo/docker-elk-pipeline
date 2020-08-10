# project06
- nginx log (w/Filebeat) -> kafka -> logstash -> elasticsearch -> kibana

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
