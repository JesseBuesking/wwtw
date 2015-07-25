wibbly wobbly timey wimey
=========================

A simple stopwatch with nice string formatting for python.

examples
--------

```
>>> import time
>>> from wwtw import StopWatch
>>> sw = StopWatch()
>>> sw.start()
>>> time.sleep(1.1)
>>> sw.stop()
>>> print(sw.pretty())
00:00:01
```

You can pass an integer to output the format in a higher precision. For example:

```
>>> print(sw.pretty(3))
00:00:01.100
```

If the stopwatch runs for more than a day, the output will look similar to the
following:

```
>>> sw.reset()
>>> sw.start()
>>> time.sleep(86411.1)
>>> sw.stop()
>>> print(sw.pretty(3))
1d 00:00:11.100
```

Of course you can get access to the raw ``timedelta`` object:

```
>>> sw.reset()
>>> sw.start()
>>> time.sleep(1.1)
>>> sw.stop()
>>> sw.elapsed()
datetime.timedelta(0, 1, 100000)
```
