# runtime O((E) + (V)log(V))
from graph import Graph
from vertex import Vertex
from heapq import heappop, heappush
from math import inf
import random

def dijkstras(graph, start):
    distances = {}
    for vertex in graph.graph_dict.keys():
        distances[vertex] = inf
    distances[start] = 0
    vertices_to_explore = [(0, start)]
    while vertices_to_explore:
        current_distance, current_vertex = heappop(vertices_to_explore)
        for neighbor, edge_weight in graph.graph_dict[current_vertex].get_edges_weight():
            new_distance = current_distance + edge_weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(vertices_to_explore, (new_distance, neighbor))
    return distances

def visited_all_nodes(visited_vertices):
    for vertex in visited_vertices:
        if visited_vertices[vertex] == 'unvisited':
            return False
    return True

def traveling_salesperson(graph, start_vertex):
    path = ""
    visited_vertices = {x: 'unvisited' for x in graph.graph_dict}
    current_vertex = start_vertex
    visited_vertices[current_vertex] = 'visited'
    path += str(current_vertex) + ' '
    visited_all_vertices = visited_all_nodes(visited_vertices)
    while not visited_all_vertices:
        current_vertex_edges = graph.graph_dict[current_vertex].get_edges()
        current_vertex_edge_weights = {}
        empty_dict = {}
        for edge in current_vertex_edges:
            current_vertex_edge_weights[edge] = graph.graph_dict[current_vertex].get_edge_weight(edge)
        found_next_vertex = False
        next_vertex = ""
        while found_next_vertex == False:
            if current_vertex_edge_weights == empty_dict:
                break
            next_vertex = min(current_vertex_edge_weights, key=current_vertex_edge_weights.get)
            if visited_vertices[next_vertex] == 'visited':
                current_vertex_edge_weights.pop(next_vertex)
            else:
                found_next_vertex = True
        if current_vertex_edge_weights == empty_dict:
            visited_all_vertices = True
        else: 
            current_vertex = next_vertex
            visited_vertices[current_vertex] = 'visited'
            path += str(current_vertex) + ' '
            visited_all_vertices = visited_all_nodes(visited_vertices)
    print(path)
