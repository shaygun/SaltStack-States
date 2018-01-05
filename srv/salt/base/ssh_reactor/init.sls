sshd_config:
  file.managed:
    - name: /etc/ssh/sshd_config
    - source: salt://ssh_reactor/templates/sshd_config
    - user: root
    - group: root
    - mode: 0644

stop_sshd:
  service.dead:
    - name: ssh

start_sshd:
  service.running:
    - name: ssh
    - require:
      - service: stop_sshd

#salt '*' state.sls sshd_reactor  ( to test )
