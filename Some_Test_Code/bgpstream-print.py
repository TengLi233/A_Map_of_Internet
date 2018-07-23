import networkx as nx

as_graph = nx.Graph()

as_graph.add_node(1)
as_graph.add_node(2)
as_graph.add_node(3)
as_graph.add_node(4)
as_graph.add_node(8)

print(as_graph.nodes)

as_graph.add_node(1, longtidude = 1231234)
as_graph.add_node(2, longtidude = 1231234)
as_graph.add_node(3, longtidude = 1231234)
as_graph.add_node(4, longtidude = 1231234)
as_graph.add_node(1, longtidude = 34)

for node in as_graph:
    print(node, as_graph.nodes[node], as_graph.degree(node))

print(as_graph.has_node(1))











