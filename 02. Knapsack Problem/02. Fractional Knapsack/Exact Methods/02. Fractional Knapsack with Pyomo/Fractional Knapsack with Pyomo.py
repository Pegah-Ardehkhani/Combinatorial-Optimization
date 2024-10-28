import matplotlib.pyplot as plt
from pyomo.environ import *

def solve_fractional_knapsack_with_pyomo(item_values, item_weights, max_weight, show_plot=True):
    """
    Solve the Fractional Knapsack Problem using linear programming with Pyomo and plot the results.

    Parameters:
    - item_values (list of floats): List of item values.
    - item_weights (list of floats): List of item weights.
    - max_weight (float): Maximum weight capacity of the knapsack.
    - show_model (bool): If True, prints the linear programming model used to solve the knapsack problem.
    - show_plot (bool): If True, displays a bar plot of value-to-weight ratios.
    """

    # Get the number of items
    n = len(item_values)

    # Initialize the model
    model = ConcreteModel()

    # Define sets
    model.I = RangeSet(n)  # Index set for items

    # Define parameters
    model.item_values = Param(model.I, initialize={i + 1: item_values[i] for i in range(n)})
    model.item_weights = Param(model.I, initialize={i + 1: item_weights[i] for i in range(n)})
    model.max_weight = Param(initialize=max_weight)

    # Define decision variables
    model.x = Var(model.I, within=NonNegativeReals, bounds=(0, 1))  # Fraction of each item

    # Objective function: Maximize the total value
    model.obj = Objective(expr=sum(model.item_values[i] * model.x[i] for i in model.I), sense=maximize)

    # Constraint: The total weight of selected items should not exceed max_weight
    model.weight_constraint = Constraint(expr=sum(model.item_weights[i] * model.x[i] for i in model.I) <= model.max_weight)

    # Solve the problem
    result = SolverFactory('glpk').solve(model)

    # Check if the solution is optimal
    if result.solver.termination_condition == TerminationCondition.optimal:
        total_value = model.obj()
        total_weight = sum(model.item_weights[i] * model.x[i].value for i in model.I)
        selected_items = [(i, model.x[i].value) for i in model.I if model.x[i].value > 0]  # Include fractions

        print("Optimal Total Value:", total_value, "\n")
        print("Total Weight of Selected Items:", total_weight, "\n")
        print("Selected Items (Index, Fraction):", selected_items, "\n")  # Indexes starting from 1

        # Plot the results if show_plot is set to True
        if show_plot:
            plot_knapsack_solution(item_values, item_weights, selected_items)
    else:
        print("No optimal solution found.")

def plot_knapsack_solution(values, weights, selected_items):
    """
    Plots the selected and unselected items in the fractional knapsack problem, showing value-to-weight ratios.

    Parameters:
    - values (list of floats): List of item values.
    - weights (list of floats): List of item weights.
    - selected_items (list of tuples): (Index, Fraction) of selected items.
    """
    n = len(values)
    item_indices = list(range(1, n + 1))  # Start items from index 1

    # Calculate value-to-weight ratios
    ratios = [values[i] / weights[i] for i in range(n)]

    # Define colors for selected vs. unselected items, with transparency for fractions
    colors = ['#afd30b' if any(i == item[0] for item in selected_items) else '#d30b32' for i in range(1, n + 1)]
    alphas = [next((item[1] for item in selected_items if item[0] == i), 1.0) for i in range(1, n + 1)]  # Default to full opacity

    # Create the bar plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the value-to-weight ratio with transparency for fractional selections
    bars = ax.bar(item_indices, ratios, color=colors)
    for bar, alpha in zip(bars, alphas):
        bar.set_alpha(alpha)

    ax.set_xticks(item_indices)  # Ensure x-axis has sequential indices (1, 2, 3, ...)
    ax.set_xlabel("Item Index")
    ax.set_ylabel("Value-to-Weight Ratio", color='black')
    ax.set_title("Fractional Knapsack Solution: Value-to-Weight Ratios (Green = Selected, Red = Unselected)")

    # Display value and weight on each bar
    for i in range(n):
        ax.text(item_indices[i], ratios[i] + 0.1, f"V:{values[i]} W:{weights[i]}", ha='center', fontsize=8)

    plt.show()

# Example usage
if __name__ == "__main__":
    values = [100, 280, 120, 300, 450, 130, 150, 200, 240, 160]
    weights = [10, 40, 20, 50, 60, 15, 25, 30, 45, 35]
    max_weight = 100

    solve_fractional_knapsack_with_pyomo(values, weights, max_weight, show_plot=True)