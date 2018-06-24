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
import os
import errno
import requests

def create_directories(filenames):
    for filename in filenames:
        if not os.path.exists(filename):
            os.makedirs(filename)

key = 'e52f0769ccdce73f961a6332beb2033e'

urls = ["http://gtfsrt.prod.obanyc.com/vehiclePositions?key=%s" % key,
        "http://gtfsrt.prod.obanyc.com/tripUpdates?key=%s" % key,
        'http://datamine.mta.info/mta_esi.php?key=%s&feed_id=%s' % (key, 1),
        'http://datamine.mta.info/mta_esi.php?key=%s&feed_id=%s' % (key, 26),
        'http://datamine.mta.info/mta_esi.php?key=%s&feed_id=%s' % (key, 16),
        'http://datamine.mta.info/mta_esi.php?key=%s&feed_id=%s' % (key, 21),
        'http://datamine.mta.info/mta_esi.php?key=%s&feed_id=%s' % (key, 2),
        'http://datamine.mta.info/mta_esi.php?key=%s&feed_id=%s' % (key, 11),
        'http://datamine.mta.info/mta_esi.php?key=%s&feed_id=%s' % (key, 31),
        'http://datamine.mta.info/mta_esi.php?key=%s&feed_id=%s' % (key, 36),
        'http://datamine.mta.info/mta_esi.php?key=%s&feed_id=%s' % (key, 51),
        ]

filenames = ['busVehiclePosition','bustripUpdates',
             'gtfs_1','gtfs_26','gtfs_16','gtfs_21','gtfs_2','gtfs_11','gtfs_31','gtfs_36','gtfs_51']

create_directories(filenames)

timestamp = strftime("%Y-%m-%d-%H-%M-%S", gmtime())
feed = gtfs_rt.FeedMessage()

for name, url in zip(filenames, urls):
    try:
        response = requests.get(url)
        feed.ParseFromString(response.content)
        file_name = '%s_%s' % (name,timestamp)
        file_path = os.path.join(name, file_name)

        with open(file_path, "w") as f:
            f.writelines(repr(feed))
    except:
        pass


# with open(file_name, "w") as f:
#     f.writelines(repr(feed))

# for entity in feed.entity:
#   if entity.HasField('trip_update'):
#     print entity.trip_update

