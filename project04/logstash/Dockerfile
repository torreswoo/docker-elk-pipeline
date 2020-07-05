ARG ELK_VERSION

# https://www.docker.elastic.co/
FROM docker.elastic.co/logstash/logstash:${ELK_VERSION}

# Add your logstash plugins setup here
# Example: RUN logstash-plugin install logstash-filter-json
# RUN bin/logstash-plugin install --no-verify
# RUN bin/logstash-plugin logstash-input-http
# RUN bin/logstash-plugin logstash-input-file

RUN bin/logstash-plugin list 
