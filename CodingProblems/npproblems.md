# NP Problems
### Luke Ritchie
Algorithms are written in pseudocode, with python-esq list structures

## Vertex 2-Color
#### Given a graph G=(V,E), is there a way to color the vertices,  using two colors, so that no edge connects two vertices  that have the same color

```
function 2-color(V, E):
    color1 = BLUE
    color2 = RED
    for v in V:
        if color(v, color1, color2):
            return True


function color(vertice, color, next_color)
    vertice.color = color
    children = []
    for neighbor of vertice:
        if neighbor.color == color:
            return False
        else if neighbor.color == color2:
            continue
        else:
            children.append(color(neighbor, next_color, color))
    if all(children) or len(children) == 0:
        return True
    else:
        return False
``` 



## 2-SAT
#### Given a Boolean formula Phi in conjunctive normal form (an AND of ORs) where each OR has one or two literals, is Phi satisfiable?
```
function 2_SAT(phi):
    conditionals = []
 
    for clause in phi:
        if len(clause)==1:
            conditionals.push(clause[0])
        else if len(clause)==2:
            conditionals.push((-clause[0], clause[1]))
            conditionals.push((-clause[1], clause[0]))

    visited = []
    neg_visited = []
    dfs = [] #to be used as stack

    for clause in conditionals:
        tracked = clause[0]
        dfs.push(clause)
        visited.push(clause)
        while(len(dfs)>0):
            curr = dfs.top()
            if curr[1] == -(tracked):
                return False
            else:
                for clause in conditionals:
                    if (clause not in visited and 
                    curr[0]==clause[0] and 
                    clause[1]!=curr[1]):
                        dfs.push(clause)
    

    return True
```


## Hamiltonian Path
#### Given a graph G=(V,E), is there a simple (non-self-intersecting)  path that visits each vertex exactly one?
```

function Hamiltonian_Path(V, E):
    visited = stack()
    for vertice in V:
        visited.push(vertice)
        while(len(visited) > 0):
            curr = visited.top()
            for edge in E:
                if edge[0] == curr or edge[1] == curr:
                    if edge[0] in visited and edge[1] not in visited:
                        visited.push(edge[1])
                        break
                    else if edge[0] not in visited and edge[1] in visited:
                        visited.push(edge[0])
                        break
            if len(visited) == len(V):
                return True
            if visited.top() == curr:
                visited.pop()
    return False


```

## Exact 3Cover
#### Given a universe U = {x_1, ..., x_k} and S, a collection of subsets   of U, where each subset has size 3, is there a subset T of  S    such that the subsets that are elements of T don't overlap,   but their union is U?  (In other words, T partitions U.)

```
function 3Cover(U, S):
    Set newset = {}
    Set subsetT = {}
    Stack s = []
    for set_i in S:
        newset = set_i
        s.push(newset)
        while(len(s)>0):
            curr = s.top()
            for set_j in S:
                if len(curr.union(set_j)) == len(curr)+3:
                    s.push(curr.union(set_j))
                    break
            if s.top() == curr:
                s.pop()
            if len(s.top()) == len(U):
                return True
        
    return False

```

