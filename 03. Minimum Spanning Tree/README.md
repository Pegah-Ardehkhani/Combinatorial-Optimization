# Minimum Spanning Tree Problem

<p align="center"> 
  <img width="650" height="350" src="https://s3.stackabuse.com/media/articles/graphs-in-python-minimum-spanning-trees-prims-algorithm-8.gif"> 
</p>

### 1. What is the Minimum Spanning Tree Problem?

The **Minimum Spanning Tree (MST) Problem** is a foundational optimization problem in graph theory, where the goal is to find a subset of edges that connect all nodes in a graph with the minimum possible total edge weight. MST has various applications, including network design, clustering, and image processing.

#### Problem Description
- **Given**: 
  - An undirected, connected graph $( G = (V, E) )$, where $( V )$ is the set of vertices (nodes) and $( E )$ is the set of edges, each with a weight $( w_{ij} )$.
- **Objective**: Identify a subset of edges that forms a tree connecting all vertices while minimizing the total edge weight.

### 2. Types of Spanning Tree Problems

While MST is the primary form, several related problems arise with different constraints:

1. **K-Minimum Spanning Tree**:
   - Requires finding the $( k )$-smallest spanning trees, which can be useful in scenarios requiring backup paths.

2. **Degree-Constrained MST**:
   - Adds a restriction on the maximum degree of any vertex in the tree, useful in network design to limit connections per node.

3. **Minimum Steiner Tree**:
   - Extends MST by allowing additional points (Steiner points) to connect specific nodes at minimum cost.

### 3. Mathematical Model of the Minimum Spanning Tree Problem

To formulate MST as an optimization problem, we define the following:

#### Decision Variables
- Let $( x_{ij} )$ be a binary decision variable:
  - $( x_{ij} = 1 )$ if edge $( (i, j) )$ is included in the spanning tree.
  - $( x_{ij} = 0 )$ otherwise.

#### Parameters
- $( w_{ij} )$: Weight (or cost) of edge $( (i, j) )$.
- $( V )$: Set of vertices.
- $( E )$: Set of edges in the graph.

#### Objective Function
The objective is to minimize the total weight of the selected edges in the tree:

$\text{Minimize } \sum_{(i,j) \in E} w_{ij}.x_{ij}$

#### Constraints

1. **Tree Constraint**: The selected edges must form a connected acyclic subgraph covering all vertices. This constraint can be represented by enforcing that each subset $( S \subset V )$ (where $( S \neq \emptyset )$ and $(S \neq V))$ has at least one connection to $( V \setminus S )$:

   $\sum_{i \in S, j \in V \setminus S} x_{ij} \geq 1, \quad \forall S \subset V, S \neq \emptyset, S \neq V$

2. **Edge Constraints**: Ensure that the selected edges connect all nodes with exactly $( |V| - 1 )$ edges, which characterizes a tree:

   $\sum_{(i,j) \in E} x_{ij} = |V| - 1$

3. **Binary Constraints**: Each $( x_{ij} )$ should be a binary variable:

   $x_{ij} \in \{0, 1\} \quad \forall (i,j) \in E$

#### Summary of the MST Model

- **Objective**: Minimize the sum of selected edge weights to form a tree covering all vertices.
- **Constraints**:
  1. The solution must form a connected, acyclic subgraph.
  2. A total of $( |V| - 1 )$ edges must be selected.
  3. Binary constraints on $( x_{ij} )$.

### 4. Solution Approaches for MST

The MST Problem can be solved efficiently with greedy algorithms:

#### a. **Prim’s Algorithm**
   - Prim’s algorithm starts from a single vertex and grows the MST one edge at a time, choosing the minimum weight edge that connects a new vertex to the tree.

#### b. **Kruskal’s Algorithm**
   - Kruskal’s algorithm sorts edges by weight and adds them to the MST, provided they do not form a cycle, until all vertices are connected.

#### c. **Borůvka’s Algorithm**
   - Each vertex finds the smallest edge connecting it to a different component, repeatedly merging components until only one tree remains.

### Conclusion

The Minimum Spanning Tree Problem is a core optimization problem with applications across computer networks, clustering, and other areas requiring efficient connections. Efficient algorithms such as Prim's, Kruskal's, and Borůvka's provide exact solutions, making MST a well-studied problem in graph theory and combinatorial optimization.
