# Capacitated Vehicle Routing Problem (CVRP)

The **standard Vehicle Routing Problem (VRP)**, also known as the **Capacitated Vehicle Routing Problem (CVRP)**, is the basic version of the VRP where a fleet of vehicles with fixed capacity must deliver goods from a central depot to a set of customers while minimizing the total travel distance or cost.

### Characteristics of Standard VRP (CVRP)

1. **Single Depot**: All vehicles start and end their routes at a single, central depot.
2. **Customer Demands**: Each customer has a specific demand that must be fulfilled.
3. **Vehicle Capacity Constraint**: Each vehicle has a fixed capacity, and the sum of the demands on a vehicle’s route cannot exceed this capacity.
4. **Objective**: Minimize the total distance or cost for all routes.

### Problem Description

- **Input**:
  - A central depot where all vehicles begin and end their routes.
  - A set of customers, each with a demand (amount of goods they need).
  - A fleet of vehicles, each with a specified capacity.
  - A distance matrix representing the travel cost or distance between each pair of locations (depot and customers).

- **Output**:
  - Optimal routes for each vehicle, such that:
    - Each customer is visited exactly once by one vehicle.
    - Total demand on each route does not exceed vehicle capacity.
    - The overall travel distance or cost is minimized.

### Mathematical Model for Standard VRP

#### Decision Variables
- $( x_{ij}^k )$: Binary variable, where $( x_{ij}^k = 1 )$ if vehicle $( k )$ travels from location $( i )$ to $( j )$; 0 otherwise.
- $( u_i )$: Auxiliary variables to help eliminate sub-tours.

#### Parameters
- $( w_{ij} )$: Distance or cost associated with traveling from location $( i )$ to $( j )$.
- $( Q )$: Capacity of each vehicle.
- $( d_i )$: Demand at each customer location $( i )$.
- $( K )$: Set of vehicles available.

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

3. **Vehicle Capacity Constraint**:
   - The sum of demands on each route cannot exceed the vehicle capacity.
   $\sum_{i} d_i \cdot x_{ij}^k \leq Q, \quad \forall k \in K$

4. **Subtour Elimination**:
   - Auxiliary variables \( u_i \) ensure that no sub-tour forms.
   $u_i - u_j + Q \cdot x_{ij}^k \leq Q - d_j, \quad \forall i, j \neq \text{depot}, i \neq j, k \in K$

### Solution Techniques for Standard VRP
The standard VRP can be solved using:
- **Exact Methods**: For small instances, integer programming and branch-and-bound algorithms can yield optimal solutions.
- **Heuristic and Metaheuristic Methods**: For large-scale problems, methods like the Clarke-Wright Savings algorithm, Genetic Algorithms, Simulated Annealing, and Ant Colony Optimization are commonly used for finding near-optimal solutions efficiently.

### Applications of Standard VRP
Standard VRP is widely used in logistics and transportation, including:
- Delivery route planning for e-commerce.
- Supply distribution for retail.
- Waste collection and recycling.

The standard VRP is the foundation for many VRP extensions, including those with additional constraints like time windows, multiple depots, and pickup and delivery.
