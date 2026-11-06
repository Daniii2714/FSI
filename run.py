# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print(search.breadth_first_graph_search(ab)[0].path())
print("Nodos generados: ", search.breadth_first_graph_search(ab)[1])
print("Nodos visitados: ", search.breadth_first_graph_search(ab)[2])
print("Coste total: ", search.breadth_first_graph_search(ab)[3])

print(search.depth_first_graph_search(ab)[0].path())
print("Nodos generados: ", search.depth_first_graph_search(ab)[1])
print("Nodos visitados: ", search.depth_first_graph_search(ab)[2])
print("Coste total: ", search.depth_first_graph_search(ab)[3])


print(search.branch_and_Bound_search(ab)[0].path())
print("Nodos generados: ", search.branch_and_Bound_search(ab)[1])
print("Nodos visitados: ", search.branch_and_Bound_search(ab)[2])
print("Coste total: ", search.branch_and_Bound_search(ab)[3])

print(search.branch_and_bound_subestimation_search(ab)[0].path())
print("Nodos generados: ", search.branch_and_bound_subestimation_search(ab)[1])
print("Nodos visitados: ", search.branch_and_bound_subestimation_search(ab)[2])
print("Coste total: ", search.branch_and_bound_subestimation_search(ab)[3])
# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
