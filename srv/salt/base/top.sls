base:
  '*':
    - users
    - shell_exec

  'web*':
    - elkstack

#the users state will run for all servers, the apache state will only run
#for servers that their name starts with web
