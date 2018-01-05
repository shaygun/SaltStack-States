start_nginx:
  service.running:
    - name: nginx

#salt '*' state.sls nginx_service_reactor  ( to test )
