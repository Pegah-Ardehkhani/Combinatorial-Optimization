# Farthest Insertion

The **Farthest Insertion** heuristic is a constructive approach for solving the Traveling Salesman Problem (TSP). It starts by selecting an initial tour with the starting city and the farthest unvisited city from it. The algorithm then iteratively inserts the farthest remaining city into the current tour at the position that results in the smallest possible increase in the tour's total length. This approach spreads out the tour by covering distant cities first, which can lead to a more balanced route and better solutions for certain geographical layouts.

### Steps of the Farthest Insertion Heuristic:
1. **Start Tour Initialization**: Begin with a minimal tour that includes the starting city and the farthest city from it.
2. **Find Farthest City**: Identify the unvisited city that is farthest from any city already in the current tour.
3. **Optimal Insertion**: Insert this farthest unvisited city into the tour at the position that adds the least distance to the overall tour length.
4. **Repeat**: Continue this process until all cities have been inserted.
5. **Completion**: Once all cities are included in the tour, return to the starting city to complete the route.

This method focuses on expanding the tour outward by selecting cities based on maximum distance, which can sometimes yield better solutions than nearest-insertion approaches.

---

### Example of Farthest Insertion Heuristic

Consider a TSP instance with 4 cities and the following distance matrix:

|         | City 1 | City 2 | City 3 | City 4 |
|---------|--------|--------|--------|--------|
| **City 1** | 0      | 10     | 15     | 20     |
| **City 2** | 10     | 0      | 35     | 25     |
| **City 3** | 15     | 35     | 0      | 30     |
| **City 4** | 20     | 25     | 30     | 0      |

Let’s apply the **Farthest Insertion** heuristic to this matrix, starting from City 1.

#### Step 1: Initialize with Start City
- Start at **City 1**.
- Find the farthest city from City 1, which is **City 4** with a distance of 20.
- **Initial tour**: `1 → 4 → 1`
- **Total distance so far**: 20

#### Step 2: Insert the Farthest City
- Look for the farthest unvisited city from any city in the current tour (1 → 4).
  - The farthest city from City 1 is City 3 with a distance of 15.
  - The farthest city from City 4 is City 3 with a distance of 30.
- **Choose City 3** (since 30 > 15).
- Insert City 3 at the position in the current tour (1 → 4) that minimizes the increase in total distance.
- **Updated tour**: `1 → 3 → 4 → 1`
- **Total distance so far**: 15 (City 1 to City 3) + 30 (City 3 to City 4) + 20 (City 4 to City 1) = 65.

#### Step 3: Insert Remaining City
- The only unvisited city left is **City 2**.
  - Insert City 2 at the position that causes the least increase in distance.
  - The best insertion point is between City 1 and City 3.
- **Final tour**: `1 → 2 → 3 → 4 → 1`
- **Total distance**: 10 (1 to 2) + 35 (2 to 3) + 30 (3 to 4) + 20 (4 to 1) = 95.
