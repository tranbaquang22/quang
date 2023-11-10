import numpy as np
import tkinter as tk


def solve_linear_equations(coefficients, constants):
    try:
        solution = np.linalg.solve(coefficients, constants)
        return solution
    except np.linalg.LinAlgError:
        return None


def solve_equations(coefficient_entries, constant_entries):
    coefficients = []
    constants = []

    for entry in coefficient_entries:
        equation = []
        for e in entry:
            coefficient = float(e.get())
            equation.append(coefficient)
        coefficients.append(equation)

    for e in constant_entries:
        constant = float(e.get())
        constants.append(constant)

    coefficients_matrix = np.array(coefficients)
    constants_vector = np.array(constants)

    solution = solve_linear_equations(coefficients_matrix, constants_vector)

    if solution is not None:
        result_text.delete("1.0", tk.END)
        for i in range(len(solution)):
            result_text.insert(tk.END, f"Biến {i + 1}: {solution[i]}\n")
    else:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Không có lời giải.")


def create_equation_inputs():
    n = int(num_equations_entry.get())

    for i in range(n):
        equation_frame = tk.Frame(input_frame)
        equation_frame.pack(pady=5)

        equation_label = tk.Label(equation_frame, text=f"Phương trình {i + 1}:")
        equation_label.pack(side=tk.LEFT)

        coefficient_entries = []
        for j in range(n):
            coefficient_entry = tk.Entry(equation_frame, width=5)
            coefficient_entry.pack(side=tk.LEFT)
            coefficient_entries.append(coefficient_entry)

        constant_entry = tk.Entry(equation_frame, width=5)
        constant_entry.pack(side=tk.LEFT)

        coefficient_entries_list.append(coefficient_entries)
        constant_entries_list.append(constant_entry)


# Create the main window
window = tk.Tk()
window.title("Giải Hệ Phương Trình Tuyến Tính")

# Create input frame
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

# Create number of equations input
num_equations_label = tk.Label(input_frame, text="Số Phương Trình:")
num_equations_label.pack(side=tk.LEFT)

num_equations_entry = tk.Entry(input_frame, width=5)
num_equations_entry.pack(side=tk.LEFT)

create_inputs_button = tk.Button(input_frame, text="Tạo Đầu Vào", command=create_equation_inputs)
create_inputs_button.pack(side=tk.LEFT, padx=10)

coefficient_entries_list = []
constant_entries_list = []

# Create solve button
solve_button = tk.Button(window, text="Giải",
                         command=lambda: solve_equations(coefficient_entries_list, constant_entries_list))
solve_button.pack(pady=10)

# Create result text area
result_text = tk.Text(window, height=5, width=30)
result_text.pack()

# Start the GUI event loop
window.mainloop()
