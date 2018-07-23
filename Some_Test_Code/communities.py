from _pybgpstream import BGPStream, BGPRecord, BGPElem
from collections import defaultdict

stream = BGPStream()
rec = BGPRecord()

stream.add_filter("collector", "rrc06")
stream.add_filter("record-type", "ribs")
stream.add_filter("peer-asn", "25152")
stream.add_filter('prefix', "185.84.166.0/23")
stream.add_filter("community", "*:3400")

stream.add_interval_filter(1438415400, 1438416600)

stream.start()

community_prefix = defaultdict(set)

while(stream.get_next_record(rec)):
    elem = rec.get_next_elem()
    while (elem):
        pfx = elem.fields['prefix']
        communities = elem.fields['communities']
        for c in communities:
            ct = str(c["asn"]) + ":" + str(c["value"])
            community_prefix[ct].add(pfx)
        elem = rec.get_next_elem()

for ct in community_prefix:
    print "Community:", ct, "==>", ",".join(community_prefix[ct])

