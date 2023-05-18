
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import networkx as nx


class UniformCostSearchGUI:
    def __init__(self, root):
        self.root = root
        self.graph_entry = None
        self.start_entry = None
        self.goal_entry = None
        self.result_text = None
        self.graph = None

        # Create GUI components
        self.create_input_components()

    def create_input_components(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack()

        graph_label = ttk.Label(main_frame, text="Graph:")
        graph_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.graph_entry = ttk.Entry(main_frame, width=20)
        self.graph_entry.grid(row=0, column=1, padx=5, pady=5)

        start_label = ttk.Label(main_frame, text="Start Node:")
        start_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.start_entry = ttk.Entry(main_frame, width=20)
        self.start_entry.grid(row=1, column=1, padx=5, pady=5)

        goal_label = ttk.Label(main_frame, text="Goal Node:")
        goal_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.goal_entry = ttk.Entry(main_frame, width=20)
        self.goal_entry.grid(row=2, column=1, padx=5, pady=5)

        run_button = ttk.Button(main_frame, text="Run Uniform Cost Search", command=self.run_uniform_cost_search)
        run_button.grid(row=3, column=0, columnspan=2, pady=10)

        result_frame = ttk.Frame(main_frame, borderwidth=1, relief="solid")
        result_frame.grid(row=4, column=0, columnspan=2, pady=10)

        result_label = ttk.Label(result_frame, text="Result:")
        result_label.pack()

        self.result_text = tk.Text(result_frame, height=4, width=30)
        self.result_text.pack(pady=5)

    def run_uniform_cost_search(self):
        graph = self.graph_entry.get()
        start = self.start_entry.get()
        goal = self.goal_entry.get()

        # Perform Uniform Cost Search
        result = self.uniform_cost_search(graph, start, goal)

        # Display result
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Result: " + result)

        # Visualize graph
        self.visualize_graph(graph)

    def uniform_cost_search(self, graph, start, goal):
        # Implement the Uniform Cost Search algorithm here
        # You can use the graph, start, and goal as inputs

        # Placeholder implementation
        result = "Uniform Cost Search Result"
        return result

    def visualize_graph(self, graph):
        self.graph = nx.Graph(graph)

        pos = nx.spring_layout(self.graph)
        nx.draw_networkx(self.graph, pos, with_labels=True, node_color="skyblue", node_size=500, font_size=10)
        plt.title("Graph Visualization")
        plt.axis("off")
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x500")
    root.title("Uniform Cost Search Algorithm")
    app = UniformCostSearchGUI(root)
    root.mainloop()