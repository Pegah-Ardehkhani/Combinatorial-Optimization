### 1. What is the Shortest Path Problem?

<p align="center"> 
  <img width="650" height="350" src="https://b2316719.smushcdn.com/2316719/wp-content/uploads/2023/03/dijkstra_animation_02.gif?lossy=1&strip=1&webp=1"> 
</p>

The **Shortest Path Problem** is a fundamental optimization problem in graph theory, where the goal is to find the shortest possible route between two nodes in a graph based on edge weights. This problem has numerous applications, such as navigation systems, communication networks, and logistics.

#### Problem Description
- **Given**: 
  - A directed or undirected graph $( G = (V, E) )$, where $( V )$ is the set of vertices (nodes), $( E )$ is the set of edges, and $( w_{ij} )$ is the weight (or cost) associated with edge $((i, j))$.
- **Objective**: Determine the shortest path from a source node $( s \in V )$ to a destination node $( t \in V )$, minimizing the sum of edge weights along the path.

---

### 2. Types of Shortest Path Problems

Several variants of the shortest path problem exist, depending on the graph's structure and additional constraints:

1. **Single-Source Shortest Path**:
   - Find the shortest paths from a single source node $( s )$ to all other nodes in the graph.

2. **Single-Pair Shortest Path**:
   - Find the shortest path between a specific pair of nodes, $( s )$ (source) and $( t )$ (target).

3. **All-Pairs Shortest Path**:
   - Find the shortest paths between all pairs of nodes in the graph.

4. **K-Shortest Paths**:
   - Determine the $( k )$-shortest distinct paths between two nodes, often used in routing and logistics.

5. **Constrained Shortest Path**:
   - Find the shortest path that satisfies additional constraints, such as time limits or resource bounds.

---

### 3. Mathematical Model of the Shortest Path Problem

To formulate the shortest path problem as an optimization problem, we define the following:

#### Decision Variables
- Let $( x_{ij} )$ be a binary decision variable:
  - $( x_{ij} = 1 )$ if edge $((i, j))$ is included in the path.
  - $( x_{ij} = 0 )$ otherwise.

#### Parameters
- $( w_{ij} )$: Weight (or cost) of edge $((i, j))$.
- $( V )$: Set of vertices.
- $( E )$: Set of edges in the graph.
- $( s )$: Source node.
- $( t )$: Target node.

---

#### Objective Function
Minimize the total weight of the path from the source $( s )$ to the target $( t )$:

$\text{Minimize } \sum_{(i,j) \in E} w_{ij} \cdot x_{ij}$

---

#### Constraints

1. **Flow Conservation**:
   - Ensure that for every node, the incoming and outgoing flow satisfy the following:
     - At the source node $( s )$, one unit of flow is sent out:
       $\sum_{j: (s, j) \in E} x_{sj} - \sum_{i: (i, s) \in E} x_{is} = 1$
     - At the target node $( t )$, one unit of flow is received:
       $\sum_{i: (i, t) \in E} x_{it} - \sum_{j: (t, j) \in E} x_{tj} = 1$
     - For all other intermediate nodes \( v \in V \setminus ${s, t\} )$, the inflow equals the outflow:
       $\sum_{i: (i, v) \in E} x_{iv} - \sum_{j: (v, j) \in E} x_{vj} = 0$

2. **Binary Constraints**:
   - Each edge can either be included or not in the path:
     $x_{ij} \in \{0, 1\}, \quad \forall (i, j) \in E$

---

#### Summary of the Shortest Path Model

- **Objective**: Minimize the total weight of edges included in the path from the source $( s )$ to the target $( t )$.
- **Constraints**:
  1. Flow conservation ensures a valid path from $( s )$ to $( t )$.
  2. Binary constraints ensure that edges are either included or excluded.

---

### 4. Solution Approaches for the Shortest Path Problem

The Shortest Path Problem can be solved efficiently with the following algorithms:

#### a. **Dijkstra’s Algorithm**
   - **Applicability**: Graphs with non-negative edge weights.
   - **Approach**:
     - Start at the source node and iteratively select the node with the smallest tentative distance, updating distances to its neighbors.

#### b. **Bellman-Ford Algorithm**
   - **Applicability**: Graphs with negative edge weights (but no negative cycles).
   - **Approach**:
     - Relax all edges $( |V| - 1 )$ times, ensuring the shortest path distances are updated.

#### c. **Floyd-Warshall Algorithm**
   - **Applicability**: All-pairs shortest paths.
   - **Approach**:
     - Iteratively update a distance matrix using the formula:
       $d[i][j] = \min(d[i][j], d[i][k] + d[k][j])$

#### d. **A* Algorithm**
   - **Applicability**: Spatial graphs with a heuristic (e.g., Euclidean distance).
   - **Approach**:
     - Use a combination of actual and heuristic distances to prioritize nodes.

#### e. **Bidirectional Search**
   - **Applicability**: Undirected graphs for single-pair shortest paths.
   - **Approach**:
     - Perform simultaneous searches from the source and target nodes.

---

### Conclusion

The Shortest Path Problem is a widely studied optimization problem with applications in transportation, network design, and many other domains. Algorithms like Dijkstra’s and Bellman-Ford provide efficient solutions for single-source problems, while Floyd-Warshall and Johnson's algorithms address all-pairs scenarios. Proper selection of the algorithm depends on the graph's structure and specific requirements of the problem.
