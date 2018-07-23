import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/' +'..')
from pyecharts import Graph
import data_collection_package.get_data as dg


def draw_map(AS):
    graph = Graph("AS Links Map")

    nodes = []

    maxDegree = 0

    for key in AS:
        if len(AS[key]) >= maxDegree:
            maxDegree = len(AS[key])

    for key in AS:
        singleNode = {"name": "AS" + key, "symbolSize": (len(AS[key]) + 1) / (maxDegree + 1) * 5}
        nodes.append(singleNode)

    links = []

    for i in nodes:
        key = i.get('name')[2:]
        for j in AS[key]:
            links.append({"source": i.get('name'), "target": "AS" + j})

    graph.add("AS Links Map", nodes, links, layout="cycle")
    graph.render()


def main():
    AS = dg.main()
    draw_map(AS)


main()
