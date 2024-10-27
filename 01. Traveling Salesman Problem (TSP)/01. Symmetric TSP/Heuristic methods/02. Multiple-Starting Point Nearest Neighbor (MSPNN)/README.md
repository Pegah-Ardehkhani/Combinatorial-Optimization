# Multiple-Starting Point Nearest Neighbor (MSPNN) Heuristic

The **Multiple-Starting Point Nearest Neighbor (MSPNN)** heuristic is an approach for finding an approximate solution to the **Traveling Salesman Problem (TSP)**. TSP is a classic optimization problem where the goal is to find the shortest possible route that visits each city exactly once and returns to the starting city.

The MSPNN heuristic builds upon the traditional Nearest Neighbor (NN) heuristic by running the NN algorithm from each possible starting city and selecting the best route. This improves the quality of the solution, as the NN heuristic is sensitive to the starting city and can yield different results depending on the initial choice.

---

## Algorithm Details

The algorithm works as follows:
1. **Loop through each city as a starting point**:
   - For each city, run the Nearest Neighbor heuristic, building a route by choosing the nearest unvisited city at each step.
   - Compute the total distance for each resulting tour.
   
2. **Select the shortest tour**:
   - Track the shortest tour among all possible starting cities and use it as the final solution.
   
3. **Optional Display**:
   - Print the best route found along with the total distance.
   - Optionally, display all routes and distances computed for each starting point to compare performance.

---

## Key Features

- **Multiple Starting Points**: By considering every city as a starting point, MSPNN addresses the NN heuristic's limitation of sensitivity to the initial city, often leading to shorter tours.
- **Improved Solution Quality**: The best tour among all starting points is selected, increasing the likelihood of a solution closer to the optimal.
- **Efficient**: Although MSPNN is computationally more intensive than a single NN run, it remains fast enough for moderately large TSP instances, making it suitable for scenarios where an approximate solution is sufficient.

---

## Parameters

- **`distance_matrix`**: A 2D list or numpy array representing the pairwise distances between cities.
- **`show_route`** (bool, optional): Displays a plot of the best route found if set to `True`.
- **`show_other_routes`** (bool, optional): Prints each route and total distance from every starting point if set to `True`.

## Usage Example

```python
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Solve the TSP with MSPNN
solve_tsp_with_MSPNN(distance_matrix, show_route=True, show_other_routes=True)
```

---

## Advantages and Limitations

### Advantages
- **Enhanced Solution Quality**: By examining all starting points, MSPNN typically provides a better solution than the single NN heuristic.
- **Simple to Implement**: MSPNN retains the simplicity of the Nearest Neighbor approach while adding minimal complexity.
- **Visualization**: Optional plotting of the best route provides a clear view of the resulting tour.

### Limitations
- **Increased Computation**: For large instances, the need to repeat the NN heuristic from each city adds to the computation time.
- **Still an Approximation**: While often effective, MSPNN does not guarantee the shortest possible tour, especially for complex city distributions.

---

## Conclusion

The **Multiple-Starting Point Nearest Neighbor (MSPNN)** heuristic is a straightforward yet effective improvement on the classic Nearest Neighbor heuristic for TSP. By evaluating multiple starting points, MSPNN yields higher-quality solutions while maintaining computational efficiency, making it a valuable tool for real-world TSP applications where exact solutions are not feasible.
