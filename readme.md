wibbly wobbly timey wimey
=========================

A simple stopwatch with nice string formatting for python.

examples
--------

```
>>> import time
>>> from wwtw import StopWatch, stopwatch
>>> sw = StopWatch()
>>> sw.start()
>>> time.sleep(1.1)
>>> sw.stop()
>>> print(sw.pretty())
00:00:01
```

There's also the option of using the stopwatch in a ``with`` statement ...

```
>>> with StopWatch() as sw:
...     time.sleep(1.1)
...
>>> print(sw.pretty())
00:00:01
```

... or as a function decorator

```
>>> @stopwatch() # notice the decorator is all lowercase
... def myfunc():
...     time.sleep(1.1)
...
>>> myfunc()
00:00:01
```

You can pass an integer to output the format in a higher precision. For example:

```
>>> print(sw.pretty(3))
00:00:01.100
```

If the stopwatch runs for more than a day, the output will start with ``Nd``,
where ``N`` is the number of days:

```
>>> sw.restart()
>>> time.sleep(86411.1)
>>> sw.stop()
>>> print(sw.pretty(3))
1d 00:00:11.100
```

Of course you can get access to the raw ``timedelta`` object from a
``StopWatch`` instance:

```
>>> sw.restart()
>>> time.sleep(1.1)
>>> sw.stop()
>>> sw.elapsed
datetime.timedelta(0, 1, 100000)
```
