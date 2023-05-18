
import tkinter as tk
from tkinter import ttk
from queue import PriorityQueue


class AStarGUI:
    def __init__(self, root):
        self.root = root
        self.grid_size = None
        self.start_node = None
        self.goal_node = None
        self.grid_buttons = None
        self.path = []

        # Create GUI components
        self.create_input_components()

    def create_input_components(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack()

        size_label = ttk.Label(main_frame, text="Grid Size:")
        size_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        size_entry = ttk.Entry(main_frame, width=20)
        size_entry.grid(row=0, column=1, padx=5, pady=5)

        start_label = ttk.Label(main_frame, text="Start Node:")
        start_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        start_entry = ttk.Entry(main_frame, width=20)
        start_entry.grid(row=1, column=1, padx=5, pady=5)

        goal_label = ttk.Label(main_frame, text="Goal Node:")
        goal_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        goal_entry = ttk.Entry(main_frame, width=20)
        goal_entry.grid(row=2, column=1, padx=5, pady=5)

        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)

        button = ttk.Button(button_frame, text="Create Grid", command=lambda: self.create_grid(size_entry.get()))
        button.pack(pady=5)

        solve_button = ttk.Button(button_frame, text="Solve", command=self.solve_astar)
        solve_button.pack(pady=5)

        self.grid_buttons = []

    def create_grid(self, size):
        self.grid_size = int(size)

        grid_frame = ttk.Frame(self.root, padding=20)
        grid_frame.pack()

        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                button = ttk.Button(grid_frame, text=" ", width=5, command=lambda x=i, y=j: self.toggle_obstacle(x, y))
                button.grid(row=i, column=j, padx=2, pady=2)
                row.append(button)
            self.grid_buttons.append(row)

    def toggle_obstacle(self, x, y):
        button = self.grid_buttons[x][y]
        current_text = button["text"]

        if current_text == " ":
            button.config(text="X")
        else:
            button.config(text=" ")

    def solve_astar(self):
        if self.grid_size is None:
            return

        self.start_node = None
        self.goal_node = None
        grid = []

        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                button = self.grid_buttons[i][j]
                if button["text"] == "X":
                    row.append(1)
                else:
                    if button["text"] == "S":
                        self.start_node = (i, j)
                    elif button["text"] == "G":
                        self.goal_node = (i, j)
                    row.append(0)
            grid.append(row)

        if self.start_node is None or self.goal_node is None:
            return

        path = self.astar(grid

, self.start_node, self.goal_node)

        if path is not None:
            self.path = path
            self.show_path()

    def astar(self, grid, start, goal):
        rows = len(grid)
        cols = len(grid[0])

        # Define the heuristic function (Manhattan distance)
        def heuristic(node):
            return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

        # Define the cost function
        def cost(node):
            return 1

        # Define the neighbors of a given node
        def neighbors(node):
            i, j = node
            neighbors = []
            if i > 0:
                neighbors.append((i - 1, j))
            if i < rows - 1:
                neighbors.append((i + 1, j))
            if j > 0:
                neighbors.append((i, j - 1))
            if j < cols - 1:
                neighbors.append((i, j + 1))
            return neighbors

        # Create priority queue and visited set
        queue = PriorityQueue()
        queue.put((0, start))
        visited = set()
        visited.add(start)

        # Create dictionaries for storing costs and parents
        cost_so_far = {start: 0}
        parent = {start: None}

        while not queue.empty():
            current = queue.get()[1]

            if current == goal:
                break

            for next_node in neighbors(current):
                new_cost = cost_so_far[current] + cost(next_node)
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + heuristic(next_node)
                    queue.put((priority, next_node))
                    visited.add(next_node)
                    parent[next_node] = current

        # Reconstruct the path from goal to start
        path = []
        current = goal

        while current != start:
            path.append(current)
            current = parent[current]

        path.append(start)
        path.reverse()

        if path[0] == start and path[-1] == goal:
            return path
        else:
            return None

    def show_path(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                button = self.grid_buttons[i][j]
                if (i, j) in self.path:
                    button.config(text="*", foreground="red")
                elif button["text"] != "S" and button["text"] != "G":
                    button.config(text=" ")

    def clear_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                button = self.grid_buttons[i][j]
                button.config(text=" ")

    def set_start_node(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                button = self.grid_buttons[i][j]
                if button["text"] == "S":
                    button.config(text=" ")
        self.start_node = None

    def set_goal_node(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                button = self.grid_buttons[i][j]
                if button["text"] == "G":
                    button.config(text=" ")
        self.goal_node = None

"""""
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x400")
    root.title("A* Algorithm")
    app = AStarGUI(root)
    root.mainloop()
"""