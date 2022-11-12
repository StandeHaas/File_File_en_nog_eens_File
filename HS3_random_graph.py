from graph import Graph
from vertex import Vertex
import random

def random_G(n_vertices, max_n_edges=2, max_weight=False):
    G = Graph()
    list_of_vertices = []
    for val in range(n_vertices):
        vertex = Vertex(val)
        list_of_vertices.append(vertex)
        G.add_vertex(vertex)

    for v_idx in range(len(list_of_vertices)):
        v = list_of_vertices[v_idx]
        list_of_vertices.remove(v)
        for _ in range(max_n_edges):
            if max_weight is not False: 
                G.add_edge(v, random.choice(list_of_vertices), weight=random.randrange(1, max_weight))
            else: 
                G.add_edge(v, random.choice(list_of_vertices))
        list_of_vertices.insert(v_idx, v)
    return G

def standard_G():
    G_standard = Graph()
    standard_list = [1,2,3,4,5,6,7,8,9,10]
    standard_list_of_vertices = []
    for i in range(len(standard_list)):
        vertex = Vertex(standard_list[i])
        standard_list_of_vertices.append(vertex)
        G_standard.add_vertex(vertex)
    for i in range(len(standard_list)):
        v = standard_list_of_vertices[i]
        G_standard.add_edge(v, standard_list_of_vertices[2], weight = random.randint(1, 10))
    return G_standard

def test_G():
    g = Graph(True)
    lst = ['1', '2', '3', '4', '5', '6']
    list_of_vertices = []
    for i in range(len(lst)):
        vertex = Vertex(lst[i])
        list_of_vertices.append(vertex)
        g.add_vertex(vertex)
    g.add_edge(list_of_vertices[0], list_of_vertices[1], 5)
    g.add_edge(list_of_vertices[0], list_of_vertices[4], 5)
    g.add_edge(list_of_vertices[1], list_of_vertices[2], 5)
    g.add_edge(list_of_vertices[1], list_of_vertices[4], 5)
    g.add_edge(list_of_vertices[2], list_of_vertices[3], 5)
    g.add_edge(list_of_vertices[3], list_of_vertices[5], 5)
    g.add_edge(list_of_vertices[3], list_of_vertices[4], 5)
    return g