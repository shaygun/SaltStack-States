dev:
  '*':
    - users.dev_users
#if you use init.sls, top file will not require ".dev_users"
#.dev_users is the name of the state file inside the users folder

#base state will be combined with dev states and all run together
#method of deviding the state files
