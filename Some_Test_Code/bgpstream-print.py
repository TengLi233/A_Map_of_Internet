from _pybgpstream import BGPStream, BGPRecord, BGPElem

stream = BGPStream()
rec = BGPRecord()

collector = input("Please enter the date provider you want to collect data: ")
start = input("Please enter the time you want to start(YY/MM/DD): ")
end = input("Please enter the end time(YY/MM/DD): ")

stream.add_filter('collector', collector)
stream.add_filter('record-type', 'ribs')
#type: project, collerctor, record-type, peer-asn, prefix
stream.add_interval_filter(1438415400,1438416600)

stream.start()

while(stream.get_next_record(rec)):
    if rec.status != "valid":
        print rec.project, rec.collector, rec.type, rec.time, rec.status
    else:
        elem = rec.get_next_elem()
        while(elem):
            print rec.project, rec.collector, rec.type, rec.time, rec.status
            print elem.type, elem.peer_address, elem.peer_asn, elem.fields
            elem = rec.get_next_elem()


