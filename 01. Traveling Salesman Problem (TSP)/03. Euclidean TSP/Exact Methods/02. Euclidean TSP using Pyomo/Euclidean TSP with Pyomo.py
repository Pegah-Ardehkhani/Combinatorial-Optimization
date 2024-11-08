#!pip install pyomo
#!apt-get install -y -qq glpk-utils
import matplotlib.pyplot as plt
from pyomo.environ import *
import numpy as np
import math

def euclidean_distance(point1, point2):
    """Calculate Euclidean distance between two points in 2D space."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def generate_distance_matrix(points):
    """Generate a distance matrix for the given list of points."""
    n = len(points)
    distance_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distance_matrix[i][j] = euclidean_distance(points[i], points[j])
    return distance_matrix

def solve_euclidean_tsp_with_pyomo(city_points, show_route=True):
    """
    Solve the Euclidean Traveling Salesman Problem (TSP) using linear programming with Pyomo.

    Parameters:
    - city_points (dict): Dictionary of city labels and (x, y) coordinates, e.g., {'A': (0, 0), 'B': (2, 3)}.
    - show_route (bool): If True, displays a plot of the optimal route after solving the TSP. Defaults to True.
    - show_model (bool): If True, prints the linear programming model used to solve the TSP. Defaults to False.
    """

    # Extract points and labels
    labels = list(city_points.keys())
    points = list(city_points.values())

    # Generate distance matrix from points
    distance_matrix = generate_distance_matrix(points)
    n = len(distance_matrix)

    # Create Pyomo model
    model = ConcreteModel()

    # Define sets
    model.Cities = RangeSet(1, n)

    # Define variables
    model.x = Var(model.Cities, model.Cities, domain=Binary, initialize=0)
    model.u = Var(model.Cities, within=NonNegativeReals, bounds=(0, n-1))

    # Objective function: Minimize total distance
    model.objective = Objective(
        expr=sum(distance_matrix[i-1][j-1] * model.x[i, j] for i in model.Cities for j in model.Cities if i != j),
        sense=minimize
    )

    # Constraints
    # 1. Each city has exactly one outgoing edge
    model.outflow = ConstraintList()
    for i in model.Cities:
        model.outflow.add(sum(model.x[i, j] for j in model.Cities if i != j) == 1)

    # 2. Each city has exactly one incoming edge
    model.inflow = ConstraintList()
    for j in model.Cities:
        model.inflow.add(sum(model.x[i, j] for i in model.Cities if i != j) == 1)

    # 3. Subtour elimination constraints (Miller-Tucker-Zemlin constraints)
    model.subtour = ConstraintList()
    for i in range(2, n+1):
        for j in range(2, n+1):
            if i != j:
                model.subtour.add(model.u[i] - model.u[j] + n * model.x[i, j] <= n - 1)

    # Solve the model
    result = SolverFactory('glpk').solve(model)

    # Retrieve and print the solution
    if result.solver.status == SolverStatus.ok and result.solver.termination_condition == TerminationCondition.optimal:
        # Find the tour by starting from city 1 and following the path
        tour = []
        current_city = 1
        visited_cities = set([current_city])

        while len(visited_cities) < n:
            for j in range(1, n+1):
                if current_city != j and model.x[current_city, j].value == 1:
                    tour.append((current_city, j))
                    visited_cities.add(j)
                    current_city = j
                    break

        # Add the last leg returning to the starting city
        for j in range(1, n+1):
            if current_city != j and model.x[current_city, j].value == 1:
                tour.append((current_city, j))
                break

        # Convert tour from numeric indices to city labels
        labeled_tour = [(labels[i - 1], labels[j - 1]) for i, j in tour]

        # Print the results in the specified format
        print("Optimal Total Distance:", model.objective(), "\n")
        print("Optimal Tour:", labeled_tour)

        # Show the Optimal Route if show_route is set to True
        if show_route:
            plot_optimal_route(city_points, labeled_tour, model.objective())

    else:
        print("No optimal solution found.")
        return None

def plot_optimal_route(city_points, optimal_tour, total_distance):
    """
    Plots the optimal route based on the Euclidean points and labels.

    Parameters:
    - city_points (dict): Dictionary of city labels and (x, y) coordinates.
    - optimal_tour (list of tuples): Optimal path with labels, e.g., [('A', 'C'), ('C', 'D'), ('D', 'B'), ('B', 'A')].
    - total_distance (float): Total distance of the optimal tour.
    """
    ordered_points = [city_points[optimal_tour[0][0]]]
    for _, next_city in optimal_tour:
        ordered_points.append(city_points[next_city])

    # Extract x and y coordinates of the ordered points
    x_coords = [point[0] for point in ordered_points]
    y_coords = [point[1] for point in ordered_points]

    # Plotting the route
    plt.figure(figsize=(8, 8))
    plt.plot(x_coords, y_coords, marker='o', color='blue', linewidth=2)
    plt.title(f"Optimal TSP Route\nTotal Distance: {total_distance:.2f}")

    # Annotate cities with labels
    for label, (x, y) in city_points.items():
        plt.text(x, y, label, color="red", fontsize=14, ha="center", va="center",
                 bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))

    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.show()

# Example usage
if __name__ == "__main__":
    city_points = {'A': (0, 0), 'B': (2, 3), 'C': (5, 4), 'D': (6, 1), 'E': (4,2), 'F': (4,1)}
    solve_euclidean_tsp_with_pyomo(city_points, show_route=True)