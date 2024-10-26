# Exact Methods

Exact methods for solving the **Traveling Salesman Problem (TSP)** guarantee an optimal solution by exhaustively exploring the solution space or using mathematical optimization techniques to systematically prune infeasible or suboptimal solutions. Due to the NP-hard nature of the TSP, exact methods are often computationally expensive and generally feasible only for small to moderately sized instances (up to about 100 cities, depending on computational power and algorithm optimization).

Below are some of the primary exact methods for solving TSP, along with an overview of how each works, its advantages and limitations, and references to key research papers.

---

### 1. **Brute Force Search**
   - **Concept**: This is the most straightforward approach, which involves examining every possible permutation of cities to determine the shortest possible route.
   - **Algorithm**: Generate all \((n-1)!\) possible routes, calculate their total distances, and select the shortest.
   - **Complexity**: \(O((n-1)!)\), where \(n\) is the number of cities.
   - **Advantages**: Guarantees the optimal solution and is easy to understand.
   - **Limitations**: Impractical for instances larger than about 10 cities due to its factorial growth.
   - **Reference**: This approach is often presented in introductory TSP and combinatorial optimization literature, though not typically attributed to a specific research paper due to its simplicity.

---

### 2. **Dynamic Programming (Held-Karp Algorithm)**
   - **Concept**: The Held-Karp algorithm (also known as the Bellman-Held-Karp algorithm) uses dynamic programming to store and reuse partial solutions, drastically reducing redundant calculations.
   - **Algorithm**:
     1. Define states that represent the minimum cost of reaching a subset of cities ending at a specific city.
     2. Use a recursive formula to build solutions for larger subsets based on previously computed results for smaller subsets.
     3. Reconstruct the optimal tour from the final results.
   - **Complexity**: \(O(n^2 \cdot 2^n)\), where \(n\) is the number of cities, which is significantly more efficient than brute force but still exponential.
   - **Advantages**: Reduces redundant calculations and can handle slightly larger instances than brute force.
   - **Limitations**: Still exponential in complexity, limiting practical use to fewer than about 30 cities.
   - **Reference**: Bellman, R. (1962). Dynamic programming treatment of the traveling salesman problem. *Journal of the ACM*, 9(1), 61-63. \
     Held, M., & Karp, R. M. (1962). A dynamic programming approach to sequencing problems. *Journal of the Society for Industrial and Applied Mathematics*, 10(1), 196-210.

---

### 3. **Branch and Bound**
   - **Concept**: Branch and Bound is a systematic approach that partitions the problem into smaller subproblems (branching) and uses bounds to eliminate paths that cannot improve upon the current best solution.
   - **Algorithm**:
     1. Start with an initial bound based on a relaxed version of the TSP (e.g., using Minimum Spanning Tree or Assignment Problem).
     2. Create branches by exploring routes and updating bounds.
     3. Prune branches that exceed the current best solution.
   - **Complexity**: In the worst case, \(O(n!)\), though practical performance is often much better due to effective pruning.
   - **Advantages**: Provides optimal solutions for small to medium instances and can reduce the search space significantly.
   - **Limitations**: Becomes computationally expensive as the number of cities increases.
   - **Reference**: Little, J. D., Murty, K. G., Sweeney, D. W., & Karel, C. (1963). An algorithm for the traveling salesman problem. *Operations Research*, 11(6), 972-989.

---

### 4. **Cutting Planes (Branch and Cut)**
   - **Concept**: Branch and Cut is a combination of Branch and Bound with cutting planes. Cutting planes are additional constraints added to the linear programming (LP) relaxation of the TSP to help eliminate fractional solutions.
   - **Algorithm**:
     1. Formulate the TSP as a linear program.
     2. Solve the relaxed problem without integer constraints.
     3. If the solution is not integer, add "cuts" to the LP model to eliminate infeasible solutions.
     4. Repeat until an integer solution is achieved or no more cuts can be found.
   - **Complexity**: Depends on the number of cuts needed; typically much better than Branch and Bound alone.
   - **Advantages**: One of the most efficient exact methods for TSP, especially when used with state-of-the-art TSP solvers.
   - **Limitations**: Complex to implement and requires effective methods for generating cuts.
   - **Reference**: Padberg, M., & Rinaldi, G. (1990). An efficient algorithm for the minimum capacity cut problem. *Mathematical Programming*, 47(1-3), 19-36. \
     Grötschel, M., & Padberg, M. W. (1985). Polyhedral theory and exact algorithms for the symmetric traveling salesman problem. *Mathematical Programming Studies*, 12, 43-60.

