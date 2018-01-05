beacons:
  inotify: # inotify watch file module
    /etc/ssh/sshd_config:
      mask:
        - modify
  service:
    nginx:
      onchangeonly: True
  diskusage:
    - /: 70%
    - interval: 60
