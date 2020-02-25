# NP Problems
### Luke Ritchie
Algorithms are written in pseudocode, with python-esq list structures

## Vertex 2-Color
#### Given a graph G=(V,E), is there a way to color the vertices,  using two colors, so that no edge connects two vertices  that have the same color

Using BFS we check starting from each vertex whether there exists a 2-coloring possible. This is more of a bipartite algorithm. The 'color' subfunction returns false if there is no 2-coloring possible from the given node. '2-color' loops through each vertex and returns true when it finds a coloring that is valid or returns false when it has exhausted all possible colorings and found none that are valid. This algorithm is O(V^2), as it will loop over each vertex in both the '2-color' function, and the 'color' function.
```
function 2-color(V, E):
    outcomes = []
    for vertex in V:
        if color(vertex, E):
            return True
    return False


function color(starting_vertex, E):
    color1 = BLUE
    color2 = RED
    visited = [] # used as queue
    visited.append(starting_vertex)
    while len(visited) > 0:
        v = visited.pop()
        
        if (v,v) in E:
            return False
        for vertex in V:
            if (v, vertex) in E and vertex.color == None:
                # set to opposite color as current vertex
                vertex.color = color1 if v.color==color2 else color2 
                visited.append(vertex)
            elif (v, vertex) in E and vertex.color == v.color:
                return False
        
        return True

    return False
``` 



## 2-SAT
#### Given a Boolean formula Phi in conjunctive normal form (an AND of ORs) where each OR has one or two literals, is Phi satisfiable?

I converted this problem into a graph by observing that (A V B) == (~A -> B) ^ (~B->A). If this graph contains a doubly connected path from X -> ~X (i.e. contains x->~x and ~x->x), then it cannot be satisfiable. I began by preprocessing into two graph structures, conditionals, and negated conditionals, to represent the different directions in the graph. 
It worst case runs <=n loops, and <=2n depth-first searches of depth <=n, so order O(n^3)
```
function 2_SAT(phi):
    conditionals = []
    neg_conditionsals = []

    for clause in phi:
        if len(clause)==1:
            conditionals.push(clause[0])
        else if len(clause)==2:
            conditionals.push((-clause[0], clause[1]))
            neg_conditionals.push((-clause[1], clause[0]))

    visited = []
    neg_visited = []
    dfs = [] #to be used as stack
    back_dfs #used as stack, reverse traversal

    for clause in conditionals:
        tracked = clause[0]
        dfs.append(clause)
        visited.append(clause)
        while(len(dfs)>0):
            curr = dfs[-1]
            delete(dfs[-1])
            if curr[1] == -(tracked):
                # we found its negation, now we check if the negation is 
                # also connected to its own negation
                back_dfs.append(curr)
                while(len(back_dfs)>0):
                    back_curr = back_dfs[-1]
                    delete(back_dfs[-1])
                    neg_visited.append(back_curr)
                    if back_curr[1] == tracked:
                        # We traveled from literal, to its negation, back to itself
                        # so the equation cannot be satisfiable
                        return False
                    else:
                        for c in neg_conditionals:
                            if (c not in neg_visited and 
                            back_curr[0]==c[0] and 
                            c[1]!=back_curr[1]):
                                back_dfs.push(c)
                    # move on to next clause
                    neg_visted = []
                    break
            else:
                for c in conditionals:
                    if (c not in visited and 
                    curr[0]==c[0] and 
                    c[1]!=curr[1]):
                        dfs.push(c)
    return True
```


## Hamiltonian Path
#### Given a graph G=(V,E), is there a simple (non-self-intersecting)  path that visits each vertex exactly one?

I think I'm still confused because I couldn't figure out how to do this in less than factorial time. I changed the algorithm to generate a path and then check if it is a solution or not. I'm not sure if that's what you meant by an NP algorithm though. 

The function will generate a path non-deterministically and then check it in constant time. It loops until it cannot add a new edge to the path, only adding when it can find an edge that connects a vertex not already in the path. It samples vertexes from those remaining, removing them from the sampling list after adding them.  As soon as it samples a vertex it cannot add to the graph it breaks. It then checks if it added an amount of vertexes equal to the size of the graph (visited each vertex), and that there are no remaining vertices. This is not guaranteed to find a solution, but it does generate a solution in O(|V|) time and check it in O(1) time. 


```
function Hamiltonian_Path(V, E):
    remaining = V
    vertices_in_path = []
    while len(vertices_in_path) < len(V):
        next = rand.sample(remaining)
        if next not in verticies_in_path and any((vertices_in_path, next) in E):
            remaining.delete(next)
            vertices_in_path.append(next)
        else:
            break
    if len(vertices_in_path) != len(V) or len(remaining) > 0:
        return False
    else:
        return True


```

## Exact 3Cover
#### Given a universe U = {x_1, ..., x_k} and S, a collection of subsets   of U, where each subset has size 3, is there a subset T of  S    such that the subsets that are elements of T don't overlap,   but their union is U?  (In other words, T partitions U.)


The function will generate a union of subsets of S non-deterministically and then check it in polynomial time. It loops until it reaches a max size or finds a subset that contains duplicate elements. It then loops over the chosen sets, adding each element in the sets into a list. If it adds an element that already exists in the list, there must have been overlap, so it returns False. Otherwise if it makes it through all elements without finding a duplicate it returns true. It generates a solution in O(|U|) and checks it in O(|S|)
```
function 3Cover(U, S):
    Set newset = {}
    Set subsetT = {}
    chosenSets = []
    while len(newset) < len(U):
        subsetT = rand.sample(S)
        if len(newset.union(subsetT)) == len(subsetT+3):
            S.delete(subsetT)
            chosenSets.append(subsetT)
        else:
            break
    temp = []
    for set in chosenSets:
        for element in set:
            if element in temp:
                return False
            else:
                temp.append(element)
    return True
```

