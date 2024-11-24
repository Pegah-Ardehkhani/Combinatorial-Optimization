# Multi-Depot Multi-Salesman Problem (MDMSP)

The **Multi-Depot Multi-Salesman Problem (MDMSP)** is a generalized version of the Traveling Salesman Problem (TSP) that involves multiple depots and multiple salesmen. It requires determining the optimal routes for multiple salesmen who each start from one of several depots, visit a subset of cities, and return to one of the depots. The objective is to minimize the total travel cost or distance while ensuring every city is visited exactly once.

---

## Key Characteristics of MDMSP

1. **Multiple Depots**:
   - The problem has several starting and ending points (depots), typically representing warehouses, hubs, or facilities.

2. **Multiple Salesmen**:
   - A predefined number of salesmen, each starting and ending at a depot, are assigned to visit all cities.

3. **City Assignment**:
   - Each city must be visited exactly once by one of the salesmen.

4. **Objective**:
   - Minimize the total travel cost, distance, or time across all routes.

5. **Flexible Routing**:
   - Salesmen can start and end at different depots or the same depot, depending on constraints and objectives.

6. **Constraints**:
   - Routes must be contiguous (no subtours).
   - Depots are the only valid starting and ending points for routes.

---

## Problem Formulation

### Inputs
1. **Distance Matrix**:
   - A matrix representing distances or costs between all locations (depots + cities).
2. **Depots**:
   - A list of depot locations.
3. **Cities**:
   - A list of cities that must be visited.
4. **Number of Salesmen**:
   - Total number of available salesmen.

### Decision Variables
1. $( x_{i,j}^k )$: A binary variable where $( x_{i,j}^k = 1 )$ if salesman $( k )$ travels from location $( i )$ to $( j )$, and $( 0 )$ otherwise.
2. $( u_i^k )$: A continuous variable used to eliminate subtours.

### Objective Function
Minimize the total distance traveled by all salesmen:

$\text{Minimize } \sum_{k=1}^{K} \sum_{i=1}^{N} \sum_{j=1}^{N} d_{i,j} \cdot x_{i,j}^k$

where:
- $( K )$: Number of salesmen.
- $( N )$: Total number of locations.
- $( d_{i,j} )$: Distance between locations $( i )$ and $( j )$.

### Constraints
1. **City Visit**:
   Each city must be visited exactly once:
   
   $\sum_{k=1}^{K} \sum_{i=1}^{N} x_{i,j}^k = 1, \quad \forall j \in \text{Cities}$

2. **Depot Connections**:
   Each salesman must start and end at a depot:
   
   $\sum_{j \in \text{Cities}} x_{\text{depot}, j}^k \leq 1, \quad \forall k$
   
   $\sum_{i \in \text{Cities}} x_{i, \text{depot}}^k \leq 1, \quad \forall k$

4. **Subtour Elimination**:
   Eliminate disconnected routes using Miller-Tucker-Zemlin (MTZ) constraints:
   
   $u_i^k - u_j^k + N \cdot x_{i,j}^k \leq N-1, \quad \forall i, j \in \text{Cities}, i \neq j$

---

## Example of MDMSP

### Input
- **Distance Matrix**:
  ```
  [
      [0, 10, 15, 20, 5],  # Depot 1
      [10, 0, 35, 25, 10],  # City 1
      [15, 35, 0, 30, 15],  # City 2
      [20, 25, 30, 0, 20],  # City 3
      [5, 10, 15, 20, 0]   # Depot 2
  ]
  ```
- **Depots**: [1, 5] (Depot 1 and Depot 2).
- **Number of Salesmen**: 2.

### Output
- **Optimal Routes**:
  1. Salesman 1: Depot 1 -> City 1 -> City 3 -> Depot 1.
  2. Salesman 2: Depot 2 -> City 2 -> Depot 2.
- **Total Distance**: 85 units.

---

## Applications of MDMSP

1. **Logistics and Distribution**:
   - Assigning delivery routes to trucks based at different warehouses to serve customers efficiently.

2. **Field Service Scheduling**:
   - Scheduling maintenance teams to visit multiple locations, starting and ending at different regional hubs.

3. **Transportation Planning**:
   - Optimizing routes for buses, shuttles, or delivery drones operating from multiple depots.

4. **Supply Chain Management**:
   - Determining optimal delivery routes for goods dispatched from multiple distribution centers.

5. **Military and Emergency Operations**:
   - Planning routes for patrols, rescue missions, or supply drops from multiple bases.

---

## Limitations of MDMSP

1. **Complexity**:
   - MDMSP is NP-hard, making exact solutions computationally expensive for large instances.

2. **Scalability**:
   - As the number of depots, cities, and salesmen grows, the problem becomes intractable without heuristics or approximation algorithms.

3. **Dynamic Conditions**:
   - Real-world scenarios often involve dynamic factors (e.g., traffic, weather), which are not captured in static formulations.

4. **Heterogeneous Resources**:
   - Many formulations assume homogeneous salesmen and vehicles, which may not reflect real-world diversity in capacity or cost.

5. **Subtour Elimination**:
   - Ensuring feasible routes without subtours requires additional constraints, increasing computational overhead.

---

## Conclusion

The Multi-Depot Multi-Salesman Problem (MDMSP) is a versatile and challenging optimization problem with applications in logistics, transportation, and beyond. While its complexity poses challenges, advances in algorithms and computational power have made it feasible to solve practical instances using exact or heuristic methods.
