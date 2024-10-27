import numpy as np
import matplotlib.pyplot as plt

def solve_tsp_with_nearest_neighbor(distance_matrix, start=1, show_route=True):
    """
    Solve the TSP using the Nearest Neighbor heuristic.

    Parameters:
    - distance_matrix (2D list or numpy array): Matrix of distances between cities.
    - start (int): The starting city (1-based index). Defaults to City 1.
    - show_route (bool): Whether to display the route plot. Defaults to True.
    """
    # Convert to 1-based indexing for cities
    n = len(distance_matrix)
    unvisited = set(range(1, n + 1))  # Cities indexed from 1 to n
    tour = [start]  # Start from the specified city
    current_city = start
    unvisited.remove(current_city)
    total_distance = 0

    while unvisited:
        # Find the nearest unvisited city
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city - 1][city - 1])
        total_distance += distance_matrix[current_city - 1][next_city - 1]
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    # Return to the starting city
    total_distance += distance_matrix[current_city - 1][start - 1]
    tour.append(start)

    # Print results
    print("Total Distance:", total_distance, "\n")
    print("Tour:", tour, "\n")

    # Plot the route if show_route is True
    if show_route:
        plot_route_linear(tour, total_distance)

def plot_route_linear(tour, total_distance):
    """
    Plots the route in a line for the TSP.

    Parameters:
    - tour (list): The sequence of cities in the order visited, e.g., [1, 3, 4, 2, 1].
    - total_distance (float): Total distance of the tour.
    """
    # Generate positions along a line for each city in the order of the tour
    x_coords = list(range(1, len(tour) + 1))
    y_coords = [1] * len(tour)  # Constant y-coordinate for a linear view

    # Create a figure
    plt.figure(figsize=(10, 2))
    plt.title(f"Nearest Neighbor TSP Route (Linear View)\nTotal Distance: {total_distance}")

    # Plot each city in the order of the tour
    plt.scatter(x_coords, y_coords, color='blue', s=100, zorder=5)

    # Annotate each city with its index
    for i, (x, y) in enumerate(zip(x_coords, y_coords)):
        plt.text(x, y + 0.05, f'{tour[i]}', ha='center', color='darkred')

    # Draw lines between cities in the order of the tour
    for idx in range(len(tour) - 1):
        plt.plot([x_coords[idx], x_coords[idx + 1]], [1, 1], color='green', linestyle='-', linewidth=2)

    # Set plot limits and remove the y-axis for a clean linear view
    plt.ylim(0.8, 1.2)
    plt.xlabel("Cities")
    plt.gca().get_yaxis().set_visible(False)
    plt.gca().get_xaxis().set_visible(False)
    plt.show()


# Example usage
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Call the function with the option to display the route
solve_tsp_with_nearest_neighbor(distance_matrix, start=1, show_route=True)