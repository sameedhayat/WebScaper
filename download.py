from google.transit import gtfs_realtime_pb2 as gtfs_rt
import wget
from datetime import datetime, timedelta
from time import gmtime, strftime
import tarfile
def daterange(start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    for n in range(int ((end_date - start_date).days)+1):
        strg = '{:%Y-%m-%d}'.format(start_date + timedelta(n))
        yield strg


start_date = '2014-10-01'
finish_date = '2014-10-07'
for r in daterange(start_date, finish_date):
    url = "https://datamine-%s.s3.amazonaws.com/gtfs.tgz" % r
    filename = wget.download(url, 'gtfs_subway%s.tgz' % r)