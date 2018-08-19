import plotly.graph_objs as go
import plotly
import math


plotly.tools.set_credentials_file(username='ltknow', api_key='Lg7qlfduhEolzJYMyEdk')


class MapDrawer(object):
    def __init__(self, as_graph):
        self.as_graph = as_graph

    def draw_map(self, filename):

        colorscale = [[0.0, 'rgb(254,224,144)'], [0.1111111111111111, 'rgb(253,174,97)'],
                      [0.2222222222222222, 'rgb(244,109,67)'], [0.3333333333333333, 'rgb(215,48,39)'],
                      [0.4444444444444444, 'rgb(165,0,38)'], [0.5555555555555556, 'rgb(49,54,149)'],
                      [0.6666666666666666, 'rgb(69,117,180)'], [0.7777777777777778, 'rgb(116,173,209)'],
                      [0.8888888888888888, 'rgb(171,217,233)'], [1.0, 'rgb(171,217,233)']]

        # use the two lists to store the radius and angle of every node
        r = list()
        sizes = list()
        theta = list()
        data = list()
        # get the max degree of the graph
        max_degree = 1
        max_radius = 0

        for node in self.as_graph:
            if int(self.as_graph.degree(node)) > max_degree:
                max_degree = int(self.as_graph.degree(node))
        # add radius and angle to the node
        for node in self.as_graph.nodes:

            if self.as_graph.degree(node) <= 0:
                radius = 1 - math.log(1.0 / max_degree)
            else:
                radius = 1 - math.log(float(self.as_graph.degree(node)) / max_degree)

            if radius > max_radius:
                max_radius = radius

            area = 10 * float(self.as_graph.degree(node) + max_degree) / (max_degree * 2)
            try:
                angle = self.as_graph.node[node]['longtitude']
            except KeyError:
                continue

            r.append(radius)
            sizes.append(area)
            theta.append(angle)

            self.as_graph.add_node(node, pos=(radius, angle), degree=self.as_graph.degree(node))

        node = go.Scatterpolar(
            r=r,
            theta=theta,
            mode='markers',
            marker=dict(
                symbol='square',
                size=sizes,
                cmax=0,
                color=r,  # set color equal to the radius
                colorscale=colorscale,
                showscale=True
            )
        )

        edge_r1 = list()
        edge_theta1 = list()

        edge_r2 = list()
        edge_theta2 = list()

        edge_r3 = list()
        edge_theta3 = list()

        for edge in self.as_graph.edges:
            try:
                r0, t0 = self.as_graph.node[edge[0]]['pos']
                r1, t1 = self.as_graph.node[edge[1]]['pos']

                radius = max(r0, r1)

                flag = radius/max_radius

                if flag <= 0.4:
                    edge_r3 += [r0, r1, None]
                    edge_theta3 += [t0, t1, None]
                elif flag <= 0.7:
                    edge_r2 += [r0, r1, None]
                    edge_theta2 += [t0, t1, None]
                else:
                    edge_r1 += [r0, r1, None]
                    edge_theta1 += [t0, t1, None]

            except KeyError:
                continue

        edge1 = go.Scatterpolar(
            r=edge_r1,
            theta=edge_theta1,
            line=dict(
                width=0.5,
                color='rgba(171,217,233,0.1)',
            ),
            mode='lines'
        )

        data.append(edge1)
        edge2 = go.Scatterpolar(
            r=edge_r2,
            theta=edge_theta2,
            line=dict(
                width=1,
                color='rgba(49,54,149,0.2)',
            ),
            mode='lines'
        )
        data.append(edge2)
        edge3 = go.Scatterpolar(
            r=edge_r3,
            theta=edge_theta3,
            line=dict(
                width=2,
                color='rgba(215,48,39,0.5)',
            ),
            mode='lines'
        )
        data.append(edge3)

        data.append(node)

        fig = go.Figure(data=data)

        plotly.offline.plot(fig, filename=filename + '.html', auto_open=True)
