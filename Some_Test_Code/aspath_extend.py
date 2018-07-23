from _pybgpstream import BGPStream, BGPRecord, BGPElem
from collections import defaultdict
from itertools import groupby
import networkx as nx

stream = BGPStream()
rec = BGPRecord()

as_graph = nx.Graph()

bgp_lens = defaultdict(lambda: defaultdict(lambda: None))

stream.add_filter('collector', 'rrc00')
stream.add_filter('record-type', 'ribs')

stream.add_interval_filter(1438415400, 1438416600)

stream.start()

while(stream.get_next_record(rec)):
    elem = rec.get_next_elem()
    while(elem):
        peer = str(elem.peer_asn)
        hops = [k for k, g in groupby(elem.fields['as-path'].split(" "))]

        if len(hops) > 1 and hops[0] == peer:
            origin = hops[-1]
            for i in range(0, len(hops) - 1):
                as_graph.add_edge(hops[i], hops[i + 1])

            bgp_lens[peer][origin] = min(filter(bool, [bgp_lens[peer][origin], len(hops)]))

        elem = rec.get_next_elem()


for peer in bgp_lens:
    for origin in bgp_lens[peer]:
        nxlen = len(nx.shortest_path(as_graph, peer, origin))
        print peer, origin, bgp_lens[peer][origin], nxlen



