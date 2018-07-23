import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/' +'..')
from _pybgpstream import BGPStream, BGPRecord, BGPElem
from objects_package import autonomous_system
from collections import defaultdict
from datetime import datetime
from itertools import groupby
import networkx as nx
import calendar


class Data_Collector(object):

    def __init__(self,collector, start, end):
        self.collector = collector
        self.start = start
        self.end = end
    # method to catch data from MapOfInternet
    # parameter is the collector and datetime
    # return varible is a dictionary stored the asn and its neiborhoods in key-value format
    def get_data_dict(self):
        stream = BGPStream()
        rec = BGPRecord()

        stream.add_filter('collector', self.collector)
        stream.add_filter('record-type', 'ribs')
        stream.add_interval_filter(self.start, self.end)

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
                    # print rec.project, rec.collector, rec.type, rec.time, rec.status
                    # print elem.type,elem.fields['as-path']
                    elem = rec.get_next_elem()
        return a_s

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
                            as_Graph.add_edge(autonomous_system.AS(list[i]), autonomous_system.AS(list[i + 1]))
                    elem = rec.get_next_elem()
        return as_Graph