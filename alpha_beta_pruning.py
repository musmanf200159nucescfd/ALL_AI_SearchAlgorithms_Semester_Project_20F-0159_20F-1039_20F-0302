
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import networkx as nx


class AlphaBetaPruningGUI:
    def __init__(self, root):
        self.root = root
        self.height_entry = None
        self.values_entry = None
        self.result_text = None
        self.graph = None

        # Create GUI components
        self.create_input_components()

    def create_input_components(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack()

        height_label = ttk.Label(main_frame, text="Height of Tree:")
        height_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.height_entry = ttk.Entry(main_frame, width=20)
        self.height_entry.grid(row=0, column=1, padx=5, pady=5)

        values_label = ttk.Label(main_frame, text="Values of Leaf Nodes:")
        values_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.values_entry = ttk.Entry(main_frame, width=20)
        self.values_entry.grid(row=1, column=1, padx=5, pady=5)

        run_button = ttk.Button(main_frame, text="Run Alpha-Beta Pruning", command=self.run_alpha_beta_pruning)
        run_button.grid(row=2, column=0, columnspan=2, pady=10)

        result_frame = ttk.Frame(main_frame, borderwidth=1, relief="solid")
        result_frame.grid(row=3, column=0, columnspan=2, pady=10)

        result_label = ttk.Label(result_frame, text="Result:")
        result_label.pack()

        self.result_text = tk.Text(result_frame, height=10, width=40)
        self.result_text.pack(pady=5)

    def run_alpha_beta_pruning(self):
        height = int(self.height_entry.get())
        values = list(map(int, self.values_entry.get().split()))

        tree = self.build_tree(height, values)
        self.graph = nx.DiGraph()
        self.build_graph(tree, 0)

        result = self.alpha_beta_pruning(tree, float("-inf"), float("inf"), True)

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

        self.draw_tree()

    def build_tree(self, height, values):
        if height <= 0 or not values:
            return None

        root = Node(values.pop(0))
        root.left = self.build_tree(height - 1, values)
        root.right = self.build_tree(height - 1, values)

        return root

    def build_graph(self, node, parent_id):
        if node is None:
            return

        node_id = len(self.graph)
        self.graph.add_node(node_id, value=str(node.value))

        if parent_id is not None:
            self.graph.add_edge(parent_id, node_id)

        self.build_graph(node.left, node_id)
        self.build_graph(node.right, node_id)

    def alpha_beta_pruning(self, node, alpha, beta, is_maximizing):
        if node is None:
            return ""

        if node.left is None and node.right is None:
            return str(node.value)

        if is_maximizing:
            value = float("-inf")
            sign = "max"
            for child in [node.left, node.right]:
                child_value =self.alpha_beta_pruning(child, alpha, beta, False)
                value = max(value, int(child_value))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
        else:
            value = float("inf")
            sign = "min"
            for child in [node.left, node.right]:
                child_value = self.alpha_beta_pruning(child, alpha, beta, True)
                value = min(value, int(child_value))
                beta = min(beta, value)
                if alpha >= beta:
                    break

        return str(value) + f", Type: {sign}\n"

    def draw_tree(self):
        pos = nx.spring_layout(self.graph)
        plt.figure(figsize=(8, 6))
        nx.draw_networkx(self.graph, pos, with_labels=True, node_size=500, font_size=10, node_color="lightblue",
                         edge_color="gray", arrows=True)
        plt.axis("off")
        plt.title("Alpha-Beta Pruning Tree")
        plt.show()


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x400")
    root.title("Alpha-Beta Pruning")
    app = AlphaBetaPruningGUI(root)
    root.mainloop()