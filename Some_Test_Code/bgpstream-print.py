import networkx as nx

as_graph = nx.Graph()

as_graph.add_node(1)
as_graph.add_node(2)
as_graph.add_node(3)
as_graph.add_node(4)
as_graph.add_node(8)

print(as_graph.nodes)

as_graph.add_node(1, longtidude = 123.4)
as_graph.add_node(2, longtidude = 63.1234)
as_graph.add_node(3, longtidude = 223.1234)
as_graph.add_node(4, longtidude = 23.1234)
as_graph.add_node(1, longtidude = 34.0)

for node in as_graph:
    print(node, as_graph.nodes[node], as_graph.degree(node))

print(as_graph.has_node(1))









