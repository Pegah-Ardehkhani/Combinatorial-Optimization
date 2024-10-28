import networkx as nx
import matplotlib.pyplot as plt
import heapq

def solve_MST_with_prim(nodes, edges):
    """
    Solves the MST problem using Prim's algorithm.

    Parameters:
    - nodes (list of ints): List of node identifiers.
    - edges (dict): Dictionary with (node1, node2) tuples as keys and weights as values.
    """
    # Create a graph from edges for easier management
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(((node1, node2, weight) for (node1, node2), weight in edges.items()))

    # Initialize variables for Prim's algorithm
    mst_edges = []  # List to store edges in the MST
    total_weight = 0  # Accumulate total MST weight
    visited = set()  # Track visited nodes
    min_heap = []  # Priority queue to get the minimum edge

    # Start from the first node
    start_node = nodes[0]
    visited.add(start_node)

    # Add edges from the start node to the min-heap
    for neighbor, weight in G[start_node].items():
        heapq.heappush(min_heap, (weight['weight'], start_node, neighbor))

    # Main loop for Prim's algorithm
    while min_heap:
        weight, node1, node2 = heapq.heappop(min_heap)  # Get the smallest edge
        if node2 not in visited:  # Only consider edges to unvisited nodes
            visited.add(node2)  # Mark the new node as visited
            mst_edges.append((node1, node2, weight))  # Add edge to the MST
            total_weight += weight  # Update total weight

            # Add edges from the new node to the min-heap
            for neighbor, edge_weight in G[node2].items():
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight['weight'], node2, neighbor))

            # Stop if we have enough edges for an MST
            if len(mst_edges) == len(nodes) - 1:
                break

    # Display the total weight and selected edges in the MST
    print("Optimal Total Weight:", total_weight, "\n")
    print("Selected Edges in MST:")
    for edge in mst_edges:
        print(f"Edge: ({edge[0]}, {edge[1]}), Weight: {edge[2]}")
    print("\n")

    # Plot the MST for visual understanding
    plot_mst(nodes, edges, mst_edges)


def plot_mst(nodes, edges, mst_edges):
    """
    Plots the Minimum Spanning Tree with all edges shown, MST edges highlighted.

    Parameters:
    - nodes (list): List of node identifiers.
    - edges (dict): All edges with weights.
    - mst_edges (list): MST edges as (node1, node2, weight).
    """
    # Set figure size for better visibility
    plt.figure(figsize=(10, 6))  # Adjust width and height as needed

    # Create a graph and add nodes and edges
    G = nx.Graph()
    G.add_nodes_from(nodes)
    for (node1, node2), weight in edges.items():
        G.add_edge(node1, node2, weight=weight)

    # Extract positions for nodes using a spring layout for visual clarity
    pos = nx.spring_layout(G, seed=42)

    # Draw all edges with light color and thinner lines for background
    nx.draw_networkx_edges(G, pos, edgelist=edges.keys(), width=1, alpha=0.5, edge_color="gray")

    # Highlight MST edges with a different color and thicker lines
    mst_edge_list = [(edge[0], edge[1]) for edge in mst_edges]
    nx.draw_networkx_edges(G, pos, edgelist=mst_edge_list, width=2, edge_color="#bd1435", label="MST Edges")

    # Draw nodes with custom size and color for better visibility
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color="#14bd87")
    nx.draw_networkx_labels(G, pos, font_size=12, font_color="black")

    # Add edge labels to display the weights
    edge_labels = {edge: f"{weight}" for edge, weight in edges.items()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    # Display the plot with title
    plt.title("Minimum Spanning Tree (MST)")
    plt.show()


# Example usage
if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6, 7]
    edges = {
        (1, 2): 3,
        (1, 3): 2,
        (2, 4): 6,
        (2, 5): 5,
        (3, 4): 1,
        (3, 6): 4,
        (4, 5): 2,
        (5, 7): 3,
        (6, 7): 4,
        (4, 6): 3
    }

    solve_MST_with_prim(nodes, edges)