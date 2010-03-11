"""
Vulcan: the highly logical way to populate Redis

Example:

	from vulcan import Vulcan
	s = Vulcan(10000, 'strings') # We want 10,000 random strings
	s.populate() #Populate the database
"""

__author__ = 'Ted Nyman'
__version__ = '0.1.0'
__license__ = 'MIT'

import redis
import random
from random import randint

class Vulcan(object):
    """
    Generate data for Redis	
    """
    def __init__(self, size, datatype='strings'):
        """
        Size is an integer representing how many keys you want. 
        Datatype can be 'strings', 'lists', 'sets', or 'zsets.' 
        'Strings' is the default datatype.		
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
	        r = redis.Redis(host='localhost', port=6379, db=6)
	        r.flushdb()
	        bunch_o_keys = range(size)
	        for i in bunch_o_keys: 
	            r.set(i, (randint(0, size)))

            elif datatype == 'lists':
	        r = redis.Redis(host='localhost', port=6379, db=7)
	        r.flushdb()
	        bunch_o_keys = range(size)
	        for i in bunch_o_keys:
	            r.lpush(i,(randint(0, size)))

            elif datatype == 'sets':
	        r = redis.Redis(host='localhost', port=6379, db=8)
	        r.flushdb()
	        bunch_o_keys = range(size)
	        for i in bunch_o_keys:
                    r.sadd(i,(randint(0, size)))

            elif datatype == 'zsets':
	        r = redis.Redis(host='localhost', port=6379, db=9)
	        r.flushdb()
	        bunch_o_keys = range(size)
	        for i in bunch_o_keys:
                    r.zadd(i,(randint(0, size)), (randint(0, size)))

            else:
                print "Error, can't populate. Options are 'strings', 'lists', 'sets', or 'zsets'. To do otherwise would be illogical."

        else:
	    print "Error, can't populate. You must specify an integer for the number of values." 
 




			
	
