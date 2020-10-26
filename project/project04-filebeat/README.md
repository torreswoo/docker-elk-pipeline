# project04
- nginx log (w/Filebeat) -> logstash -> elasticsearch
<img width="1373" alt="스크린샷 2020-07-05 오후 8 40 53" src="https://user-images.githubusercontent.com/11022719/86531859-d3f1d280-beff-11ea-9ea6-e6a6b9991727.png">

- http://localhost:5601/
- http://localhost:9200/
- http://localhost:8080/

```
mkdir -p ./beats/filebeat-nginx/log/nginx
docker-compose -f docker-compose.beats02.filebeat.yml up
docker-compose -f docker-compose.beats02.filebeat.yml up --force-recreate --build 
docker-compose up
docker-compose ls
docker ps
docker volume ls
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

### Filebeat & Logstash

- input : project02/beats/filebeat-nginx/log/nginx/access.log
```
172.20.0.1 - - [28/Jun/2020:16:42:31 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36" "-"
```

- filter & output : project02/logstash/ pipeline/logstash.conf & pattern/nginx.pattern
```json
{
   "ecs":{
      "version":"1.4.0"
   },
   "verb":"GET",
   "response":304,
   "bytes":0,
   "tags":[
      "beats_input_codec_plain_applied"
   ],
   "message":"172.20.0.1 - - [28/Jun/2020:16:42:31 +0000] "   GET / HTTP/1.1   " 304 0 "   "-"   " "   Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML,
   like Gecko) Chrome/83.0.4103.116 Safari/537.36   " "   "-"   "",
   "httpversion":"1.1",
   "log":{
      "file":{
         "path":"/var/log/nginx/access.log"
      },
      "offset":2569
   },
   "ident":"-",
   "clientip":"172.20.0.1",
   "@version":"1",
   "request":"/",
   "@timestamp":"2020-07-05T08:06:08.903Z",
   "type":"nginx-access",
   "timestamp":"28/Jun/2020:16:42:31 +0000",
   "host":{
      "name":"980e31a6ffd5"
   },
   "agent":{
      "version":"7.6.2",
      "type":"filebeat",
      "ephemeral_id":"8fb63cdd-2b14-4906-b8d9-d155e296146f",
      "id":"771c5264-f817-43ad-955c-e231e70aeda3",
      "hostname":"980e31a6ffd5"
   },
   "auth":"-"
}
```
