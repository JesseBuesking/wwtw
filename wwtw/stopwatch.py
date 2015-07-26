from datetime import datetime


class StopWatch(object):

    def __init__(self):
        self._start = None
        self._stop = None
        self._elapsed = None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()

    def start(self):
        self._start = datetime.utcnow()

    def stop(self):
        self._stop = datetime.utcnow()

    def elapsed(self):
        if self._elapsed is None:
            self._elapsed = self._stop - self._start

        return self._elapsed

    def reset(self):
        self._start = None
        self._stop = None
        self._elapsed = None

    def pretty(self, precision=0):
        assert precision >= 0, "expecting precision >= 0"
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

        return hms
