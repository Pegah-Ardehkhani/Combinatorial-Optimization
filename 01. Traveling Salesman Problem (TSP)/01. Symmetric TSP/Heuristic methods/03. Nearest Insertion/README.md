# Nearest Insertion

The **Nearest Insertion** heuristic is a constructive approach for solving the Traveling Salesman Problem (TSP). It begins by selecting an initial "seed" tour, usually involving a few starting cities. The algorithm then iteratively inserts the remaining cities one by one into the tour at the position that results in the smallest possible increase in the tour's total length.

### Steps of the Nearest Insertion Heuristic:
1. **Start Tour Initialization**: Begin with a minimal tour, often just a single city or the two closest cities.
2. **Find Nearest City**: Identify the unvisited city that is nearest to any city already in the current tour.
3. **Optimal Insertion**: Insert this nearest unvisited city into the tour at the position that adds the least distance to the overall tour length.
4. **Repeat**: Continue this process until all cities have been inserted.
5. **Completion**: Once all cities are included in the tour, return to the starting city to complete the route.

This method balances the greedy choice of the nearest unvisited city with strategic insertion, aiming to maintain a relatively short path. The Nearest Insertion heuristic is generally faster than exact algorithms, making it useful for quickly approximating solutions to the TSP for medium-sized datasets, although it may not yield an optimal solution for every case.
