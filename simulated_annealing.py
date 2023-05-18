
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import random


class SimulatedAnnealingGUI:
    def __init__(self, root):
        self.root = root
        self.temperature_entry = None
        self.initial_solution_entry = None
        self.result_text = None
        self.x_values = None
        self.y_values = None
        self.best_solution = None

        # Create GUI components
        self.create_input_components()

    def create_input_components(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack()

        temperature_label = ttk.Label(main_frame, text="Initial Temperature:")
        temperature_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.temperature_entry = ttk.Entry(main_frame, width=20)
        self.temperature_entry.grid(row=0, column=1, padx=5, pady=5)

        initial_solution_label = ttk.Label(main_frame, text="Initial Solution:")
        initial_solution_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.initial_solution_entry = ttk.Entry(main_frame, width=20)
        self.initial_solution_entry.grid(row=1, column=1, padx=5, pady=5)

        run_button = ttk.Button(main_frame, text="Run Simulated Annealing", command=self.run_simulated_annealing)
        run_button.grid(row=2, column=0, columnspan=2, pady=10)

        result_frame = ttk.Frame(main_frame, borderwidth=1, relief="solid")
        result_frame.grid(row=3, column=0, columnspan=2, pady=10)

        result_label = ttk.Label(result_frame, text="Result:")
        result_label.pack()

        self.result_text = tk.Text(result_frame, height=10, width=40)
        self.result_text.pack(pady=5)

    def run_simulated_annealing(self):
        temperature = float(self.temperature_entry.get())
        initial_solution = list(map(int, self.initial_solution_entry.get().split()))

        self.x_values = np.arange(-10, 11, 1)
        self.y_values = self.objective_function(self.x_values)

        current_solution = initial_solution
        current_energy = self.calculate_energy(current_solution)

        best_solution = current_solution
        best_energy = current_energy

        while temperature > 0.1:
            new_solution = self.generate_neighbor(current_solution)
            new_energy = self.calculate_energy(new_solution)

            if self.acceptance_probability(current_energy, new_energy, temperature) > random.random():
                current_solution = new_solution
                current_energy = new_energy

            if current_energy < best_energy:
                best_solution = current_solution
                best_energy = current_energy

            temperature *= 0.95

        self.best_solution = best_solution

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Best Solution: {best_solution}\nBest Energy: {best_energy}")

        self.plot_results()

    def objective_function(self, x):
        return x ** 2

    def calculate_energy(self, solution):
        x = self.x_values[solution]
        y = self.y_values[solution]
        return np.sum(y)

    def generate_neighbor(self, solution):
        neighbor = solution.copy()
        index = random.randint(0, len(neighbor) - 1)
        neighbor[index] = random.randint(0, len(self.x_values) - 1)


        return neighbor

    def acceptance_probability(self, current_energy, new_energy, temperature):
        if new_energy < current_energy:
            return 1.0
        return np.exp((current_energy - new_energy) / temperature)

    def plot_results(self):
        plt.figure(figsize=(8, 6))
        plt.plot(self.x_values, self.y_values, label="Objective Function")
        plt.scatter(self.x_values[self.best_solution], self.y_values[self.best_solution], color='red',
                    label="Best Solution")
        plt.title("Simulated Annealing")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x400")
    root.title("Simulated Annealing")
    app = SimulatedAnnealingGUI(root)
    root.mainloop()