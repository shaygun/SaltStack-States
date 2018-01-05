##Manual way to create user
create_user_jhon:
  user.present:
    - name: jhon
    - fullname: jhon man
    - shell: /bin/bash
    - home: /home/jhon
    - uid: 10010
    - gid_from_name: True
    - groups:
      - root

ssh_key_jhon:
  ssh_auth.present:
    - name: ADMIN-USER
    - user: jhon
    - source: salt://users/keys/jhon.pub
