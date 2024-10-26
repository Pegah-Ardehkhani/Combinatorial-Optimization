# Traveling Salesman Problem (TSP)

<p align="center"> 
  <img width="450" height="350" src="https://community.ptc.com/t5/image/serverpage/image-id/2899i03C9464782900092/image-size/large?v=v2&px=999"> 
</p>

### 1. What is the Traveling Salesman Problem (TSP)?

The **Traveling Salesman Problem (TSP)** is a classic optimization problem in which a salesman (or an agent) must visit a set of cities exactly once, return to the starting city, and minimize the total travel distance (or cost). The goal is to find the shortest possible route that allows the salesman to visit each city once and return to the starting point.

#### Problem Description
- Given: A set of $( n )$ cities and the distances (or costs) between each pair of cities.
- Objective: Find the shortest possible route that starts and ends at a specified city, visiting each other city exactly once.

### 2. Mathematical Model of TSP

To formulate the TSP as an optimization problem, we define the following:

#### Decision Variables
- Let $( x_{ij} )$ be a binary decision variable:
  - $( x_{ij} = 1 )$ if the path from city $( i )$ to city $( j )$ is part of the optimal route.
  - $( x_{ij} = 0 )$ otherwise.

#### Parameters
- $( d_{ij} )$: The distance (or cost) of traveling from city $( i )$ to city $( j )$.

#### Objective Function
The objective is to minimize the total distance (or cost) of the tour:

$\text{Minimize } \sum_{i=1}^n \sum_{j=1}^n d_{ij} x_{ij}$

#### Constraints

1. **Each City is Visited Exactly Once**:
   - Each city $( i )$ must have exactly one incoming and one outgoing edge:
   
     $\sum_{j=1}^n x_{ij} = 1$   $\quad$    $\forall i = 1, ..., n$

     $\sum_{i=1}^n x_{ij} = 1$   $\quad$   $\forall j = 1, ..., n$

   - These constraints ensure that each city is entered and exited exactly once.

3. **Subtour Elimination**:
   - One of the major challenges of TSP is to eliminate **subtours** (routes that visit a subset of cities and do not form a complete tour). A common approach to prevent subtours is to use additional variables and constraints:
   - Define a variable $( u_i )$ for each city $( i )$ to represent the position of the city in the tour.
   - The subtour elimination constraints are:
     
     $u_i - u_j + n.x_{ij} \leq n - 1$   $\quad$   $\forall i, j = 2, ..., n, ; \ i \neq j$
     
   - These constraints prevent the formation of smaller cycles (subtours) by enforcing the order of cities in the tour.

4. **Binary Constraints**:
   - $( x_{ij} )$ should be a binary variable, meaning:
     $x_{ij} \in \{0, 1}$

5. **Non-negativity for Position Variables**:
   - For the subtour elimination constraints, the position variables $( u_i )$ should be non-negative:
     $u_i \geq 0$ $\quad$ $\forall i = 1, ..., n$

#### Summary of the TSP Model:

- **Objective**: $\text{Minimize } \sum_{i=1}^n \sum_{j=1}^n d_{ij} x_{ij}$
  
- **Constraints**:
  1. Each city has exactly one incoming and outgoing edge.
  2. Subtour elimination constraints.
  3. Binary constraints on $( x_{ij} )$.
  4. Non-negativity constraints for $( u_i )$.

This model can be solved using integer programming techniques, where the binary decision variables are optimized to find the minimum-cost route.

#### Special Features of the TSP Model:

1. **Problem Complexity:**
   
- **Exponential Growth:** The number of feasible solutions for an n-city TSP is $\frac{1}{2}(n-1)!$ as you've noted, which grows exponentially with $n$. This makes TSP very challenging as $n$ increases.
  
- **NP-hard**: TSP is a well-known NP-hard problem in combinatorial optimization, meaning there is no known polynomial-time algorithm that guarantees an optimal solution for large instances.

2. **Types of TSP:**
   
 - Symmetric TSP: In the symmetric TSP, the distance between any two cities is the same in both directions, so $( d_{ij} = d_{ji})$

 - Asymmetric TSP: In the asymmetric TSP, distances may differ depending on direction, so $( d_{ij} \neq d_{ji})$

 - Euclidean TSP: A specific TSP where cities are points in the Euclidean plane, and distances are the Euclidean distances between points. This TSP type often appears in geographic applications.

### 3. Alternative Ways to Solve TSP

Aside from solving TSP with an optimization model, there are other methods and algorithms to tackle the problem. Here are some alternative approaches:

#### a. **Heuristic Algorithms**
Heuristic algorithms provide approximate solutions to the TSP, often with significantly reduced computation time. Some popular heuristic approaches include:
   - **Nearest Neighbor Heuristic**: Start from an arbitrary city and at each step, move to the nearest unvisited city until all cities are visited.
   - **Greedy Algorithm**: Select the shortest available edge that does not form a cycle (except for the final cycle) until a complete tour is formed.
   - **Christofides Algorithm**: A heuristic that guarantees a solution within 1.5 times the optimal solution for metric TSP (where distances satisfy the triangle inequality).

#### b. **Metaheuristic Algorithms**
Metaheuristic algorithms use probabilistic techniques to explore the solution space and can often provide high-quality solutions for TSP. Some popular metaheuristics include:
   - **Simulated Annealing**: A probabilistic algorithm that explores the solution space by allowing both uphill and downhill moves, gradually reducing the probability of uphill moves to converge to an optimal solution.
   - **Genetic Algorithm**: Uses evolutionary techniques inspired by natural selection, where solutions evolve over generations to optimize the tour.
   - **Ant Colony Optimization**: Inspired by the behavior of ants searching for food, this algorithm uses pheromone trails to probabilistically build solutions, emphasizing shorter routes.

#### c. **Dynamic Programming**
   - **Held-Karp Algorithm**: A dynamic programming approach for TSP that solves subproblems recursively and combines them for the overall solution. This approach has a time complexity of \( O(n^2 \cdot 2^n) \), making it feasible for only relatively small instances of TSP.

#### d. **Branch and Bound**
   - This is an exact algorithm that systematically explores subsets of the solution space, using bounds to eliminate suboptimal branches. Although it guarantees an optimal solution, the computational cost can become impractical for large instances.

#### e. **Approximation Algorithms**
   - For special cases of TSP, such as metric TSP (where distances satisfy the triangle inequality), approximation algorithms can provide solutions within a guaranteed ratio of the optimal solution.
   - For instance, the **Christofides algorithm** is a 1.5-approximation for metric TSP.
