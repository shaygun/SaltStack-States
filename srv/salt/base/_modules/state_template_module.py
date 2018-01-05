# -*- coding: utf-8 -*-
#https://docs.saltstack.com/en/latest/ref/states/writing.html

'''
Management of  Redis servers
============================

.. versionadded:: Nitrogen

:depends: redis
:configuration: see :py:mod:`salt.modules.redis` for setup instructions

Example States
#information about the state in the top doc string.
.. code-block:: yaml

    set redis key:
      redis.present:
        - name: key
        - value: value

    set redis key with host args:
      redis.absent:
        - name: key
        - host: 127.0.0.1
        - port: 1234
        - database: 3
        - password: somepass
'''

#####################################################
from __future__ import absolute_import
#####################################################

#####################################################
#__virtualname__ is used to change the name the module should be loaded under.
# this is name of the module
__virtualname__ = 'redis'
#####################################################

#####################################################
##if the redis.set_key module is loaded in the __salt__ dunder.
#If it is not loaded, we know we can't do any work in this
#state, and we should return False.
def __virtual__():
    if 'redis.set' in __salt__:
        return __virtualname__
    return (False, 'The redis execution module failed to load: redis python module is not available')
#####################################################

#####################################################
#
def present(name, value, host=None, port=None, database=None, password=None):
    '''
    Ensure key and value pair exists

    name
        Key to ensure it exists

    value
        Value the key should be set to

    host
        Host to use for connection

    port
        Port to use for connection

    database
        Database key should be in

    password
        Password to use for connection
    '''
#doctring for function need to be added #

#We have a return dictionary and it always includes the following:
#a default ret variable that describes what happens when the state
#fails, so I can just return it on failure at the end.
    ret = {'name': name,
           'changes': {},
           'result': False,
           'comment': 'Failed to set key {key} to value {value}'.format(key=name, value=value)}

#
    connection = {'host': host, 'port': port, 'database': database, 'password': password}
    current = __salt__['redis.get'](name, **connection)
    if current == value:
        ret['result'] = True
        ret['comment'] = 'Key {key} is already value correct'.format(key=name)
        return ret

    if __opts__['test'] is True:
        ret['result'] = None
        ret['changes'] = {
            'old': {name: current},
            'new': {name: value},
        }
        ret['pchanges'] = ret['changes']
        ret['comment'] = 'Key {key} will be updated.'.format(key=name)
        return ret

    __salt__['redis.set'](name, value, **connection)

    current, old = __salt__['redis.get'](name, **connection), current

    if current == value:
        ret['result'] = True
        ret['comment'] = 'Key {key} was updated.'.format(key=name)
        ret['changes'] = {
            'old': {name: old},
            'new': {name: current},
        }
        return ret

    return ret
#####################################################

#####################################################
def absent(name, host=None, port=None, database=None, password=None):
    '''
    Ensure key is not set.

    name
        Key to ensure it does not exist

    host
        Host to use for connection

    port
        Port to use for connection

    database
        Database key should be in

    password
        Password to use for connection
    '''
    ret = {'name': name,
           'changes': {},
           'result': False,
           'comment': 'Failed to delete key {key}'.format(key=name, value=value)}

    connection = {'host': host, 'port': port, 'database': database, 'password': password}
    current = __salt__['redis.get'](name, **connection)
    if current is None:
        ret['result'] = True
        ret['comment'] = 'Key {key} is already absent'.format(key=name)
        return ret

    if __opts__['test'] is True:
        ret['result'] = None
        ret['changes'] = {
            'old': {name: current},
            'new': {name: None},
        }
        ret['pchanges'] = ret['changes']
        ret['comment'] = 'Key {key} will be deleted.'.format(key=name)
        return ret

    __salt__['redis.delete'](name, value, **connection)

    current, old = __salt__['redis.get'](name, **connection), current

    if current is None:
        ret['result'] = True
        ret['comment'] = 'Key {key} was deleted.'.format(key=name)
        ret['changes'] = {
            'old': {name: old},
            'new': {name: current},
        }
        return ret

    return ret
#####################################################
