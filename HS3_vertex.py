# Vertex class
class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}
    
    def get_edges(self):
        return list(self.edges.keys())

    def get_edges_weight(self):
        lst_edges = list(self.edges.keys())
        lst_weight = list(self.edges.values())
        lst = []
        for i in range(len(lst_edges)):
            lst.append((lst_edges[i], lst_weight[i]))
        return lst
    
    def get_edge_weight(self, edge):
        return self.edges[edge]
    
    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight
        