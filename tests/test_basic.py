from datetime import datetime
from datetime import timedelta
import time
from wwtw import StopWatch
from wwtw import stopwatch


def test_initializes_empty():
    sw = StopWatch()
    assert sw._start is None
    assert sw._stop is None
    assert sw._elapsed is None


def test_resets_empty():
    sw = StopWatch()
    sw.start()
    time.sleep(.001)
    sw.stop()
    sw.reset()

    assert sw._start is None
    assert sw._stop is None
    assert sw._elapsed is None


def test_restart():
    sw = StopWatch()
    sw.start()
    time.sleep(.001)
    sw.stop()
    sw.restart()

    assert sw._start is not None
    assert sw._stop is None
    assert sw._elapsed is None


def test_times_correctly():
    sw = StopWatch()
    sw.start()
    time.sleep(.001)
    sw.stop()

    tol = 0.001
    diff = timedelta(seconds=.001).total_seconds() - sw.elapsed.total_seconds()

    assert abs(diff) < tol
    assert 1 == sw.elapsed_ms


def test_pretty_seconds():
    sw = StopWatch()
    sw._start = datetime(2012, 1, 1, 10, 30, 1)
    sw._stop = datetime(2012, 1, 1, 10, 30, 3)
    assert "00:00:02" == sw.pretty()


def test_pretty_one_day():
    sw = StopWatch()
    sw._start = datetime(2012, 1, 1, 10, 30, 1)
    sw._stop = datetime(2012, 1, 2, 10, 31, 3)
    assert "1d 00:01:02" == sw.pretty()


def test_pretty_days():
    sw = StopWatch()
    sw._start = datetime(2012, 1, 1, 10, 30, 1)
    sw._stop = datetime(2012, 1, 10, 10, 31, 3)
    assert "9d 00:01:02" == sw.pretty()


def test_pretty_subsecond():
    sw = StopWatch()
    sw._start = datetime(2012, 1, 1, 10, 30, 1)
    sw._stop = datetime(2012, 1, 1, 10, 30, 3, 33000)
    assert "00:00:02.033" == sw.pretty(3)


def test_pretty_days_subsecond():
    sw = StopWatch()
    sw._start = datetime(2012, 1, 1, 10, 30, 1)
    sw._stop = datetime(2012, 1, 10, 10, 31, 3, 33000)
    assert "9d 00:01:02.033" == sw.pretty(3)


def test_stopwatch_name():
    sw = StopWatch("sw")
    assert "sw" == sw.name()


def test_with_statement():
    with StopWatch() as sw:
        time.sleep(.001)

    assert "00:00:00.001" == sw.pretty(3)


def test_function_decorator(capsys):
    # out == None defaults to sys.stdout/print
    @stopwatch("test_function_decorator", precision=3, out=None)
    def func():
        time.sleep(.001)
    func()
    out, err = capsys.readouterr()
    assert "test_function_decorator: 00:00:00.001\n" == out
    assert "" == err
