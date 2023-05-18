import tkinter as tk
from tkinter import ttk

import bfs
import dfs
import depth_limited
import iterative_deepening
import uniform_cost_search
import bidirectional_search
import a_star_search
import adversarial_search
import simulated_annealing
import alpha_beta_pruning

# Functions for executing search algorithms
def execute_bfs():
    # Call the function from the bfs module
    # Replace the arguments with your specific inputs
    root = tk.Tk()
    root.geometry("700x700")
    root.title("BFS Algorithm")
    bfs.GraphBFSGUI(root)
    root.mainloop()


def execute_dfs():
    # Call the function from the dfs module
    # Replace the arguments with your specific inputs
    root = tk.Tk()
    root.geometry("700x700")
    root.title("DFS Algorithm")
    dfs.GraphDFSGUI(root)
    root.mainloop()


def execute_uniform_cost_search():
    # Call the function from the dfs module
    # Replace the arguments with your specific inputs
    root = tk.Tk()
    root.geometry("700x700")
    root.title("Uniform Cost Search")
    uniform_cost_search.UniformCostSearchGUI(root)
    root.mainloop()

def execute_iterative_deepening():
    # Call the function from the bfs module
    # Replace the arguments with your specific inputs
    root = tk.Tk()
    root.geometry("700x700")
    root.title("Iterative Deepening Search Algorithm")
    iterative_deepening.IterativeDeepeningSearchGUI(root)
    root.mainloop()

def execute_depth_limited():
    # Call the function from the bfs module
    # Replace the arguments with your specific inputs
    root = tk.Tk()
    root.geometry("700x700")
    root.title("Depth Limited")
    depth_limited.DepthLimitedSearchGUI(root)
    root.mainloop()

def execute_bidirectional_search():
    # Call the function from the bfs module
    # Replace the arguments with your specific inputs
    root = tk.Tk()
    root.geometry("700x700")
    root.title("Bidirectional Search")
    bidirectional_search.BidirectionalSearchGUI(root)
    root.mainloop()

def execute_a_star_search():
    # Call the function from the bfs module
    # Replace the arguments with your specific inputs
    root = tk.Tk()
    root.geometry("700x700")
    root.title("A_Star Search")
    a_star_search.AStarGUI(root)
    root.mainloop()

def execute_adversarial_search():
    # Call the function from the bfs module
    # Replace the arguments with your specific inputs
    root = tk.Tk()
    root.geometry("700x700")
    root.title("Adversarial Search")
    adversarial_search.TicTacToeGUI(root)
    root.mainloop()

def execute_simulated_annealing():
    # Call the function from the bfs module
    # Replace the arguments with your specific inputs
    root = tk.Tk()
    root.geometry("700x700")
    root.title("Simulated Annealing")
    simulated_annealing.SimulatedAnnealingGUI(root)
    root.mainloop()

def execute_alpha_beta_pruning():
    # Call the function from the bfs module
    # Replace the arguments with your specific inputs
    root = tk.Tk()
    root.geometry("700x700")
    root.title("Alpha Beta Pruning")
    alpha_beta_pruning.AlphaBetaPruningGUI(root)
    root.mainloop()

# Create the main window
window = tk.Tk()
window.title("AI Search Algorithms")

# Application Name Label
app_name_label = ttk.Label(window, text="AI Search Algorithms", font=("Arial", 18, "bold"))
app_name_label.pack(pady=10)

# Developers Box
developers_box = tk.Frame(window, bg="white", width=300, height=120, bd=2, relief=tk.SOLID)
developers_box.pack(pady=10)

# Developers Names
developer_names = ["20F-0159 Muhammad Usman", "20F-1030 M Alam", "20F-0302 Hassan Sherazi"]
for developer_name in developer_names:
    ttk.Label(developers_box, text=developer_name, font=("Arial", 12)).pack()

# Launch App Button
def launch_app():
    # Create a new window for the app
    app_window = tk.Toplevel(window)
    app_window.title("AI Search Algorithms")
    app_window.configure(bg="light gray")

    # Create buttons for each module
    bfs_button = ttk.Button(app_window, text="Breadth First Search", command=execute_bfs, width=20, style="Custom.TButton")
    bfs_button.pack(pady=5)

    dfs_button = ttk.Button(app_window, text="Depth First Search", command=execute_dfs, width=20, style="Custom.TButton")
    dfs_button.pack(pady=5)

    astar_button = ttk.Button(app_window, text="A* Search", command=execute_a_star_search, width=20, style="Custom.TButton")
    astar_button.pack(pady=5)

    advarsarial_button = ttk.Button(app_window, text="Adversarial Search", command=execute_adversarial_search, width=20, style="Custom.TButton")
    advarsarial_button.pack(pady=5)

    alpha_beta_pruning_button = ttk.Button(app_window, text="Alpha Beta Pruning", command=execute_alpha_beta_pruning, width=20, style="Custom.TButton")
    alpha_beta_pruning_button.pack(pady=5)

    bidirectional_search_button = ttk.Button(app_window, text="Bidirectional Search", command=execute_bidirectional_search, width=20, style="Custom.TButton")
    bidirectional_search_button.pack(pady=5)

    depth_limited_button = ttk.Button(app_window, text="Depth Limited Search", command=execute_depth_limited, width=20, style="Custom.TButton")
    depth_limited_button.pack(pady=5)

    iterative_deepening_button = ttk.Button(app_window, text="Iterative Deepening", command=execute_iterative_deepening, width=20, style="Custom.TButton")
    iterative_deepening_button.pack(pady=5)

    simulated_annealing_button = ttk.Button(app_window, text="Simulated Annealing", command=execute_simulated_annealing, width=20, style="Custom.TButton")
    simulated_annealing_button.pack(pady=5)

    uniform_cost_search_button = ttk.Button(app_window, text="Uniform Cost Search", command=execute_uniform_cost_search, width=20, style="Custom.TButton")
    uniform_cost_search_button.pack(pady=5)

    # Style the buttons with custom properties
    style = ttk.Style()
    style.configure("Custom.TButton",
                    background="pink",
                    foreground="black",
                    font=("Arial", 12, "bold"),
                    padding=8)
    style.map("Custom.TButton",
              background=[("active", "chartreuse1")],
              foreground=[("active", "green")])

launch_button = ttk.Button(window, text="Launch App", command=launch_app)
launch_button.pack(pady=10)

window.mainloop()
