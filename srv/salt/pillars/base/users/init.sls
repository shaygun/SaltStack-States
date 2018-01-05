{% set admin_group = 'sudo' if grains['os'] == 'Ubuntu' else 'root' %}
admin_group: {{ admin_group }}

admin_users:
  shakib:
    fullname: shakib shaygan
    shell: /bin/bash
    home: /home/shakib
    uid: 5001
    gid_from_name: True
    groups:
      - {{ admin_group }}
    password: $6$FJ1eNYMZ$d754DxNNKe0hetlA3M2bsohF7IGUo9I7ePt8aa9uETn3/kYi7iJ35ffxRICt9URohltsOuyqFQ3wOvPkEVTCn0
    #user@1234
    enforce_password: True
    key.pub: True
    #ssh_key: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCSIMNhf8KxfvYkV7iVW21WEyYjclHDP0EaA/zHIpAnvkgt1C3CV0pmvoqw0dy286fC6SZfG+IfH+YrjCNUpNvtZXXvLypV8TlOIM54fy9B5Q6BFKmil59eK57XesV0Dbtq5E1EVe2Wj8Ej/x9/Pow4Fe8MBCpzRi7i5ApN2MlJdm/MXgGKFP4xtUrLCx/2l5R3byawV/8Y6gKyND9jvUIXh4VN5+wcRBkD3Wgzu5v2TVP4oJgU+VoON/2rb4/lXdlJljjFAwdzwwVkHmFI2t7qZUeNa5izLev7KTqP7kmdGsBtc3vu8RkdeWm5dsPs2NzNAYN6IdAqbctGAlRUKeCD mypc.local

  sara:
    fullname: sara alexander
    shell: /bin/bash
    home: /home/sara
    uid: 5002
    gid_from_name: True
    groups:
      - {{ admin_group }}
    password: $6$FJ1eNYMZ$d754DxNNKe0hetlA3M2bsohF7IGUo9I7ePt8aa9uETn3/kYi7iJ35ffxRICt9URohltsOuyqFQ3wOvPkEVTCn0
    #user@1234
    enforce_password: True
    key.pub: True
    #ssh_key: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCSIMNhf8KxfvYkV7iVW21WEyYjclHDP0EaA/zHIpAnvkgt1C3CV0pmvoqw0dy286fC6SZfG+IfH+YrjCNUpNvtZXXvLypV8TlOIM54fy9B5Q6BFKmil59eK57XesV0Dbtq5E1EVe2Wj8Ej/x9/Pow4Fe8MBCpzRi7i5ApN2MlJdm/MXgGKFP4xtUrLCx/2l5R3byawV/8Y6gKyND9jvUIXh4VN5+wcRBkD3Wgzu5v2TVP4oJgU+VoON/2rb4/lXdlJljjFAwdzwwVkHmFI2t7qZUeNa5izLev7KTqP7kmdGsBtc3vu8RkdeWm5dsPs2NzNAYN6IdAqbctGAlRUKeCD mypc.local

  joe:
    fullname: joe garfula
    shell: /bin/bash
    home: /home/joe
    uid: 5003
    gid_from_name: True
    groups:
      - {{ admin_group }}
    password: $6$FJ1eNYMZ$d754DxNNKe0hetlA3M2bsohF7IGUo9I7ePt8aa9uETn3/kYi7iJ35ffxRICt9URohltsOuyqFQ3wOvPkEVTCn0
    #user@1234
    enforce_password: True
    key.pub: True
    #ssh_key: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCSIMNhf8KxfvYkV7iVW21WEyYjclHDP0EaA/zHIpAnvkgt1C3CV0pmvoqw0dy286fC6SZfG+IfH+YrjCNUpNvtZXXvLypV8TlOIM54fy9B5Q6BFKmil59eK57XesV0Dbtq5E1EVe2Wj8Ej/x9/Pow4Fe8MBCpzRi7i5ApN2MlJdm/MXgGKFP4xtUrLCx/2l5R3byawV/8Y6gKyND9jvUIXh4VN5+wcRBkD3Wgzu5v2TVP4oJgU+VoON/2rb4/lXdlJljjFAwdzwwVkHmFI2t7qZUeNa5izLev7KTqP7kmdGsBtc3vu8RkdeWm5dsPs2NzNAYN6IdAqbctGAlRUKeCD mypc.local

  havij:
    fullname: havij havijian
    shell: /bin/bash
    home: /home/havij
    uid: 5004
    groups:
      - root
    password: $6$FJ1eNYMZ$d754DxNNKe0hetlA3M2bsohF7IGUo9I7ePt8aa9uETn3/kYi7iJ35ffxRICt9URohltsOuyqFQ3wOvPkEVTCn0
