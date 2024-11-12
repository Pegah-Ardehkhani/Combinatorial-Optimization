# Standard Vehicle Routing Problem (VRP)

<p align="center"> 
  <img width="500" height="400" src="https://upload.wikimedia.org/wikipedia/commons/2/2b/Figure_illustrating_the_vehicle_routing_problem.png"> 
</p>

The **Standard Vehicle Routing Problem (VRP)** involves finding the optimal set of routes for a fleet of vehicles to deliver goods from a central depot to a set of customers. The objective is to minimize the total travel distance or cost.

#### Characteristics of Standard VRP

1. **Single Depot**: All vehicles begin and end their routes at a central depot.
2. **Objective**: Minimize the total distance or cost for all routes.
3. **Simplification**: Unlike the CVRP, there are no vehicle capacity constraints to limit route planning.

#### Problem Description

- **Input**:
  - A central depot where all vehicles start and end their routes.
  - A set of customers that need to be visited.
  - A fleet of vehicles.
  - A distance matrix representing travel costs or distances between each location (depot and customers).

- **Output**:
  - Optimal routes for each vehicle that ensure:
    - Each customer is visited exactly once by one vehicle.
    - The overall travel distance or cost is minimized.

### Mathematical Model for Standard VRP

#### Decision Variables
- $( x_{ij}^k )$: Binary variable, where $( x_{ij}^k = 1 )$ if vehicle $( k )$ travels from location $( i )$ to $( j )$; 0 otherwise.
- $( u_i )$: Auxiliary variables to help eliminate sub-tours.

#### Parameters
- $( w_{ij} )$: Distance or cost associated with traveling from location $( i )$ to $( j )$.
- $( K )$: Set of available vehicles.

#### Objective Function
Minimize the total travel distance or cost:

$\text{Minimize } \sum_{k \in K} \sum_{(i, j)} w_{ij} \cdot x_{ij}^k$

#### Constraints
1. **Customer Visit Constraint**:
   - Each customer is visited exactly once by a vehicle.
   $\sum_{k \in K} \sum_{i \neq j} x_{ij}^k = 1, \quad \forall j \neq \text{depot}$

2. **Flow Conservation**:
   - Each vehicle that visits a customer must also leave it, maintaining route continuity.
   $\sum_{j} x_{ij}^k = \sum_{j} x_{ji}^k, \quad \forall k \in K, \forall i \neq \text{depot}$

3. **Subtour Elimination**:
   - Auxiliary variables \( u_i \) ensure that no sub-tour forms.
   $u_i - u_j + n \cdot x_{ij}^k \leq n - 1, \quad \forall i, j \neq \text{depot}, i \neq j, k \in K$
   where \( n \) is the number of locations.

### Solution Techniques for Standard VRP
- **Exact Methods**: For smaller instances, integer programming and branch-and-bound methods are feasible for finding optimal solutions.
- **Heuristic and Metaheuristic Methods**: For larger problems, methods like the Clarke-Wright Savings algorithm, Genetic Algorithms, Simulated Annealing, and Ant Colony Optimization are commonly applied to achieve near-optimal solutions efficiently.

### Applications of Standard VRP
VRP has broad applications in fields where optimal route planning is essential, such as:
- Delivery services.
- Public transportation planning.
- Maintenance and service scheduling.

This simplified VRP serves as the foundation for various VRP extensions, including those that incorporate additional constraints, such as vehicle capacity in the CVRP, time windows, and multi-depot considerations.
