# importing:
from HS3_graaf_en_vertices import Graph
from HS3_vertex import Vertex
from HS3_random_graph import random_G, standard_G, test_G
from HS3_bfs_dfs import dfs, bfs
from HS3_dijkstras_algorithm import dijkstras, visited_all_nodes, traveling_salesperson
import numpy as np  
import random 

# test Graoh

G = test_G() # random_G(20, 3, max_weight=10)
print(traveling_salesperson(G, '1'))