---

### 5. **Integer Linear Programming (ILP) Formulation**
   - **Concept**: TSP can be formulated as an integer linear program (ILP) where binary variables represent whether a route between two cities is included in the solution.
   - **Algorithm**:
     1. Define binary variables \(x_{ij}\) to represent if a path between cities \(i\) and \(j\) is part of the solution.
     2. Use the distance matrix as the objective function to minimize total travel cost.
     3. Apply constraints to ensure each city is visited exactly once and that no subtours exist.
   - **Common Formulation**:
     - Objective: Minimize \(\sum_{i=1}^n \sum_{j=1}^n d_{ij} x_{ij}\)
     - Constraints: 
       - Each city has exactly one incoming and one outgoing path.
       - Subtour elimination constraints (e.g., using Miller-Tucker-Zemlin or similar formulations).
   - **Advantages**: Leverages well-developed ILP solvers like Gurobi, CPLEX, and GLPK, allowing for moderately large instances.
   - **Limitations**: Can be memory and computation-intensive, especially for larger TSP instances.
   - **Reference**: Dantzig, G. B., Fulkerson, D. R., & Johnson, S. M. (1954). Solution of a large-scale traveling-salesman problem. *Journal of the Operations Research Society of America*, 2(4), 393-410.

---

### 6. **Branch and Price**
   - **Concept**: Branch and Price combines Branch and Bound with column generation (pricing) to solve a large-scale ILP formulation more efficiently. Columns, representing paths, are generated dynamically rather than included all at once.
   - **Algorithm**:
     1. Start with a relaxed version of the ILP formulation that contains only a subset of the paths (columns).
     2. Use a pricing subproblem to generate new paths that could potentially improve the objective.
     3. Branch on variables as in Branch and Bound, while generating new columns as needed.
   - **Complexity**: Highly variable, depending on the effectiveness of branching and pricing.
   - **Advantages**: Efficient for complex TSP variants and vehicle routing problems with additional constraints.
   - **Limitations**: Complex to implement and generally used for TSP with additional constraints, not basic TSP.
   - **Reference**: Desaulniers, G., Desrosiers, J., & Solomon, M. M. (Eds.). (2005). *Column Generation*. Springer.

---

### Summary of Exact Algorithms for TSP

| Algorithm           | Type               | Complexity        | Best for Instance Sizes | Key Advantage                          | Key Limitation                      |
|---------------------|--------------------|-------------------|-------------------------|---------------------------------------|-------------------------------------|
| Brute Force         | Exhaustive Search  | $(O((n-1)!))$    | Very small (<10 cities) | Simple and guarantees optimal solution| Impractical for large $(n)$         |
| Dynamic Programming | Recursive & Memory | $(O(n^2.2^n))$ | Small to medium (<30)  | Avoids redundant calculations         | Still exponential                   |
| Branch and Bound    | Recursive          | Variable (up to $(n!)$ ) | Small to medium (<50)  | Prunes large portions of search space| Computationally expensive           |
| Branch and Cut      | Mixed Recursive/LP | Variable         | Medium to large         | State-of-the-art for many TSP solvers| Complex to implement                |
| ILP Formulation     | LP-based           | Variable         | Medium to large         | Leverages powerful ILP solvers       | Memory/computation intensive        |
| Branch and Price    | Column Generation  | Variable         | Large, constrained TSP  | Efficient for TSP with constraints   | Implementation complexity           |

---
