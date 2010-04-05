#!/usr/bin/env python

import os

from setuptools import setup, find_packages

version = '0.1.1'


LONG_DESCRIPTION = '''

Quick Setup and Usage
---------------------

You'll need redis-py: http://github.com/andymccurdy/redis-py 

Say you want to SET ten thousand keys, with randomly generated values.

Here's all you need to do:

First, create a Vulcan object like so:

	from vulcan import Vulcan

	s = Vulcan(10000)

The default is to populate with strings, but to be explicit you could do:

	s = Vulcan(10000, 'strings')

For lists, sets, sorted sets, or hashes:

	lists = Vulcan(10000, 'lists')
	sets = Vulcan(10000, 'sets')
	zsets = Vulcan(10000, 'zsets')
        hashses = Vulcan(10000, 'hashes')

Now just:

	s.populate()

That will clear out database 5 (or 6 or 7 or 8 or 9, respectively), and populate it with your random data. You're all set.

The keys are given random integer key names, and the values and scores are also given random integers. Next version, I'll likely add in some other options for random values (probably Star Trek-based).

That's all there is to it. You are now bursting with Redis data. Live long, and prosper. \V/_


'''


setup(
    name='vulcan',
    version=version,
    description='The highly logical way to populate Redis with random data',
    long_description=LONG_DESCRIPTION,
    url='http://github.com/tnm/vulcan',
    author='Ted Nyman',
    author_email='tnm800@gmail.com',
    keywords='Redis, random, data, data structures',
    license='MIT',
    packages=find_packages(),
    py_modules=['vulcan'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
	'Programming Language :: Python',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
   ],
)
