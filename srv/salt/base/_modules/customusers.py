# turn the list to csv output
__virtualname__ = 'awsome'

def __virtual__():
    if __grains__['os_family'] == 'Redhat':
        return False
    return __virtualname__

def users_as_csv():
    user_list = __salt__['user.list_users']()
    csv = ','.join(user_list)
    return csv

#dont forget salt '*' saltutil.sync_all
# to run salt '*' customusers.users_as_csv ( without __virtual__ it will work only)
# salt '*' awsome.users_as_csv
# __virtual__ are usually used to identify the functio names dynamically
