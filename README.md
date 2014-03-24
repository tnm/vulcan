vulcan
=======

**vulcan** generates test keys for Redis.

usage
------

vulcan is just a single C file. To use, run:

```
make
```

Running `make` in the `vulcan/` directory will produce an executable called `vulcan`.

vulcan expects you to have
[hiredis](https://github.com/redis/hiredis.git) available for linking. (You can
`brew install hiredis` on OS X, do a source install, or just use your standard
distro packaging.) vulcan also expects `pthreads`.

Usage is straight-forward:

```
./vulcan [number of keys] [string|list|set|zset] -h [host] -p [port]
```

The first argument is the number of keys you wish to generate. vulcan
restricts this only to whatever `LONG_MAX` is on your system,
although I'd advise you use fewer keys than that.

The second argument is one of `string`, `list`, `set`, or
`zset`. This is the Redis datatype you wish to generate.

The other options are not required. If you don't pass in `host` or `port`
arguments, vulcan will use defaults of `127.0.0.1` and port `6390`
(note that, for safety, that port number is not the standard
Redis port of `6379`).

vulcan uses 40 threads to speed up the key generation. On a basic laptop,
vulcan can generate and set 10,000 keys in about 600 milliseconds (for any
datatype).

vulcan will also output some timing data on `stderr` when run.

example
---------

```
$ ./vulcan 10000 zset
[vulcan] Using hostname 127.0.0.1 and port 6390
[vulcan] set 10000 zsets in 660.035000 milliseconds
```

```
$ ./vulcan 10000 string -h localhost -p 6391
[vulcan] Using hostname localhost and port 6391
[vulcan] set 10000 strings in 494.922000 milliseconds
```

license
--------

MIT

