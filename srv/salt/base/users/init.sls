#################Create user with Jinja Template#################
## it will use pillars in /srv/salt/pillars/base/users/init.sls
{% for user, data in pillar.get('admin_users', {}).items() %}

### Create User from Pillar List ######
{{ user }}:
  user.present:
    - home: {{ data['home'] }}
    - shell: {{ data['shell'] }}
    - uid: {{ data['uid'] }}
{% if 'password' in data %}
    - password: {{ data['password'] }}
{% if 'enforce_password' in data %}
    - enforce_password: {{ data['enforce_password'] }}
{% endif %}
{% endif %}
    - fullname: {{ data['fullname'] }}
{% if 'groups' in data %}
    - groups: {{ data['groups'] }}
{% endif %}

#################### Copy your ssh pub key to this user #############
# it will not generate public key for the user
{% if 'key.pub' in data and data['key.pub'] == True %}
{{ user }}_key:
  ssh_auth.present:
    - user: {{ user }}
    - source: salt://users/keys/{{ user }}.pub
    - require:
      - user: {{ user }}

{% endif %}

############ SSH KEYGEN ###############

{{ user }}_keygen:
  cmd.run:
    - name: ssh-keygen -q -N '' -f /home/{{ user }}/.ssh/id_rsa
    - runas: {{ user }}
    - unless: test -f /home/{{ user }}/.ssh/id_rsa


{% endfor %}

########### OR #############
#this script work fine without for loop
#pay attention to pillar address 
#havij:
#  user.present:
#    - fullname: {{ pillar['admin_users']['havij']['fullname'] }}
#    - password: {{ pillar['admin_users']['havij']['password'] }}
#    - groups: {{ pillar['admin_users']['havij']['groups'] }}
