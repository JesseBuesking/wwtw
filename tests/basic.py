import unittest
import time
from datetime import datetime, timedelta
from wwtw import StopWatch, stopwatch


class BasicTests(unittest.TestCase):

    def test_initializes_empty(self):
        sw = StopWatch()
        self.assertIsNone(sw._start)
        self.assertIsNone(sw._stop)
        self.assertIsNone(sw._elapsed)

    def test_resets_empty(self):
        sw = StopWatch()
        sw.start()
        time.sleep(.001)
        sw.stop()
        sw.reset()

        self.assertIsNone(sw._start)
        self.assertIsNone(sw._stop)
        self.assertIsNone(sw._elapsed)

    def test_times_correctly(self):
        sw = StopWatch()
        sw.start()
        time.sleep(.001)
        sw.stop()

        self.assertAlmostEqual(
            timedelta(seconds=.001).total_seconds(),
            sw.elapsed.total_seconds(),
            3)
        self.assertEqual(1, sw.elapsed_ms)

    def test_pretty_seconds(self):
        sw = StopWatch()
        sw._start = datetime(2012, 01, 01, 10, 30, 01)
        sw._stop = datetime(2012, 01, 01, 10, 30, 03)
        self.assertEqual("00:00:02", sw.pretty())

    def test_pretty_one_day(self):
        sw = StopWatch()
        sw._start = datetime(2012, 01, 01, 10, 30, 01)
        sw._stop = datetime(2012, 01, 02, 10, 31, 03)
        self.assertEqual("1d 00:01:02", sw.pretty())

    def test_pretty_days(self):
        sw = StopWatch()
        sw._start = datetime(2012, 01, 01, 10, 30, 01)
        sw._stop = datetime(2012, 01, 10, 10, 31, 03)
        self.assertEqual("9d 00:01:02", sw.pretty())

    def test_pretty_subsecond(self):
        sw = StopWatch()
        sw._start = datetime(2012, 01, 01, 10, 30, 01)
        sw._stop = datetime(2012, 01, 01, 10, 30, 03, 33000)
        self.assertEqual("00:00:02.033", sw.pretty(3))


    def test_pretty_days_subsecond(self):
        sw = StopWatch()
        sw._start = datetime(2012, 01, 01, 10, 30, 01)
        sw._stop = datetime(2012, 01, 10, 10, 31, 03, 33000)
        self.assertEqual("9d 00:01:02.033", sw.pretty(3))

        sw._start = datetime(2012, 01, 01, 10, 30, 00)
        sw._stop = datetime(2012, 01, 02, 10, 30, 10, 100000)

    def test_stopwatch_name(self):
        sw = StopWatch("sw")
        self.assertEqual("sw", sw.name())

    def test_with_statement(self):
        with StopWatch() as sw:
            time.sleep(.001)

        self.assertEqual("00:00:00.001", sw.pretty(3))

    @unittest.skip("verifying that it prints")
    def test_function_decorator(self):
        @stopwatch("test_function_decorator")
        def func():
            time.sleep(.001)
        func()
