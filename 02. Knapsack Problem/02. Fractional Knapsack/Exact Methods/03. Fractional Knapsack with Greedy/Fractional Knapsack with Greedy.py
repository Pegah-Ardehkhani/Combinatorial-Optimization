import matplotlib.pyplot as plt

def solve_fractional_knapsack_with_greedy(values, weights, max_weight, show_plot=True):
    """
    Solve the Fractional Knapsack Problem using a greedy algorithm and plot the results.

    Parameters:
    - values (list of floats): List of item values.
    - weights (list of floats): List of item weights.
    - max_weight (float): Maximum weight capacity of the knapsack.
    - show_plot (bool): If True, displays a bar plot of selected and unselected items.
    """
    # Calculate the value-to-weight ratios and sort items by this ratio in descending order
    items = sorted(
        [(i, values[i], weights[i], values[i] / weights[i]) for i in range(len(values))],
        key=lambda x: x[3],
        reverse=True
    )

    total_value = 0
    total_weight = 0
    selected_items = []

    # Print item ratios
    print("Item | Value | Weight | Value-to-Weight Ratio")
    print("-----------------------------------------------")
    for i, value, weight, ratio in items:
        print(f"{i+1:>4} | {value:>5} | {weight:>6} | {ratio:.2f}")

    # Select items based on greedy criteria, allowing fractional selections
    for i, value, weight, ratio in items:
        if total_weight + weight <= max_weight:
            # Take the whole item
            selected_items.append((i + 1, 1.0))  # 1.0 indicates full selection of the item
            total_value += value
            total_weight += weight
        else:
            # Take the fraction of the item that fits
            fraction = (max_weight - total_weight) / weight
            selected_items.append((i + 1, fraction))
            total_value += value * fraction
            total_weight += weight * fraction
            break  # Knapsack is full

    print("\nTotal Value of Selected Items:", total_value, "\n")
    print("Total Weight of Selected Items:", total_weight, "\n")
    print("Selected Items (with fraction):", selected_items, "\n")

    # Plot the results if show_plot is set to True
    if show_plot:
        plot_fractional_knapsack_solution(values, weights, selected_items)

def plot_fractional_knapsack_solution(values, weights, selected_items):
    """
    Plots the selected and unselected items in the fractional knapsack problem, showing value-to-weight ratios.

    Parameters:
    - values (list of floats): List of item values.
    - weights (list of floats): List of item weights.
    - selected_items (list of tuples): Indices of selected items and their fraction selected.
    """
    n = len(values)
    item_indices = list(range(1, n + 1))  # Start items from index 1

    # Calculate value-to-weight ratios
    ratios = [values[i] / weights[i] for i in range(n)]

    # Define colors for selected vs. unselected items, with transparency for fractions
    colors = ['#afd30b' if any(i + 1 == item[0] for item in selected_items) else '#d30b32' for i in range(n)]
    alphas = [next((item[1] for item in selected_items if item[0] == i + 1), 1.0) for i in range(n)]

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

    solve_fractional_knapsack_with_greedy(values, weights, max_weight, show_plot=True)