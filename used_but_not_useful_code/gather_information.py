import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/' +'..')
from _pybgpstream import BGPStream, BGPRecord, BGPElem
from itertools import groupby
from datetime import datetime
import matplotlib.pyplot as plt
import networkx as nx
import calendar



# method to catch data from MapOfInternet
# parameter is the collector and datetime
# return varible is a dictionary stored the asn and its neiborhoods in key-value format
def get_data(collector, start, end):
    stream = BGPStream()
    rec = BGPRecord()

    stream.add_filter('collector', collector)
    stream.add_filter('record-type', 'ribs')
    stream.add_interval_filter(start,end)

    stream.start()

    as_Graph = nx.Graph()

    while (stream.get_next_record(rec)):
        if rec.status != "valid":
            print rec.project, rec.collector, rec.type, rec.time, rec.status
        else:
            elem = rec.get_next_elem()
            while (elem):
                if as_Graph.number_of_edges() > 10000:
                    break
                # the list is a list, which stores an as-path
                list = [k for k , g in groupby(elem.fields['as-path'].split(" "))]
                peer = str(elem.peer_asn)
                # judge whether the as-path is legal
                if len(list) > 1 and list[0] == peer:
                    # add edges to the graph
                    for i in range(0, len(list) - 1):
                        as_Graph.add_edge(list[i], list[i + 1])
                # the code below is used to test whether the program catch the correct data
                # print rec.project, rec.collector, rec.type, rec.time, rec.status
                # print elem.type,elem.fields['as-path']
                elem = rec.get_next_elem()

    nx.draw(as_Graph)
    plt.savefig("map.png")

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
    get_data(collector,start,end)
main()