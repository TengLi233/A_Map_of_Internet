import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/' + '..')
import data_collection_package.data_collector as dc
import matplotlib.pyplot as plt
from datetime import datetime
import calendar
import generate_image.draw_network_map as gm
import math
import networkx as nx


# def timestamp(year, mounth, day, hour, min):
#     dt = datetime(year, mounth, day, hour, min)
#     return int(calendar.timegm(dt.timetuple()))
#
# start = timestamp(2001, 8, 30, 15, 0)
# end = timestamp(2001, 8, 30, 15, 10)
# collector = dc.Data_Collector('rrc06', start, end)
# as_graph = collector.get_data_graph()

as_graph = nx.Graph()

as_graph.add_node(1)
as_graph.add_node(2)
as_graph.add_node(3)
as_graph.add_node(4)



print(as_graph.nodes)

edges = [(1, 2), (2, 3), (3, 4)]
as_graph.add_edges_from(edges)
as_graph.add_node(1, longtitude = 23.1234)
as_graph.add_node(2, longtitude = 12.31234)
as_graph.add_node(3, longtitude = -88.1234)
as_graph.add_node(4, longtitude = 140.1234)

r = list()
theta = list()
colors = list()
size = list()

#get the max degree of the graph
max_degree = 1
for node in as_graph:
    if int(as_graph.degree(node)) > max_degree:
        max_degree = int(as_graph.degree(node))

# add radius and angle to the node
for node in as_graph.nodes:
    try:
        radius = 1 - math.log(float(as_graph.degree(node)) / max_degree)
        angle = as_graph.node[node]['longtitude']

        r.append(radius)
        theta.append(angle)
        size.append(((as_graph.degree(node) + 1)/(max_degree + 1)) * 20)
        as_graph.add_node(node, pos=(radius, angle))
    except(KeyError):
        continue


fig = plt.figure()

ax = fig.add_subplot(111, projection='polar')

print theta

c = ax.scatter(theta, r, c='black', s=12)

plt.show()