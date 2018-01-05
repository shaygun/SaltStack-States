enforce_nginx_service:
  local.state.sls:
    - tgt: {{ data['id'] }}
    - arg:
      - nginx_reactor


#this works
#clean_tmp:
#  local.cmd.run:
#    - tgt: 'os:Ubuntu'
#    - expr_form: grain
#    - arg:
#      - rm -rf /tmp/*
