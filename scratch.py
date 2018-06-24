from google.transit import gtfs_realtime_pb2 as gtfs_rt

from time import gmtime, strftime
import os
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
curr_dir = os.path.dirname(os.path.abspath(__file__))
feed = gtfs_rt.FeedMessage()

for name, url in zip(filenames, urls):
    try:
        response = requests.get(url)
        feed.ParseFromString(response.content)
        file_name = '%s_%s' % (name,timestamp)
        file_path = os.path.join(curr_dir, "data", name, file_name)

        with open(file_path, "w") as f:
            f.writelines(repr(feed))
    except:
        pass

