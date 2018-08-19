import plotly
import plotly.graph_objs as go


def draw_bar_graph():
    trace0 = go.Bar(
        x=['-2', '-1', '0','1','2','3'],
        y=[20, 14, 23,12,43,55],
        marker=dict(
            color='rgb(158,202,225)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5,
            )
        ),
        opacity=1
    )

    data = [trace0]
    layout = go.Layout(
        title='January 2013 Sales Report',
    )

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='axt-hover-bar.html')

if __name__ == '__main__':
    draw_bar_graph()




# import urllib2
#
#
#
# def download_file(download_url):
#     response = urllib2.urlopen(download_url)
#     file = open("document.pdf", 'w')
#     file.write(response.read())
#     file.close()
#     print("Completed")
#
# def main():
#     download_file("https://www.caida.org/publications/presentations/2011/as_core_visualizing/as_core_visualizing.pdf")
#
# if __name__ == "__main__":
#     main()




# import plotly
# import plotly.graph_objs as go
#
# import six.moves.urllib
# import json
#
# colorscale = [[0.0, 'rgb(254,224,144)'], [0.1111111111111111, 'rgb(253,174,97)'], [0.2222222222222222, 'rgb(244,109,67)'],
#               [0.3333333333333333, 'rgb(215,48,39)'], [0.4444444444444444, 'rgb(165,0,38)'],
#               [0.5555555555555556, 'rgb(49,54,149)'], [0.6666666666666666, 'rgb(69,117,180)'],
#               [0.7777777777777778, 'rgb(116,173,209)'], [0.8888888888888888, 'rgb(171,217,233)'],
#               [1.0, 'rgb(224,243,248)']]
#
# response = six.moves.urllib.request.urlopen('https://raw.githubusercontent.com/plotly/datasets/master/custom_heatmap_colorscale.json')
# dataset = json.load(response)
#
# data = [
#     go.Heatmap(
#         z=dataset['z'],
#         colorscale=colorscale
#     )
# ]
# plotly.offline.plot(data, filename='demo.html')





















# import networkx as nx
# import plotly
# import plotly.graph_objs as go
#
# colorscale = [[0.0, 'rgb(165,0,38)'], [0.1111111111111111, 'rgb(215,48,39)'],
#                   [0.2222222222222222, 'rgb(244,109,67)'], [0.3333333333333333, 'rgb(253,174,97)'],
#                   [0.4444444444444444, 'rgb(254,224,144)'], [0.5555555555555556, 'rgb(224,243,248)'],
#                   [0.6666666666666666, 'rgb(171,217,233)'], [0.7777777777777778, 'rgb(116,173,209)'],
#                   [0.8888888888888888, 'rgb(69,117,180)'], [1.0, 'rgb(49,54,149)']]
#
# as_graph = nx.Graph()
#
# as_graph.add_node(1, longtidude = 123.4, pos = (12, 123.4), degree = -12)
# as_graph.add_node(2, longtidude = 63.1234, pos = (12, 63.4), degree = -1)
# as_graph.add_node(3, longtidude = 223.1234, pos = (12, 183.4), degree = 1)
# as_graph.add_node(4, longtidude = 183.1234, pos = (12, 23.4), degree = 12)
# as_graph.add_node(8, longtidude = 34.0, pos = (12, 34.0), degree = 123)
#
# edges = [(1,2),(2,3),(3,4),(4,8),(8,1),(1,4),(1,6)]
#
# as_graph.add_edges_from(edges)
#
# data = []
#
# for edge in as_graph.edges:
#         try:
#             r0, t0 = as_graph.node[edge[0]]['pos']
#             degree0 = as_graph.node[edge[0]]['degree']
#             r1, t1 = as_graph.node[edge[1]]['pos']
#             degree1 = as_graph.node[edge[1]]['degree']
#
#             edge_color = colorscale[min(degree0,degree1)/123][1]
#
#             edge_r = [r0, r1]
#             edge_theta = [t0, t1]
#
#             single_edge = go.Scatterpolar(
#                 r=edge_r,
#                 theta=edge_theta,
#                 line=dict(
#                     width=2,
#                     color=edge_color,
#                 ),
#                 mode='lines'
#             )
#
#             data.append(single_edge)
#
#         except(KeyError):
#             continue
#
# fig = go.Figure(data=data)
#
# plotly.offline.plot(fig, filename='demo.html', auto_open=True)