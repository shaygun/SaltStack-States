install_filebeat:
  pkg.installed:
    - sources:
      - filebeat: https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-6.1.1-amd64.deb

enable_filebeat:
  service.enabled:
    - name: filebeat

start_filebeat:
  service.running:
    - name: filebeat
