# Vertex 2-Color
# Given a graph G=(V,E), is there a way to color the vertices,
#   using two colors, so that no edge connects two vertices
#   that have the same color

"""
For each vertex v_i in V:
    color v_i := color_1
    switch colors
    for each neighbor v_j of v_i:
        if v_j color == v_i color
            break
        else 
            color v_j := color_2
        
"""


# 2-SAT
# Given a Boolean formula Phi in conjunctive normal form 
#   (an AND of ORs) where each OR has one or two literals,
#    is Phi satisfiable?


# Hamiltonian Path
# Given a graph G=(V,E), is there a simple (non-self-intersecting) 
#   path that visits each vertex exactly one?


# Exact 3Cover
# Given a universe U = {x_1, ..., x_k} and S, a collection of subsets
#   of U, where each subset has size 3, is there a subset T of  S 
#   such that the subsets that are elements of T don't overlap, 
#   but their union is U?  (In other words, T partitions U.)


