install_logstash:
  pkg.installed:
    - sources:
      - logstash: https://artifacts.elastic.co/downloads/logstash/logstash-6.1.1.deb

enable_logstash:
  service.enabled:
    - name: logstash

start_logstash:
  service.running:
    - name: logstash
