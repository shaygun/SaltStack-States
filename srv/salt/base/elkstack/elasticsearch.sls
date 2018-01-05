install_elasticsearch:
  pkg.installed:
    - sources:
      - elasticsearch: https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.1.1.deb

enable_elasticsearch:
  service.enabled:
    - name: elasticsearch

start_elasticsearch:
  service.running:
    - name: elasticsearch
