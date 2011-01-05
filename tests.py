import unittest
import vulcan
import redis

r5 = redis.Redis(host='localhost', port=6379, db=5)
r6 = redis.Redis(host='localhost', port=6379, db=6)
r7 = redis.Redis(host='localhost', port=6379, db=7)
r8 = redis.Redis(host='localhost', port=6379, db=8)
r9 = redis.Redis(host='localhost', port=6379, db=9)

class TestVulcan(unittest.TestCase):
    """What is Kiri-kin-tha's first law of metaphysics?"""

    def setUp(self):
        """Adjust the sine wave of this magnetic envelope so that anti-neutrons can 
        pass through it but anti-gravitons cannot."""
        r5.flushdb()
        r6.flushdb()
        r7.flushdb()
        r8.flushdb()
        r9.flushdb()

        self.strings = vulcan.Vulcan(1000, 'strings')
        self.lists = vulcan.Vulcan(1000, 'lists')
        self.sets = vulcan.Vulcan(1000, 'sets')
        self.zsets = vulcan.Vulcan(1000, 'zsets')
        self.hashes = vulcan.Vulcan(1000, 'hashes')

    def test_populate(self):
        """What is the electronic configuration of gadolinium?"""
        strings = self.strings
        lists = self.lists
        sets = self.sets
        zsets = self.zsets
        hashes = self.hashes

        strings.populate()
        all_keys = r5.keys('*')
        self.assertEquals(len(all_keys), 1000)
	
        lists.populate()
        all_keys = r6.keys('*')
        self.assertEquals(len(all_keys), 1000)
	
        sets.populate()
        all_keys = r7.keys('*')
        self.assertEquals(len(all_keys), 1000)
	
        zsets.populate()
        all_keys = r8.keys('*')
        self.assertEquals(len(all_keys), 1000)

        hashes.populate()
        all_keys = r9.keys('*')
        self.assertEquals(len(all_keys), 1000)

        r5.flushdb()
        r6.flushdb()
        r7.flushdb()
        r8.flushdb()
        r9.flushdb()

if __name__ == '__main__':
    """How do you feel? ...How do you feel?"""
    unittest.main()


