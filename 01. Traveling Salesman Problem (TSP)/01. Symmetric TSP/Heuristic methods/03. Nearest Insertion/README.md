# Nearest Insertion

The **Nearest Insertion** heuristic is a constructive approach for solving the Traveling Salesman Problem (TSP). It begins by selecting an initial "seed" tour, usually involving a few starting cities. The algorithm then iteratively inserts the remaining cities one by one into the tour at the position that results in the smallest possible increase in the tour's total length.

### Steps of the Nearest Insertion Heuristic:
1. **Start Tour Initialization**: Begin with a minimal tour, often just a single city or the two closest cities.
2. **Find Nearest City**: Identify the unvisited city that is nearest to any city already in the current tour.
3. **Optimal Insertion**: Insert this nearest unvisited city into the tour at the position that adds the least distance to the overall tour length.
4. **Repeat**: Continue this process until all cities have been inserted.
5. **Completion**: Once all cities are included in the tour, return to the starting city to complete the route.

This method balances the greedy choice of the nearest unvisited city with strategic insertion, aiming to maintain a relatively short path. The Nearest Insertion heuristic is generally faster than exact algorithms, making it useful for quickly approximating solutions to the TSP for medium-sized datasets, although it may not yield an optimal solution for every case.

---

### Example of Nearest Insertion Heuristic

Consider a TSP instance with 4 cities and the following distance matrix:

|         | City 1 | City 2 | City 3 | City 4 |
|---------|--------|--------|--------|--------|
| **City 1** | 0      | 10     | 15     | 20     |
| **City 2** | 10     | 0      | 35     | 25     |
| **City 3** | 15     | 35     | 0      | 30     |
| **City 4** | 20     | 25     | 30     | 0      |

Let’s apply the **Nearest Insertion** heuristic to this matrix, starting from City 1.

#### Step 1: Initialize with Start City
- Start at **City 1**.
- Find the closest city to City 1, which is **City 2** with a distance of 10.
- **Initial tour**: `1 → 2 → 1`
- **Total distance so far**: 10 (for the first segment)

#### Step 2: Insert the Nearest City
- Look for the nearest unvisited city to any city in the current tour (1 → 2).
  - The closest city to City 1 is City 3 with a distance of 15.
  - The closest city to City 2 is City 4 with a distance of 25.
- **Choose City 3** (since 15 < 25).
- Insert City 3 between City 1 and City 2 to minimize tour length increase.
- **Updated tour**: `1 → 3 → 2 → 1`
- **Total distance so far**: 10 (City 1 to City 2) + 15 (City 1 to City 3) + 35 (City 3 to City 2) = 60

#### Step 3: Insert Remaining City
- The only unvisited city left is **City 4**.
  - Insert City 4 at the position that causes the least increase in distance.
  - The best insertion point is between City 2 and City 1.
- **Final tour**: `1 → 3 → 2 → 4 → 1`
- **Total distance**: 10 (1 to 2) + 15 (1 to 3) + 35 (3 to 2) + 25 (2 to 4) = 85
