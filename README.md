Vulcan
======

**The highly logical, ultra-simple way to populate Redis with data**

Perhaps you want to populate Redis with a bunch of test data? Or maybe you want to try and reproduce a bug you're facing, and need to pour in a lot of random data?

Well, you want Vulcan.

So Simple, Even a Klingon Can Do It
---------------------------------------

Vulcan is written in Python, so all you'll need is [redis-py](http://github.com/andymccurdy/redis-py "redis-py").

Put Vulcan in your PYTHONPATH and you're all set.

What It Does
---------------

Vulcan will populate your Redis datastore with test data. It works for each of the built-in Redis data structures. It uses SET for strings, LPUSH for lists, SADD for sets, and ZADD for sorted sets. 

Vulcan creates the test data on a seperate DB for each datatype: DB's 6, 7, 8, and 9, respectively.

How To Do It
-------------

Say you want to SET ten thousand keys, with randomly generated values.

Here's all you need to do:

First, create a Vulcan object like so:

	from vulcan import Vulcan

	s = Vulcan(10000)

The default is to populate with strings, but to be explicit you could do:

	s = Vulcan(10000, 'strings')

For lists, sets, or sorted sets:

	lists = Vulcan(10000, 'lists')
	sets = Vulcan(10000, 'sets')
	zsets = Vulcan(10000, 'zsets')

Now call your object like so:

	s.populate()

That will clear out database #6 and populate it with your random data. You're all set.

The keys are given random integer key names, and the values and scores are also given random integers. Next version, I'll likely add in some other options for random values (probably Star Trek-based).

That's all there is to it. You are now bursting with Redis data. Live long, and prosper. \V/_
