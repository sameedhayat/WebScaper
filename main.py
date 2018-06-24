from google.transit import gtfs_realtime_pb2 as gtfs_rt

f = open('gtfs-rt.pb', 'rb')
raw_str = f.read()

msg = gtfs_rt.FeedMessage()
msg.ParseFromString(raw_str)

print msg