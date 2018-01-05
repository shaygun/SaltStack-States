# -*- coding: utf-8 -*-
# docstring
'''
######### this is description to be added ######### (Delete)
X module for interactive with basic X commands.


:maintainer: Shakib Shaygan (shakib@shakib.xyz)
:maturity: 20180103
:requires: none
:platform: all

#information about the state in the top doc string. (Delete)
Example States
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

# Import python libraries
## absolute_import provide compatibiliy between pythonv2 and v3
## logging adds debugging output to module
from __future__ import absolute_import
import logging


# Globals ( Logging )
LOG = logging.getLogger(__name__)
LOG.info('info output')
LOG.debug('debug output')
LOG.error('error output')
LOG.warning('warning output')
LOG.critical('critical output')

# __virtualname__
## set the module name, if missing the file name will be, default will be the file name of the module(minus the .py).
__virtualname__ = 'module-name'

# __virtual__()
## critical component of any Salt execution module.
## This function allows you to enter logic to determine whether or not your module should load on the given platform.
def __virtual__():
    '''
    Determine whether or not to load this module
    '''
    if __salt__['grains.get']('kernel:Linux'):
        return __virtualname__

# private function
## Any function prefixed with an underscore character will only be available within the module, and will not be directly callable through Salt.
def _private():
    '''
    "Private" function; only callable within this module
    '''
    LOG.debug('Executing the _private function')

    ret = {}
    return ret

# Public function
## available to be called from Salt, prefixed by the module name.
## For example, if our custom module was called “module”, and our function name was “public”, we’d call this through Salt by targeting module.public.
def public(*args, **kwargs):
    '''
    "Public" function; available to Salt, ie; module.public

    CLI Example:

        salt '*' module.public
    '''
    LOG.debug('Executing the public function')

    ret = _private()
    return ret

























a
