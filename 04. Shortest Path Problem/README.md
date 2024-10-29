# Shortest Path Problem

<p align="center"> 
  <img width="600" height="350" src="https://www.norsemathology.org/mediawiki-1.38.1/images/8/8e/Ellis2.gif"> 
</p>

### 1. What is the Shortest Path Problem?

The **Shortest Path Problem** is a fundamental optimization problem in graph theory, where the goal is to find the path between two vertices (a source and a destination) in a graph that minimizes the total distance or cost. This problem is essential in fields like navigation, network routing, and logistics.

#### Problem Description
- **Given**: 
  - A graph \( G = (V, E) \) with a set of vertices \( V \) and edges \( E \), where each edge \( (u, v) \in E \) has an associated weight (distance or cost) \( w(u, v) \).
- **Objective**: Find the path from a source vertex \( s \) to a target vertex \( t \) that minimizes the sum of edge weights along the path.

### 2. Types of Shortest Path Problems

The Shortest Path Problem has several variations depending on constraints and graph structure:

1. **Single-Source Shortest Path**:
   - Finds the shortest paths from a single source vertex to all other vertices. Dijkstra’s and Bellman-Ford algorithms are commonly used.

2. **Single-Destination Shortest Path**:
   - Similar to the single-source problem but focuses on paths leading to a specified destination.

3. **All-Pairs Shortest Path**:
   - Finds the shortest paths between every pair of vertices in the graph. Algorithms like Floyd-Warshall and Johnson’s algorithm are typical for this problem.

4. **k-Shortest Paths**:
   - Finds the top \( k \) shortest paths between two vertices, useful in routing and navigation systems where multiple route options are desirable.

### 3. Mathematical Model of the Shortest Path Problem

To formulate the Shortest Path Problem as an optimization problem, we define the following:

#### Decision Variables
- Let \( x_{ij} \) be a binary decision variable:
  - \( x_{ij} = 1 \) if the edge \( (i, j) \) is part of the shortest path from \( s \) to \( t \).
  - \( x_{ij} = 0 \) otherwise.

#### Parameters
- \( w_{ij} \): Weight or cost associated with edge \( (i, j) \).
- \( s \): The source vertex.
- \( t \): The target vertex.

#### Objective Function
The objective is to minimize the total path weight from \( s \) to \( t \):

\[
\text{Minimize } \sum_{(i, j) \in E} w_{ij} \cdot x_{ij}
\]

#### Constraints
1. **Flow Conservation Constraints**:
   - Ensure flow starts from the source and ends at the target.
   - For the source vertex \( s \):
     \[
     \sum_{j: (s, j) \in E} x_{sj} = 1
     \]
   - For the target vertex \( t \):
     \[
     \sum_{i: (i, t) \in E} x_{it} = 1
     \]
   - For all intermediate vertices \( k \in V \setminus \{s, t\} \):
     \[
     \sum_{i: (i, k) \in E} x_{ik} = \sum_{j: (k, j) \in E} x_{kj}
     \]

2. **Binary Constraints**:
   - Ensure all variables are binary:
     \[
     x_{ij} \in \{0, 1\}, \quad \forall (i, j) \in E
     \]

#### Summary of the Shortest Path Model

- **Objective**: \( \text{Minimize } \sum_{(i, j) \in E} w_{ij} \cdot x_{ij} \)
  
- **Constraints**:
  1. Flow conservation to connect the source and target.
  2. Binary constraints on path selection.

This model can be solved using integer programming, but for large or sparse graphs, specialized algorithms like Dijkstra’s or A* are typically more efficient.

### 4. Solution Approaches for the Shortest Path Problem

The Shortest Path Problem has both exact and heuristic solution approaches, depending on the graph's characteristics:

#### a. **Dijkstra’s Algorithm**
   - A greedy algorithm optimal for graphs with non-negative weights, finding the shortest path from a single source to all other vertices efficiently.

#### b. **Bellman-Ford Algorithm**
   - Handles graphs with negative weights, though it has higher time complexity than Dijkstra’s algorithm. Useful in scenarios with possible negative edge weights.

#### c. **Floyd-Warshall Algorithm**
   - An all-pairs shortest path algorithm with \( O(|V|^3) \) complexity, best for dense graphs where shortest paths between all vertex pairs are needed.

#### d. **A* Search Algorithm**
   - A heuristic-based algorithm often used in AI and game development. It finds the shortest path from source to target efficiently by using a heuristic to guide the search.

#### e. **Johnson’s Algorithm**
   - Efficiently finds all-pairs shortest paths in sparse graphs with both positive and negative weights, leveraging Dijkstra’s and Bellman-Ford algorithms.

### Conclusion

The Shortest Path Problem is a foundational optimization problem with a range of variations suited to different applications, from network routing to logistics and navigation. The choice of solution approach depends on graph properties, such as edge weights and density, making it a versatile problem in combinatorial optimization.
