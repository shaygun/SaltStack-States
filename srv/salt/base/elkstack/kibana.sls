install_kibana:
  pkg.installed:
    - sources:
      - kibana: https://artifacts.elastic.co/downloads/kibana/kibana-6.1.1-amd64.deb

enable_kibana:
  service.enabled:
    - name: kibana

start_kibana:
  service.running:
    - name: kibana
