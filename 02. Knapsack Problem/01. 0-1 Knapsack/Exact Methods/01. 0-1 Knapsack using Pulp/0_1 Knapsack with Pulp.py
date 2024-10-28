# !pip install pulp
from pulp import *
import matplotlib.pyplot as plt

def solve_0_1knapsack_with_pulp(values, weights, max_weight, show_model=False, show_plot=True):
    """
    Solve the 0/1 Knapsack Problem using linear programming with PuLP and plot the results.

    Parameters:
    - values (list of floats): List of item values.
    - weights (list of floats): List of item weights.
    - max_weight (float): Maximum weight capacity of the knapsack.
    - show_model (bool): If True, prints the linear programming model used to solve the knapsack problem.
    - show_plot (bool): If True, displays a bar plot of selected and unselected items.
    """

    # Get the number of items
    n = len(values)

    # Initialize the problem
    knapsack0_1 = LpProblem("0-1_Knapsack_Problem", LpMaximize)

    # Create binary decision variables x_i for each item
    x = LpVariable.dicts("x", (i for i in range(n)), cat='Binary')

    # Objective function: Maximize the total value
    knapsack0_1 += lpSum(values[i] * x[i] for i in range(n)), "Total_Value"

    # Constraint: The total weight of selected items should not exceed max_weight
    knapsack0_1 += lpSum(weights[i] * x[i] for i in range(n)) <= max_weight, "Weight_Constraint"

    # Solve the problem
    knapsack0_1.solve()

    # Retrieve and print the solution
    if knapsack0_1.status == LpStatusOptimal:
        selected_items = [i for i in range(n) if value(x[i]) == 1]
        total_value = value(knapsack0_1.objective)
        total_weight = sum(weights[i] for i in selected_items)

        print("Optimal Total Value:", total_value, "\n")
        print("Total Weight of Selected Items:", total_weight, "\n")
        print("Selected Items:", [i + 1 for i in selected_items], "\n")  # Indexes starting from 1

        # Show the model summary if show_model is set to True
        if show_model:
            print("\nModel Summary:\n")
            print(knapsack0_1)

        # Plot the results if show_plot is set to True
        if show_plot:
            plot_knapsack_solution(values, weights, selected_items)
    else:
        print("No optimal solution found.")

def plot_knapsack_solution(values, weights, selected_items):
    """
    Plots the selected and unselected items in the knapsack problem, showing value-to-weight ratios.

    Parameters:
    - values (list of floats): List of item values.
    - weights (list of floats): List of item weights.
    - selected_items (list of int): Indices of selected items.
    """
    n = len(values)
    item_indices = list(range(1, n + 1))  # Start items from index 1

    # Calculate value-to-weight ratios
    ratios = [values[i] / weights[i] for i in range(n)]

    # Define colors for selected vs. unselected items
    colors = ['#afd30b' if i in selected_items else '#d30b32' for i in range(n)]

    # Create the bar plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the value-to-weight ratio
    ax.bar(item_indices, ratios, color=colors)
    ax.set_xticks(item_indices)  # Ensure x-axis has sequential indices (1, 2, 3, ...)
    ax.set_xlabel("Item Index")
    ax.set_ylabel("Value-to-Weight Ratio", color='black')
    ax.set_title("Knapsack Solution: Value-to-Weight Ratios (Green = Selected, Red = Unselected)")

    # Display value and weight on each bar
    for i in range(n):
        ax.text(item_indices[i], ratios[i] + 0.1, f"V:{values[i]} W:{weights[i]}", ha='center', fontsize=8)

    plt.show()

# Example usage
if __name__ == "__main__":
    values = [100, 280, 120, 300, 450, 130, 150, 200, 240, 160]
    weights = [10, 40, 20, 50, 60, 15, 25, 30, 45, 35]
    max_weight = 100

    solve_0_1knapsack_with_pulp(values, weights, max_weight, show_model=True, show_plot=True)