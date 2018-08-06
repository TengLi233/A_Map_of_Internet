from _pybgpstream import BGPStream, BGPRecord
from collections import defaultdict
from itertools import groupby
from datetime import datetime
import networkx as nx
import IP2Location
import calendar
import re


class DataCollector(object):

    mode = ""
    as_prefix = defaultdict(set)

    def __init__(self, start, end, mode):
        self.start = start
        self.end = end
        self.mode = mode

        if mode == "IPv4":
            self.pattern = "(((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))\.){3}((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))"
        elif mode == "IPv6":
            self.pattern = "([\w]*[:])+([\w]*)"

    # method to catch data from BGPStream
    def get_data_graph(self):

        stream = BGPStream()
        rec = BGPRecord()
        stream.add_filter('record-type', 'ribs')
        stream.add_interval_filter(self.start, self.end)
        stream.start()

        as_graph = nx.Graph()

        while stream.get_next_record(rec):
            if rec.status == "valid":
                elem = rec.get_next_elem()
                while elem:
                    # the list is a list, which stores an as-path
                    as_path = [k for k, g in groupby(elem.fields['as-path'].split(" "))]
                    peer = str(elem.peer_asn)
                    # judge whether the as-path is legal
                    if len(as_path) > 1 and as_path[0] == peer:
                        if re.match(self.pattern, elem.fields['prefix']):
                            self.as_prefix[as_path[-1]].add(elem.fields['prefix'])
                            # add edges to the graph
                            for i in range(0, len(as_path) - 1):
                                as_graph.add_edge(as_path[i], as_path[i + 1])
                    elem = rec.get_next_elem()

        as_graph = self.add_geo_loc(as_graph)

        return as_graph

    def add_geo_loc(self, as_graph):
        as_prefix = self.as_prefix
        # use IP2Location database to get the link between AS and longtitude
        ip2_loc_obj = IP2Location.IP2Location()

        if self.mode == "IPv4":
            ip2_loc_obj.open("../IP2LocationDBs/IP2LOCATION-LITE-DB5.BIN")
        elif self.mode == "IPv6":
            ip2_loc_obj.open("../IP2LocationDBs/IP2LOCATION-LITE-DB5.IPV6.BIN")

        for key in as_prefix:
            # calculate the average longtitude of a set of prefixes for one asn
            sum_longtitude = 0.0
            for elem in as_prefix[key]:
                ip_adress = elem.split('/')
                try:
                    rec = ip2_loc_obj.get_all(ip_adress[0])
                except ValueError:
                    continue
                sum_longtitude += rec.longitude
            # set the longtitude as a attribute of the node in graph
            if len(as_prefix[key]) > 0:
                as_graph.add_node(key, longtitude=sum_longtitude / len(as_prefix[key]))
        return as_graph

    def get_as_prefix(self):
        return self.as_prefix


def timestamp(year, month, day, hour, mines):
    dt = datetime(year, month, day, hour, mines)
    return int(calendar.timegm(dt.timetuple()))


def main():
    start = timestamp(2004, 8, 30, 0, 0)
    end = timestamp(2004, 8, 30, 1, 0)
    collector = DataCollector(start, end, "IPv6")
    as_graph = collector.get_data_graph()
    as_prefix = collector.get_as_prefix()
    with open("../Autonomous_System_File/AsPrefixes_2004_IPv6.csv", 'w') as f:
        for key in as_prefix:
            f.writelines(str(key) + "\t" + str(as_prefix[key]) + "\n")
    return as_graph


if __name__ == '__main__':
    main()
