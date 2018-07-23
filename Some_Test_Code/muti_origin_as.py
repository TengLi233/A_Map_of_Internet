from _pybgpstream import BGPStream, BGPRecord, BGPElem
from collections import defaultdict

stream = BGPStream()
rec = BGPRecord()

stream.add_filter('collector', 'route-views.sg')
stream.add_filter('record-type', 'ribs')
stream.add_interval_filter(1438415400, 1438416600)

stream.start()

prefix_origin = defaultdict(set)



while(stream.get_next_record(rec)):
    elem = rec.get_next_elem()
    while(elem):
        pfx = elem.fields['prefix']
        ases = elem.fields['as-path'].split(" ")
        if len(ases) > 0:
            origin = ases[-1]
            prefix_origin[pfx].add(origin)
        elem = rec.get_next_elem()



for pfx in prefix_origin:
    if len(prefix_origin) > 1:
        print pfx, ",".join(prefix_origin[pfx])

