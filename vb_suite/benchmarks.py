from vbench.benchmark import Benchmark
from vbench.db import BenchmarkDB
from vbench.runner import BenchmarkRunner
from vbench.git import GitRepo
from datetime import datetime


common_setup = """
import time
from wwtw import StopWatch, stopwatch
"""


setup = common_setup + """
sw = StopWatch()
"""

bm_starting = Benchmark("sw.start()", setup, name='StopWatch.start')

setup = common_setup + """
sw = StopWatch()
sw.start()
"""

bm_stopping = Benchmark("sw.stop()", setup, name='StopWatch.stop')

setup = common_setup + """
sw = StopWatch()
sw.start()
time.sleep(.01)
sw.stop()
"""

bm_pretty = Benchmark("sw.pretty()", setup, name='StopWatch.pretty')

bm_pretty_precise = Benchmark("sw.pretty(3)", setup, name='StopWatch.pretty(3)')

#----------------------------------------------------------------------
# Actually running the benchmarks

benchmarks = [v for v in locals().values() if isinstance(v, Benchmark)]

REPO_PATH = '/home/jbuesking/repositories/python/wwtw'
REPO_URL = 'git@github.com:JesseBuesking/wwtw.git'
DB_PATH = '/home/jbuesking/repositories/python/wwtw/vb_suite/benchmarks.db'
TMP_DIR = '/home/jbuesking/tmp/vb_wwtw'
PREPARE = """
python setup.py clean
"""
BUILD = """
python setup.py build_ext --inplace
"""
START_DATE = datetime(2015, 7, 20)

repo = GitRepo(REPO_PATH)

to_consider = repo.shas.truncate(START_DATE)

runner = BenchmarkRunner(benchmarks, REPO_PATH, REPO_URL,
                         BUILD, DB_PATH, TMP_DIR, PREPARE,
                         run_option='eod', start_date=START_DATE)

runner.run()
