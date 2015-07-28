from pandas import *
import pandas as pd
import matplotlib.pyplot as plt

import sqlite3

from vbench.git import GitRepo


REPO_PATH = '/home/jbuesking/repositories/python/wwtw'
repo = GitRepo(REPO_PATH)

con = sqlite3.connect('vb_suite/benchmarks.db')


def get_results():
    results = con.execute("""
        select b.name, b.checksum, r.revision, r.timestamp, r.ncalls, r.timing
        from benchmarks as b
        inner join results as r
        on b.checksum = r.checksum
        order by b.name ASC, r.timestamp ASC;""").fetchall()
    x = pd.DataFrame(results, columns=[
        'name', 'checksum', 'revision', 'timestamp', 'ncalls', 'timing'])
    return x

x = get_results()
for name, group in x.groupby(['name']):
    group.sort(columns=['timestamp'], ascending=True, inplace=True)
    mini = group.timing.min()
    maxi = group.timing.max()
    diff = maxi - mini
    yrange = (mini - diff, maxi + diff)

    size_ratio = .8
    fig, ax = plt.subplots(figsize=(16*size_ratio, 9*size_ratio))

    group.revision = group.revision.str[:8]
    group.plot(x='revision', y='timing', ylim=yrange, ax=ax)
    plt.title(name)
    plt.ylabel('ms')
    plt.legend(loc='best')
    fig.autofmt_xdate()
    plt.show()

plt.ylabel('ms')
