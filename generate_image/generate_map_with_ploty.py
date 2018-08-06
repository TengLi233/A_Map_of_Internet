from datetime import datetime
import plotly.graph_objs as go
import plotly
import calendar
import plotly
import math
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/' + '..')
import data_collection_package.data_collector as dc


plotly.tools.set_credentials_file(username='ltknow', api_key = 'Lg7qlfduhEolzJYMyEdk')


def timestamp(year, mounth, day, hour, min):
    dt = datetime(year, mounth, day, hour, min)
    return int(calendar.timegm(dt.timetuple()))


def draw_map(as_graph):
    # use the two lists to store the radius and angle of every node
    r = list()
    sizes = list()
    theta = list()

    # get the max degree of the graph
    max_degree = 1
    for node in as_graph:
        if int(as_graph.degree(node)) > max_degree:
            max_degree = int(as_graph.degree(node))

    # add radius and angle to the node
    for node in as_graph.nodes:

        radius = 1 - math.log(float(as_graph.degree(node))/max_degree)
        area = float(as_graph.degree(node) + 1)/(max_degree + 1)
        try:
            angle = as_graph.node[node]['longtitude']
        except(KeyError):
            continue

        r.append(radius)
        sizes.append(area)
        theta.append(angle)

        as_graph.add_node(node, pos = (radius, angle), degree = as_graph.degree(node))

    node = go.Scatterpolar(
        r=r,
        theta=theta,
        mode='markers',
        marker=dict(
            symbol = 'square',
            size=sizes,
            cmax=0,
            color=map(lambda x : x * -1, r),  # set color equal to a variable
            colorscale='RdBu',
            showscale=True
        )
    )

    edge_r = list()
    edge_theta = list()
    edge_color = list()

    for edge in as_graph.edges:
        try:
            r0, t0 = as_graph.node[edge[0]]['pos']
            degree0 = as_graph.node[edge[0]]['degree']
            r1, t1 = as_graph.node[edge[1]]['pos']
            degree1 = as_graph.node[edge[1]]['degree']

            edge_color.append(min(degree0,degree1))
            edge_r += [r0, r1, None]
            edge_theta += [t0, t1, None]
        except(KeyError):
            continue

    edges = go.Scatterpolar(
        r=edge_r,
        theta=edge_theta,
        line=dict(
            width=0.05,
            color='#e94392',
        ),
        mode='lines'
    )

    data = [node, edges]

    fig = go.Figure(data=data)
    plotly.offline.plot(fig, filename='AS_MAP_2001.html', auto_open=True)


def main():
    start = timestamp(2001, 8, 30, 15, 0)
    end = timestamp(2001, 8, 30, 15, 10)
    collector = dc.DataCollector(start, end, "IPv4")

    as_graph = collector.get_data_graph()

    draw_map(as_graph)


if __name__ == '__main__':
    main()
