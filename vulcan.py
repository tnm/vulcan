"""
Vulcan: the highly logical way to populate Redis

Example:

	from vulcan import Vulcan
	s = Vulcan(10000, 'strings') # We want 10,000 random strings
	s.populate() # Populate the database
"""

__author__ = 'Ted Nyman'
__version__ = '0.1.1'
__license__ = 'MIT'

import redis
import random
from random import randint

class VulcanError(Exception):
    def __init__(self, msg, error_code=None):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)

class Vulcan(object):
    """
    Generate data for Redis	
    """
    def __init__(self, size, datatype='strings'):
        """
        Size is an integer representing how many keys you want. 
        Datatype can be 'strings', 'lists', 'sets', or 'zsets, or
        'hashes.' The default data type is 'strings'.	
        """
        self.size = size		
        self.datatype = datatype
	
    def populate(self):
        """
        Populate Redis with random values.
        """
        size = self.size
        datatype = self.datatype

        if type(size) == int:

            if datatype == 'strings':
                r = redis.Redis(host='localhost', port=6379, db=5)
                r.flushdb()
                bunch_o_keys = range(size)
                for i in bunch_o_keys: 
                    r.set(i, (randint(0, size)))

            elif datatype == 'lists':
                r = redis.Redis(host='localhost', port=6379, db=6)
                r.flushdb()
                bunch_o_keys = range(size)
                for i in bunch_o_keys:
                    r.lpush(i,(randint(0, size)))

            elif datatype == 'sets':
                r = redis.Redis(host='localhost', port=6379, db=7)
                r.flushdb()
                bunch_o_keys = range(size)
                for i in bunch_o_keys:
                    r.sadd(i,(randint(0, size)))

            elif datatype == 'zsets':
                r = redis.Redis(host='localhost', port=6379, db=8)
                r.flushdb()
                bunch_o_keys = range(size)
                for i in bunch_o_keys:
                    r.zadd(i,(randint(0, size)), (randint(0, size)))

            elif datatype == 'hashes':
                r = redis.Redis(host='localhost', port=6379, db=9)
                r.flushdb()
                bunch_o_keys = range(size)
                for i in bunch_o_keys:
                    r.hset(i,(randint(0, size)), (randint(0, size)))

            else:
                raise VulcanError("Must specify a valid Redis datatype. %s" %(e))

        else:
            raise VulcanError("Must specify a valid Redis datatype. %s" %(e))

