import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/' + '..')

from _pybgpstream import BGPStream, BGPRecord, BGPElem
from collections import defaultdict
from itertools import groupby
from datetime import datetime
import networkx as nx
import IP2Location
import calendar


class Data_Collector(object):

    def __init__(self,collector, start, end):
        self.collector = collector
        self.start = start
        self.end = end


    # method to catch data from BGPStream
    # return varible is a dictionary stored the asn and its neiborhoods in key-value format
    def get_data_graph(self):
        stream = BGPStream()
        rec = BGPRecord()

        stream.add_filter('collector', self.collector)
        stream.add_filter('record-type', 'ribs')
        stream.add_interval_filter(self.start, self.end)

        stream.start()

        as_Graph = nx.Graph()

        while (stream.get_next_record(rec)):
            if rec.status != "valid":
                print rec.project, rec.collector, rec.type, rec.time, rec.status
            else:
                elem = rec.get_next_elem()
                while (elem):
                    # the list is a list, which stores an as-path
                    list = [k for k, g in groupby(elem.fields['as-path'].split(" "))]
                    peer = str(elem.peer_asn)
                    # judge whether the as-path is legal
                    if len(list) > 1 and list[0] == peer:
                        # add edges to the graph
                        for i in range(0, len(list) - 1):
                            as_Graph.add_edge(list[i], list[i + 1])
                    elem = rec.get_next_elem()
         # add longtitude information to the graph
        as_Graph = self.add_geo_infor(as_Graph)
        return as_Graph


    def add_geo_infor(self, as_graph):
        # use IP2Location database to get the link between AS and longtitude
        IP2LocObj = IP2Location.IP2Location()
        IP2LocObj.open("../IP2LocationDBs/IP2LOCATION-LITE-DB5.BIN")
        # use a dict to store the asn and its prefixes
        as_prefix = defaultdict(set)

        with open('../IPv4_IPv6_ASN/IP2LOCATION-LITE-ASN.CSV') as f:
            for lines in f:
                # split one line data to different parts
                aslist = lines.split(",")
                #get the asn and its prefix
                prefix = aslist[2][1:-1]
                asn = aslist[3][1:-1]

                if as_graph.has_node(asn):
                    as_prefix[asn].add(prefix)

        for key in as_prefix:
            # calculate the average longtitude of a set of prefixes for one asn
            sum_longtitude = 0.0
            for elem in as_prefix[key]:
                ip_adress = elem.split('/')
                rec = IP2LocObj.get_all(ip_adress[0])
                sum_longtitude += rec.longitude
            # set the longtitude as a attribute of the node in graph
            as_graph.add_node(key, longtitude=sum_longtitude / len(as_prefix[key]))
        return as_graph


def timestamp(year, mounth, day, hour, min):
    dt = datetime(year, mounth, day, hour, min)
    return int(calendar.timegm(dt.timetuple()))

def main():
    start = timestamp(2001, 8, 30, 15, 0)
    end = timestamp(2001, 8, 30, 15, 10)
    collector = Data_Collector('rrc06', start, end)
    as_graph = collector.get_data_graph()
    for node in as_graph:
        print(node, as_graph.nodes[node], as_graph.degree(node))

if __name__ == '__main__':
    main()


