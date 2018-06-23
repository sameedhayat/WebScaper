from google.transit import gtfs_realtime_pb2 as gtfs_rt
# import wget
# from datetime import datetime, timedelta
from time import gmtime, strftime
# def daterange(start_date, end_date):
#     start_date = datetime.strptime(start_date, '%Y-%m-%d')
#     end_date = datetime.strptime(end_date, '%Y-%m-%d')
#     for n in range(int ((end_date - start_date).days)+1):
#         strg = '{:%Y-%m-%d}'.format(start_date + timedelta(n))
#         yield strg
#
# start_date = '2018-06-16'
# # finish_date = '2018-06-17'
# # for r in daterange(start_date, finish_date):
# #     url = "https://datamine-%s.s3.amazonaws.com/gtfs.tgz" % r
# #     filename = wget.download(url, 'gtfs_%s.tgz' % r)
# key = 'e52f0769ccdce73f961a6332beb2033e'
# url = "https://datamine-%s.s3.amazonaws.com/gtfs.tgz" % start_date
# print 'gtfs_%s.tgz' % strftime("%Y-%m-%d-%H-%M-%S", gmtime())
# filename = wget.download(url, 'gtfs_%s.tgz' % strftime("%Y-%m-%d-%H-%M-%S", gmtime()))

import requests
key = 'e52f0769ccdce73f961a6332beb2033e'
url='http://datamine.mta.info/mta_esi.php?key=%s&feed_id=%s' % (key, 1)
feed = gtfs_rt.FeedMessage()
response = requests.get(url)
feed.ParseFromString(response.content)
file_name = 'gtfs_%s' % strftime("%Y-%m-%d-%H-%M-%S", gmtime())
print feed
with open(file_name, "w") as f:
    f.writelines(repr(feed))

# for entity in feed.entity:
#   if entity.HasField('trip_update'):
#     print entity.trip_update

