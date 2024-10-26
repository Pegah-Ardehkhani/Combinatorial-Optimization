#!pip install pyomo
#!apt-get install -y -qq glpk-utils
import matplotlib.pyplot as plt
import numpy as np
from pyomo.environ import *

def solve_tsp_with_pyomo(distance_matrix, show_route=True):
    # Get the number of cities
    n = len(distance_matrix)

    # Create a Pyomo model
    model = ConcreteModel()

    # Sets for cities
    model.cities = RangeSet(1, n)

    # Decision variables: binary variable x[i,j] to indicate if the route goes from city i to city j
    model.x = Var(model.cities, model.cities, domain=Binary)

    # Auxiliary variables for subtour elimination (MTZ formulation)
    model.u = Var(model.cities, bounds=(0, n), domain=NonNegativeReals)

    # Objective function: Minimize the total travel distance
    model.objective = Objective(
        expr=sum(distance_matrix[i-1][j-1] * model.x[i, j] for i in model.cities for j in model.cities if i != j),
        sense=minimize
    )

    # Constraints
    # 1. Each city must have exactly one outgoing edge
    model.outflow_constraints = ConstraintList()
    for i in model.cities:
        model.outflow_constraints.add(sum(model.x[i, j] for j in model.cities if i != j) == 1)

    # 2. Each city must have exactly one incoming edge
    model.inflow_constraints = ConstraintList()
    for j in model.cities:
        model.inflow_constraints.add(sum(model.x[i, j] for i in model.cities if i != j) == 1)

    # 3. Subtour elimination constraints (MTZ constraints)
    model.subtour_constraints = ConstraintList()
    for i in range(2, n+1):
        for j in range(2, n+1):
            if i != j:
                model.subtour_constraints.add(model.u[i] - model.u[j] + n * model.x[i, j] <= n - 1)

    # Solve the model using an available solver
    result = SolverFactory('glpk').solve(model)

    # Check if an optimal solution was found
    if result.solver.status == SolverStatus.ok and result.solver.termination_condition == TerminationCondition.optimal:
        # Retrieve the optimal tour
        tour = []
        current_city = 1
        visited_cities = {current_city}

        while len(visited_cities) < n:
            for j in model.cities:
                if current_city != j and value(model.x[current_city, j]) == 1:
                    tour.append((current_city, j))
                    visited_cities.add(j)
                    current_city = j
                    break

        # Add the last leg returning to the starting city
        for j in model.cities:
            if current_city != j and value(model.x[current_city, j]) == 1:
                tour.append((current_city, j))
                break

        # Print results in the specified format
        total_distance = value(model.objective)
        print("Optimal Total Distance:", total_distance, "\n")
        print("Optimal Tour:", tour, "\n")

        # Show the optimal route if show_route is set to True
        if show_route:
            plot_optimal_route_linear(tour, total_distance)

    else:
        print("No optimal solution found.")
        return None

def plot_optimal_route_linear(optimal_tour, total_distance):
    """
    Plots the optimal route in a line for the TSP.

    Parameters:
    - optimal_tour (list of tuples): Optimal path, e.g., [(1, 3), (3, 4), (4, 2), (2, 1)].
    - total_distance (float): Total distance of the optimal tour.
    """
    # Extract the order of cities from the optimal tour
    ordered_cities = [optimal_tour[0][0]]  # Start with the first city in the tour
    for _, next_city in optimal_tour:
        ordered_cities.append(next_city)

    # Generate positions along a line for each city in the order of the optimal tour
    x_coords = list(range(1, len(ordered_cities) + 1))
    y_coords = [1] * len(ordered_cities)  # Set a constant y-coordinate for all cities to place them in a line

    # Create a figure
    plt.figure(figsize=(10, 2))
    plt.title(f"Optimal TSP Route (Linear View)\nTotal Distance: {total_distance}")

    # Plot each city in the order of the optimal tour
    plt.scatter(x_coords, y_coords, color='blue', s=100, zorder=5)

    # Annotate each city with its index according to the ordered tour
    for i, (x, y) in enumerate(zip(x_coords, y_coords)):
        plt.text(x, y + 0.05, f'{ordered_cities[i]}', ha='center', color='darkred')

    # Plot the route by drawing lines in the order of the optimal tour
    for idx in range(len(ordered_cities) - 1):
        plt.plot([x_coords[idx], x_coords[idx + 1]], [1, 1], color='green', linestyle='-', linewidth=2)

    # Set plot limits and remove the y-axis for a clean linear view
    plt.ylim(0.8, 1.2)
    plt.xlabel("Cities")
    plt.gca().get_yaxis().set_visible(False)
    plt.gca().get_xaxis().set_visible(False)
    plt.show()

# Example usage
if __name__ == "__main__":
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    solve_tsp_with_pyomo(distance_matrix, show_route=True)