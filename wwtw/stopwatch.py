from datetime import datetime


class StopWatch(object):

    def __init__(self, name=None):
        self._name = name
        self._start = None
        self._stop = None
        self._elapsed = None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()

    def name(self):
        return self._name

    def start(self):
        self._start = datetime.utcnow()

    def stop(self):
        self._stop = datetime.utcnow()

    def elapsed(self):
        if self._elapsed is None and self._stop is not None:
            self._elapsed = self._stop - self._start
        elif self._elapsed is None and self._stop is None:
            # just get the time up to now
            return datetime.utcnow() - self._start

        return self._elapsed

    def reset(self):
        self._start = None
        self._stop = None
        self._elapsed = None

    def pretty(self, precision=0):
        assert precision >= 0, "expecting precision >= 0"
        if self.elapsed() is None:
            if self._name is None:
                return 'n/a'
            else:
                return '{}: n/a'.format(self._name)
        seconds = int(self.elapsed().total_seconds())
        days = int(seconds / 86400)
        if days > 0:
            seconds = seconds - (days * 86400)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)

        if precision == 0:
            hms = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
        else:
            fmt = '{{:.{precision}f}}'.format(
                precision='{:02d}'.format(precision))

            hms = "{:02d}:{:02d}:{:02d}{}".format(
                hours,
                minutes,
                seconds,
                fmt.format(self.elapsed().microseconds / 1000000.).lstrip('0'))

        if days > 0:
            hms = "{}d {}".format(days, hms)

        if self._name is not None:
            hms = "{}: {}".format(self._name, hms)

        return hms


def stopwatch(name=None, precision=0):
    def decorator(func):
        def func_wrapper(*args, **kwargs):
            with StopWatch(name) as sw:
                func(*args, **kwargs)
            print(sw.pretty(precision))
        return func_wrapper
    return decorator
