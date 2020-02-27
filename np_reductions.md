# NP Reductions
### Luke Ritchie
### 2/27/2020

## Show that Hamiltonian Cycle is mapping reducible to Traveling Salesperson

**Hamiltonian Cycle**: The path that connects all vertices without intersection and creates a cycle. 

**Travelling Salesperson**: The shortest path connecting all vertices that returns to the origin. 

function f: set all edges in the hamiltonian graph to weight 1. f is bounded by O(E) where E is the number of edges in the graph or |E|.

If all edges are weight one, any route that visits each node exactly once and does not intersect would have a total weight equal to any other solution. Thus all solutions of the hamiltonian cycle would become solutions to the travelling salesperson. So for all graphs G in Hamiltonian cycle, f(G) is in Travelling Salesperson. 

## Show that Hamiltonian Path is mapping reducible to Hamiltonian Cycle. 

**Hamiltonian Cycle**: The path that connects all vertices without intersection and creates a cycle. 

**Hamiltonian Path**: The path that connects all vertices without intersection. 

function f: Add a vertex N that is connected to each other vertex in the graph. f is bounded by O(V) where V is the number of vertices in the graph or |V|. 

On graph f(G), the hamiltonian cycle will connect all vertices, including N. Removal of N will leave a Hamiltonian path that contains all vertexes in G, but is not cyclically connected. The resultant path from the hamiltonian cycle will be a cycle in f(G), but a disconnected path in G. 

## Prove that, if A and B are nontrivial languages in P, then A is mapping reducible to B. 

1) For a language L1 to be reducible to L2, there must exist a function f bounded by polynomial time such that for all x in L1, f(x) is in L2. 
2) If B is a non-trivial language, there must exist at least one element that is in B and at least one element that is not. I will refer to the element in B as 'b', and the element not in B as '~b'.
3) Create a function f such that it generates elements x and determines if they are in A. Since A is in P, this can be done in polynomial time. 
4) If x is in A, f(x) = b, if x is not in A, f(x) = ~b. 
5) It is now true that:
   1) for all x in A, f(x) is in B
   2) f(x) is bounded by polynomial time since A is a polynomial language.
6) Thus A is mapping reducible to B


## Prove that if 3SAT is mapping reducible in polynomial time to Evens, then P=NP

1) For a language L1 to be reducible to L2, there must exist a function f bounded by polynomial time such that for all x in L1, f(x) is in L2. 
2) If 3SAT were poly-time mapping reducible to Evens, there must exist a function f bounded by polynomial time such that each element in 3SAT's language can be mapped to an element in Evens language. 
3) The language Evens can be determined in polynomial time (if a number can be divided by 2 with no remainder it is in the language)
4) If 3SAT can be reduced to Evens by a polynomial factor, then 3SAT can be determined in polynomial time, since Evens can be solved in polynomial time (O(n^a + n^b) = O(n^c) [it would still be bounded by polynomial time])
5) If 3SAT can be determined in polynomial time, then it must be in P.
6) Since 3SAT is NP-complete (it is also NP-hard), all NP problems can be reduced to 3SAT.
7) If all NP problems can be reduced to 3SAT in polytime, they are also bounded by polytime, meaning they are also in P.
8) If NP is bounded by P, P=NP