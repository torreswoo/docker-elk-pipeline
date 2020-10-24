# project03

![image](https://user-images.githubusercontent.com/11022719/97082383-36541780-1644-11eb-868e-6d1b52b2eeee.png)

- http://localhost:5601/
- http://localhost:9200/

```
docker-compose -f docker-compose.beats01.metricbeat.yml up
docker-compose -f docker-compose.beats01.metricbeat.yml up --force-recreate --build 
docker-compose up
docker-compose ls
docker ps
docker volume ls
```

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
--volume="$(pwd)/beats/metricbeat/metricbeat.docker.yml:/usr/share/metricbeat/metricbeat.yml:ro" \
--volume="/var/run/docker.sock:/var/run/docker.sock:ro" \
--volume="/sys/fs/cgroup:/hostfs/sys/fs/cgroup:ro" \
--volume="/proc:/hostfs/proc:ro" \
--volume="/:/hostfs:ro" \
--net=docker-elastic-pipeline_elk \
docker.elastic.co/beats/metricbeat:7.8.0 metricbeat -e \
-E output.elasticsearch.hosts=["elasticsearch:9200"]

```

## MetricBeat - sample metric
```json
{
   "monitoring":{
      "metrics":{
         "beat":{
            "cpu":{
               "system":{
                  "ticks":130,
                  "time":{
                     "ms":56
                  }
               },
               "total":{
                  "ticks":330,
                  "time":{
                     "ms":114
                  },
                  "value":330
               },
               "user":{
                  "ticks":200,
                  "time":{
                     "ms":58
                  }
               }
            },
            "handles":{
               "limit":{
                  "hard":1048576,
                  "soft":1048576
               },
               "open":21
            },
            "info":{
               "ephemeral_id":"bcd54f00-eaec-4324-b724-5b4b8c203955",
               "uptime":{
                  "ms":60092
               }
            },
            "memstats":{
               "gc_next":13732000,
               "memory_alloc":10473960,
               "memory_total":34078008,
               "rss":364544
            },
            "runtime":{
               "goroutines":82
            }
         },
         "libbeat":{
            "config":{
               "module":{
                  "running":0
               }
            },
            "output":{
               "events":{
                  "acked":63,
                  "batches":15,
                  "total":63
               },
               "read":{
                  "bytes":5566
               },
               "write":{
                  "bytes":105863
               }
            },
            "pipeline":{
               "clients":4,
               "events":{
                  "active":0,
                  "published":63,
                  "total":63
               },
               "queue":{
                  "acked":63
               }
            }
         },
         "metricbeat":{
            "docker":{
               "container":{
                  "events":6,
                  "success":6
               },
               "cpu":{
                  "events":6,
                  "success":6
               },
               "diskio":{
                  "events":6,
                  "success":6
               },
               "info":{
                  "events":3,
                  "success":3
               },
               "memory":{
                  "events":6,
                  "success":6
               },
               "network":{
                  "events":6,
                  "success":6
               }
            },
            "system":{
               "cpu":{
                  "events":3,
                  "success":3
               },
               "load":{
                  "events":3,
                  "success":3
               },
               "memory":{
                  "events":3,
                  "success":3
               },
               "network":{
                  "events":12,
                  "success":12
               },
               "process":{
                  "events":3,
                  "success":3
               },
               "process_summary":{
                  "events":3,
                  "success":3
               },
               "socket_summary":{
                  "events":3,
                  "success":3
               }
            }
         },
         "system":{
            "load":{
               "1":0.9,
               "15":0.45,
               "5":0.71,
               "norm":{
                  "1":0.3,
                  "15":0.15,
                  "5":0.2367
               }
            }
         }
      }
   }
}
```
