from vertex import Vertex

# Graph class
class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}
    
    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_vertices(self, lst):
        for vertex in lst:
            self.add_vertex(vertex)
    
    def add_edge(self, from_vertex, to_vertex, weight=0): 
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if self.directed == False:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)
    
    def get_vertex(self, value):
        return self.graph_dict[value]

# pathfinding algoritm which checks every single option, and stops cylces
    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]
        seen = {}
        while start: 
            current_vertex = start.pop(0)
            seen[current_vertex] = True
            if current_vertex == end_vertex:
                return True
            vertex = self.graph_dict[current_vertex]
            next_vertices = vertex.get_edges()
            next_vertices = [vertex for vertex in next_vertices if vertex not in seen]
            start += next_vertices
        return False

    def adjacency_iter(self):
        list = []
        for vertex in self.graph_dict: 
            list.append((vertex, {e: {} for e in self.graph_dict[vertex].get_edges()}))
        return(list)
            
        