# -*- coding: utf-8 -*-
"""0-1 Knapsack with Pyomo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LVEqTBKHa3lMtnVO7Axpg8xw4bU32BXW
"""

# !pip install pyomo
# !apt-get install -y -qq glpk-utils
import matplotlib.pyplot as plt
from pyomo.environ import *

def solve_0_1knapsack_with_pyomo(values, weights, max_weight, show_plot=True):
    """
    Solve the 0/1 Knapsack Problem using Pyomo and plot the results.

    Parameters:
    - values (list of floats): List of item values.
    - weights (list of floats): List of item weights.
    - max_weight (float): Maximum weight capacity of the knapsack.
    - show_plot (bool): If True, displays a bar plot of selected and unselected items.
    """

    # Get the number of items
    n = len(values)

    # Initialize the model
    model = ConcreteModel()

    # Create index set for items
    model.item_set = RangeSet(1, n)

    # Parameters for values and weights
    model.item_values = Param(model.item_set, initialize={i + 1: values[i] for i in range(n)})
    model.item_weights = Param(model.item_set, initialize={i + 1: weights[i] for i in range(n)})

    # Decision variables x_i for each item (0 or 1)
    model.x = Var(model.item_set, domain=Binary)  # Binary decision variables

    # Objective function: Maximize the total value
    model.obj = Objective(expr=sum(model.item_values[i] * model.x[i] for i in model.item_set), sense=maximize)

    # Constraint: The total weight of selected items should not exceed max_weight
    model.weight_constraint = Constraint(expr=sum(model.item_weights[i] * model.x[i] for i in model.item_set) <= max_weight)

    # Solve the model using the GLPK solver (ensure GLPK is installed)
    solver = SolverFactory('glpk')
    result = solver.solve(model)

    # Retrieve and print the solution
    if result.solver.status == SolverStatus.ok and result.solver.termination_condition == TerminationCondition.optimal:
        selected_items = [i for i in model.item_set if value(model.x[i]) == 1]
        total_value = value(model.obj)
        total_weight = sum(model.item_weights[i] * value(model.x[i]) for i in model.item_set)

        print("Optimal Total Value:", total_value, "\n")
        print("Total Weight of Selected Items:", total_weight, "\n")
        print("Selected Items:", [i for i in selected_items], "\n")  # Indexes starting from 1

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
    colors = ['#afd30b' if (i + 1) in selected_items else '#d30b32' for i in range(n)]

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

    solve_0_1knapsack_with_pyomo(values, weights, max_weight, show_plot=True)