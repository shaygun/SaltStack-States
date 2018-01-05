# -*- coding: utf-8 -*-
'''
######### this is description to be added #########
Redis module for interactive with basic redis commands.


######### version of saltstack that this module added to  #########
.. versionadded:: Nitrogen

######### A depends string, to let the user know that the redis python module is required. #########
:depends: redis

#########  example configuration if you one is possible to be used. #########
Example configuration

.. code-block:: yaml
    redis:
      host: 127.0.0.1
      port: 6379
      database: 0
      password: None
'''
#####################################################
#Then we have the imports. We catch the import error on
#redis, and set HAS_REDIS as False if it can't be
#imported so that we can reference it in
#the __virtual__ function and know if the module should
# be available or not.

from __future__ import absolute_import

# Import python libraries
try:
    import redis
    HAS_REDIS = True
except ImportError:
    HAS_REDIS = False
#####################################################

#####################################################
#__virtualname__ is used to change the name the module should be loaded under.
# this is name of the module
__virtualname__ = 'redis'
#####################################################

#####################################################
#The __virtual__ function is used to decide if the module can be used or not.
#If it can be used and it has a __virtualname__ variable, return that variable.
#Otherwise if it is to be named after the name of the file, just return True.
def __virtual__():
    '''
    Only load this module if redis python module is installed
    '''
    if HAS_REDIS:
        return __virtualname__
    return (False, 'The redis execution module failed to load: redis python module is not available')
#####################################################

#####################################################
def _connect(host=None, port=None, database=None, password=None):
    '''
    Return redis client instance
    '''
    if not host:
        host = __salt__['config.option']('redis.host')
    if not port:
        port = __salt__['config.option']('redis.port')
    if not database:
        database = __salt__['config.option']('redis.database')
    if not password:
        password = __salt__['config.option']('redis.password')
    name = '_'.join([host, port, database, password])

    #__context__. This is a really usefull for connections,
    #because you only have to setup the connection one time,
    #and then you can continually just return it and use it
    #every time the module is used, instead of having to
    #reinitialize the connection.
    if name not in __context__:
        __context__[name] = redis.StrictRedis(host, port, database, password)
    return __context__[name]
#####################################################

#####################################################
def get(key, host=None, port=None, database=None, password=None):
#this is calle docstring and should always availble for each function
#that gets showed when you run salt-call sys.doc <module.function>
    '''
    Get Redis key value

    CLI Example:

    .. code-block:: bash

        salt '*' redis.get foo
        salt '*' redis.get bar host=127.0.0.1 port=21345 database=1
    '''
    server = _connect(host, port, database, password)
    return server.get(key)
#####################################################

def set(key, value, host=None, port=None, database=None, password=None):
    '''
    Set Redis key value

    CLI Example:

    .. code-block:: bash

        salt '*' redis.set foo bar
        salt '*' redis.set spam eggs host=127.0.0.1 port=21345 database=1
    '''
    server = _connect(host, port, database, password)
    return server.set(key, value)


def delete(key, host=None, port=None, database=None, password=None):
    '''
    Delete Redis key value

    CLI Example:

    .. code-block:: bash

        salt '*' redis.delete foo bar
        salt '*' redis.delete spam host=127.0.0.1 port=21345 database=1
    '''
    server = _connect(host, port, database, password)
    return server.delete(key, value)
