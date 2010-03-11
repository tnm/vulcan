import unittest
import vulcan
import redis

r6 = redis.Redis(host='localhost', port=6379, db=6)
r7 = redis.Redis(host='localhost', port=6379, db=7)
r8 = redis.Redis(host='localhost', port=6379, db=8)
r9 = redis.Redis(host='localhost', port=6379, db=9)

class TestVulcan(unittest.TestCase):
    """What is Kiri-kin-tha's first law of metaphysics?"""

    def setUp(self):
        """Adjust the sine wave of this magnetic envelope so that anti-neutrons can 
        pass through it but anti-gravitons cannot."""
	r6.flushdb()
	r7.flushdb()
	r8.flushdb()
	r9.flushdb()

 	self.s = vulcan.Vulcan(1000, 'strings')
 	self.l = vulcan.Vulcan(1000, 'lists')
 	self.se = vulcan.Vulcan(1000, 'sets')
 	self.z = vulcan.Vulcan(1000, 'zsets')

    def test_populate(self):
        """What is the electronic configuration of gadolinium?"""
	s = self.s
	l = self.l
	se = self.se
	z = self.z

	s.populate()
	all_keys = r6.keys('*')
	self.assertEquals(len(all_keys), 1000)
	
        l.populate()
	all_keys = r7.keys('*')
	self.assertEquals(len(all_keys), 1000)
	
        se.populate()
	all_keys = r8.keys('*')
	self.assertEquals(len(all_keys), 1000)
	
        z.populate()
	all_keys = r9.keys('*')
	self.assertEquals(len(all_keys), 1000)

	r6.flushdb()
	r7.flushdb()
	r8.flushdb()
	r9.flushdb()

if __name__ == '__main__':
    """How do you feel? ...How do you feel?"""
    unittest.main()


