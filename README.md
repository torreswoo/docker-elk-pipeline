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

# Beats

## MetricBeat

### MetricBeat - local setup
- https://www.elastic.co/guide/en/beats/metricbeat/current/command-line-options.html
```
$ curl -L -O https://artifacts.elastic.co/downloads/beats/metricbeat/metricbeat-7.8.0-darwin-x86_64.tar.gz
tar xzvf metricbeat-7.8.0-darwin-x86_64.tar.gz

$ ./metricbeat setup --dashboards
$ ./metricbeat modules list 
$ ./metricbeat test config

$ ./metricbeat -e
$ ./metricbeat -e -c metricbeat.yml 

$ ./metricbeat modules enable system
$ ./metricbeat modules enable docker
```

### MetricBeat - docker setup
- elastic.co/guide/en/beats/metricbeat/current/load-kibana-dashboards.html
- https://www.elastic.co/guide/en/beats/metricbeat/current/running-on-docker.html
- https://www.elastic.co/guide/en/beats/metricbeat/current/metricbeat-module-docker.htmls


```
$ docker run --net=host docker.elastic.co/beats/metricbeat:7.8.0 setup --dashboards

$ curl -L -O https://raw.githubusercontent.com/elastic/beats/7.8/deploy/docker/metricbeat.docker.yml

$ docker run \
--name=metricbeat01 \
--user=root \
--volume="$(pwd)/metricbeat.docker.yml:/usr/share/metricbeat/metricbeat.yml:ro" \
--volume="/var/run/docker.sock:/var/run/docker.sock:ro" \
--volume="/sys/fs/cgroup:/hostfs/sys/fs/cgroup:ro" \
--volume="/proc:/hostfs/proc:ro" \
--volume="/:/hostfs:ro" \
--net=docker-elastic-pipeline_elk \
docker.elastic.co/beats/metricbeat:7.8.0 metricbeat -e \
-E output.elasticsearch.hosts=["elasticsearch:9200"]

```

