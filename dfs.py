
import tkinter as tk
from tkinter import ttk


class GraphDFSGUI:
    def __init__(self, root):
        self.root = root
        self.vertices_entry = None
        self.edges_entry = None
        self.edge_entries = []
        self.weight_entries = []
        self.start_vertex_entry = None
        self.graph = {}
        self.run_dfs_button = None
        self.result_text = None

        # Create GUI components
        self.create_input_components()

    def create_input_components(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack()

        vertices_label = ttk.Label(main_frame, text="Number of Vertices:")
        vertices_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.vertices_entry = ttk.Entry(main_frame, width=20)
        self.vertices_entry.grid(row=0, column=1, padx=5, pady=5)

        edges_label = ttk.Label(main_frame, text="Number of Edges:")
        edges_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.edges_entry = ttk.Entry(main_frame, width=20)
        self.edges_entry.grid(row=1, column=1, padx=5, pady=5)

        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)

        button = ttk.Button(button_frame, text="Enter Values for Source/Destination/Weight", command=self.create_edge_fields)
        button.pack(pady=5)

        self.run_dfs_button = ttk.Button(main_frame, text="Run DFS", command=self.run_dfs)
        self.run_dfs_button.grid(row=3, column=0, columnspan=2, pady=10)

        start_vertex_label = ttk.Label(main_frame, text="Starting Vertex:")
        start_vertex_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.start_vertex_entry = ttk.Entry(main_frame, width=20)
        self.start_vertex_entry.grid(row=4, column=1, padx=5, pady=5)

        result_frame = ttk.Frame(main_frame, borderwidth=1, relief="solid")
        result_frame.grid(row=5, column=0, columnspan=2, pady=10)

        result_label = ttk.Label(result_frame, text="Result:")
        result_label.pack()

        self.result_text = tk.Text(result_frame, height=4, width=30)
        self.result_text.pack(pady=5)

    def create_edge_fields(self):
        num_edges = int(self.edges_entry.get())

        edge_frame = ttk.Frame(self.root, padding=20)
        edge_frame.pack()

        for i in range(num_edges):
            source_label = ttk.Label(edge_frame, text="Source:")
            source_label.grid(row=i, column=0, sticky="w", padx=5, pady=5)
            source_entry = ttk.Entry(edge_frame, width=10)
            source_entry.grid(row=i, column=1, padx=5, pady=5)

            destination_label = ttk.Label(edge_frame, text="Destination:")
            destination_label.grid(row=i, column=2, sticky="w", padx=5, pady=5)
            destination_entry = ttk.Entry(edge_frame, width=10)
            destination_entry.grid(row=i, column=3, padx=5, pady=5)

            weight_label = ttk.Label(edge_frame, text="Weight:")
            weight_label.grid(row=i, column=4, sticky="w",

 padx=5, pady=5)
            weight_entry = ttk.Entry(edge_frame, width=10)
            weight_entry.grid(row=i, column=5, padx=5, pady=5)

            self.edge_entries.append((source_entry, destination_entry))
            self.weight_entries.append(weight_entry)

    def run_dfs(self):
        num_vertices = int(self.vertices_entry.get())

        # Process graph input
        for i, (source_entry, destination_entry) in enumerate(self.edge_entries):
            source = int(source_entry.get())
            destination = int(destination_entry.get())
            weight = int(self.weight_entries[i].get())

            if source in self.graph:
                self.graph[source].append((destination, weight))
            else:
                self.graph[source] = [(destination, weight)]

        # Perform DFS
        start_vertex = int(self.start_vertex_entry.get())
        dfs_result = self.dfs(start_vertex)

        # Display DFS result
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "DFS traversal: " + " -> ".join(str(vertex) for vertex in dfs_result))

    def dfs(self, vertex, visited=None, traversal=None):
        if visited is None:
            visited = set()
        if traversal is None:
            traversal = []

        visited.add(vertex)
        traversal.append(vertex)

        if vertex in self.graph:
            neighbors = self.graph[vertex]
            for neighbor, _ in neighbors:
                if neighbor not in visited:
                    self.dfs(neighbor, visited, traversal)

        return traversal


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x500")
    root.title("DFS Algorithm")
    app = GraphDFSGUI(root)
    root.mainloop()