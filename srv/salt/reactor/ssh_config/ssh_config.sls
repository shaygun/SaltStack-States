enforce_salt_config:
  local.state.sls:
    - tgt: {{ data['id'] }}
    - arg:
      - ssh_reactor

#this works
#clean_tmp:
#  local.cmd.run:
#    - tgt: 'os:Ubuntu'
#    - expr_form: grain
#    - arg:
#      - rm -rf /tmp/*
