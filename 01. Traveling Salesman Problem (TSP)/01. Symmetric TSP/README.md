# Symmetric Traveling Salesman Problem (Symmetric TSP)

The **Symmetric Traveling Salesman Problem (Symmetric TSP)** is a classic combinatorial optimization problem and a specific version of the Traveling Salesman Problem (TSP). In Symmetric TSP, a salesperson (or agent) must find the shortest possible tour that visits each city exactly once, then returns to the starting city, with distances between cities being symmetric. This means that the distance from city $( A )$ to city $( B )$ is the same as the distance from $( B )$ to $( A )$, making the underlying graph undirected.

### Key Characteristics of Symmetric TSP
1. **Symmetry**: The distance or cost between any pair of cities is the same in both directions. If $(d_{ij})$ is the distance from city $(i)$ to city $(j)$, then $(d_{ij} = d_{ji})$ for all city pairs $(i)$ and $(j)$.
2. **Undirected Graph Representation**: Since the distances are symmetric, the problem can be represented on an undirected, weighted graph where nodes represent cities, and edges represent the distances or costs between them.
3. **NP-hardness**: Symmetric TSP is NP-hard, meaning that as the number of cities grows, the problem becomes computationally intractable for exact algorithms. This motivates the development of heuristic and metaheuristic approaches.

### Problem Formulation of Symmetric TSP
In Symmetric TSP, we aim to find a **Hamiltonian cycle** (a cycle that visits each node exactly once) with the minimum total weight (distance or cost). Mathematically, the problem is typically formulated as an **Integer Linear Program (ILP)**.

### Differences Between Symmetric and Asymmetric TSP
1. **Symmetry of Distances**:
   - In Symmetric TSP, the distances between cities are symmetric, i.e., $(d_{ij} = d_{ji})$.
   - In Asymmetric TSP, distances are directional, so $(d_{ij})$ may not equal $(d_{ji})$.

2. **Graph Representation**:
   - Symmetric TSP can be represented on an undirected graph, while Asymmetric TSP requires a directed graph.

3. **Applications**:
   - Symmetric TSP is often used in geographic routing, where travel between two points is usually independent of direction (e.g., Euclidean distances).
   - Asymmetric TSP is common in cases with one-way streets or directional costs, such as in airline routes or delivery scenarios where costs differ based on direction.

### Exact Methods for Solving Symmetric TSP
Due to the symmetric nature of distances, Symmetric TSP is often more amenable to optimization techniques compared to Asymmetric TSP. Here are some exact methods commonly used:

1. **Branch and Bound**:
   - Uses bounding functions to prune the search space, efficiently finding optimal solutions for smaller instances.
   - **Little’s Algorithm** is a well-known Branch and Bound method for Symmetric TSP.

2. **Dynamic Programming (Held-Karp Algorithm)**:
   - Reduces redundant calculations by storing results of subproblems, achieving a complexity of \(O(n^2 \cdot 2^n)\).

3. **Integer Linear Programming (ILP)**:
   - Solves the TSP by formulating it as an ILP and using subtour elimination constraints.
   - Common ILP solvers include **Gurobi**, **CPLEX**, and **GLPK**.

4. **Branch and Cut**:
   - Combines Branch and Bound with cutting planes to eliminate fractional solutions in the linear relaxation.
   - This is one of the most efficient methods for solving large instances of Symmetric TSP and is implemented in several TSP solvers, such as **Concorde**.

### Heuristic and Metaheuristic Methods for Symmetric TSP
While exact methods work well for small to medium-sized instances, heuristic and metaheuristic approaches are often necessary for larger instances. Some effective heuristic approaches for Symmetric TSP include:

1. **Nearest Neighbor Heuristic**:
   - Greedily selects the nearest unvisited city, building a feasible (though often suboptimal) solution.

2. **Christofides Algorithm**:
   - For metric TSP, guarantees a solution within 1.5 times the optimal solution by constructing a minimum spanning tree, finding a minimum matching, and combining them.

3. **Local Search (2-opt and 3-opt)**:
   - Improvement heuristics that swap edges to iteratively reduce tour length.

4. **Simulated Annealing, Genetic Algorithms, and Ant Colony Optimization**:
   - Metaheuristics that explore a larger search space, effective for finding high-quality solutions for large TSP instances.

### Example of Symmetric TSP
Consider a simple instance of Symmetric TSP with four cities and the following distance matrix (where $(d_{ij} = d_{ji})$):

|       | City 1 | City 2 | City 3 | City 4 |
|-------|--------|--------|--------|--------|
| **City 1** | 0      | 10     | 15     | 20     |
| **City 2** | 10     | 0      | 35     | 25     |
| **City 3** | 15     | 35     | 0      | 30     |
| **City 4** | 20     | 25     | 30     | 0      |

1. **Objective**: Find the minimum-cost tour that visits each city once and returns to the starting city.
2. **Solution (Example)**:
   - One possible tour is **1 → 2 → 4 → 3 → 1** with a total distance of $(10 + 25 + 30 + 15 = 80)$.
   - For Symmetric TSP, this tour will have the same distance in either direction, e.g., **1 → 3 → 4 → 2 → 1** would also yield $80$.

### Applications of Symmetric TSP
Symmetric TSP appears in numerous real-world applications where distances or travel costs are not directional, including:

1. **Logistics and Distribution**:
   - Routing delivery trucks or mail carriers in areas without one-way streets.
   
2. **Manufacturing**:
   - Ordering machines or processing steps where travel between locations has consistent costs.
   
3. **Circuit Board Design**:
   - Determining the shortest path for connections between nodes on a circuit board.

4. **Tourism and Travel**:
   - Planning round trips or tours where the travel cost is the same in either direction, such as planning road trips.

### Limitations of Symmetric TSP
While Symmetric TSP is easier to solve than the Asymmetric TSP, it still presents computational challenges as the problem size grows:

1. **Computational Intractability**:
   - Exact methods become impractical for large instances due to exponential complexity, requiring heuristic or metaheuristic solutions.

2. **Inflexibility in Modeling Asymmetric Scenarios**:
   - In many real-world problems, travel costs may be asymmetric due to one-way roads, fuel costs, or time-based traffic variations. Symmetric TSP does not accommodate these scenarios directly.

### Conclusion
Symmetric TSP is a fundamental problem in combinatorial optimization with wide-ranging applications. It is characterized by symmetric travel costs, making it suitable for undirected graph models. While exact methods like Branch and Bound, Dynamic Programming, and Branch and Cut provide optimal solutions for smaller instances, heuristic and metaheuristic approaches are often needed for larger instances. Symmetric TSP remains an essential benchmark in optimization research, providing insights and methods applicable to other combinatorial and routing problems
