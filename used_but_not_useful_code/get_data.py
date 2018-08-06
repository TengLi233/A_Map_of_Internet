from _pybgpstream import BGPStream, BGPRecord, BGPElem
from collections import defaultdict
from itertools import groupby
from datetime import datetime
import calendar


# method to catch data from MapOfInternet
# parameter is the collector and datetime
# return varible is a dictionary stored the asn and its neiborhoods in key-value format
def get_data(collector, start, end):
    stream = BGPStream()
    rec = BGPRecord()

    stream.add_filter('collector', collector)
    stream.add_filter('record-type', 'ribs')
    stream.add_interval_filter(start, end)

    stream.start()

    a_s = defaultdict(set)

    while (stream.get_next_record(rec)):
        if rec.status != "valid":
            print rec.project, rec.collector, rec.type, rec.time, rec.status
        else:
            elem = rec.get_next_elem()
            while elem:
                # the list is a list, which stores an as-path
                list = [k for k, g in groupby(elem.fields['as-path'].split(" "))]
                peer = str(elem.peer_asn)
                # divide the as path to several ASes, and find their neiborhoods
                if len(list) > 1 and list[0] == peer:
                    a_s[list[-1]].add(list[-2])
                # the code below is used to test whether the program catch the correct data
                print rec.project, rec.collector, rec.type, rec.time, rec.status
                print elem.type, elem.peer_asn, elem.peer_address, elem.fields
                elem = rec.get_next_elem()
    print len(a_s)
    return a_s


# a method to transfer a datetime to timestamp
# in python3 do not need this method
def timestamp(year, mounth, day, hour, min):
    dt = datetime(year, mounth, day, hour, min)
    return int(calendar.timegm(dt.timetuple()))


# main method to start the program
def main():
    collector = 'rrc06'
    start = timestamp(2001, 8, 30, 15, 0)
    end = timestamp(2001, 8, 30, 15, 10)
    ases = get_data(collector, start, end)
    return ases


if __name__ == '__main__':
    main()