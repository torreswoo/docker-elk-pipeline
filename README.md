# Elastic Stack Pipeline
- using Docker

### Quick start
```
docker-compose up
docker-compose -f docker-compose.yml up
docker-compose ls
docker ps
docker volume ls
```

### docker-compose file

#### docker-compose.yml
- Dockerfile를 가지고 ELK실행

#### docker-compose.simple.yml
- docker image만으로 elasticsearch, kibana를 실행

#### docker-compose.xpack.yml
- `xpack.license.self_generated.type=basic` "basic" 일부 xpack의 기능을 무료로 사용가능, trial은 30일 체험버전
- `xpack.security.enabled=true`로 하면 user/pw를 가지고 클러스터에 접근해야한다.
- kibana UI에서 Security가 활성화되고, user & role를 설정할 수 있다.

```
$ curl -XGET -u elastic:changeme http://localhost:9200/_xpack/security/user?pretty
$ curl -XGET http://elastic:changeme@localhost:9200/_xpack/security/user?pretty
```

### Project List

- project01 : Logstash (HTTP input plugin) & codec JSON 
- project02 : Logstash (File input plugin & filter plugin) & apache log 파싱
- project03 : MetricBeat & 시스템 메트릭
- project04 : FileBeat & Logstash (Beats & Grok Plugin) & 로그파일수집
- project05 : Multi Node Elasticsearch Cluster
- project06 : Beats, Kafka, Logstash, Elasticsearch, Kibana
