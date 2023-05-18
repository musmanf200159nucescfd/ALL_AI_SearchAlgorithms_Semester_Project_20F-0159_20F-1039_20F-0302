
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt


class DepthLimitedSearchGUI:
    def __init__(self, root):
        self.root = root
        self.depth_entry = None
        self.solve_button = None

        # Create GUI components
        self.create_input_components()

    def create_input_components(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack()

        depth_label = ttk.Label(main_frame, text="Depth Limit:")
        depth_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.depth_entry = ttk.Entry(main_frame, width=20)
        self.depth_entry.grid(row=0, column=1, padx=5, pady=5)

        self.solve_button = ttk.Button(main_frame, text="Solve", command=self.solve)
        self.solve_button.grid(row=1, column=0, columnspan=2, pady=10)

    def solve(self):
        depth_limit_entry_value = self.depth_entry.get()
        if depth_limit_entry_value == "":
            return

        depth_limit = int(depth_limit_entry_value)

        # Perform depth-limited search
        result = self.depth_limited_search(depth_limit)

        # Plot the search tree
        self.plot_search_tree(result)

    def depth_limited_search(self, depth_limit):
        # TODO: Implement your depth-limited search algorithm here
        # Return the result of the search, e.g., a search tree

        # Example code: Generate a dummy search tree
        tree = {
            'A': ['B', 'C', 'D'],
            'B': ['E', 'F'],
            'C': [],
            'D': ['G', 'H'],
            'E': [],
            'F': [],
            'G': [],
            'H': [],
        }

        return tree

    def plot_search_tree(self, search_tree):
        plt.figure(figsize=(8, 6))
        self.plot_tree_node(search_tree, 'A', 0, 0)
        plt.axis('off')
        plt.show()

    def plot_tree_node(self, search_tree, node, level, x_pos):
        if node not in search_tree:
            return

        y_pos = -level * 0.1
        children = search_tree[node]

        for child in children:
            x_offset = 1 / (level + 1)
            x_child = x_pos + x_offset

            plt.plot([x_pos, x_child], [y_pos, y_pos - 0.1], 'k-')
            plt.text(x_pos, y_pos, node, ha='center', va='center')
            self.plot_tree_node(search_tree, child, level + 1, x_child)

            x_pos += x_offset

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Depth-Limited Search")
    app = DepthLimitedSearchGUI(root)
    app.run()