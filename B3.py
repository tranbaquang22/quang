import tkinter as tk
from math import pi

class ShapeCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Máy tính hình học")

        self.shape_label = tk.Label(master, text="Chọn hình:")
        self.shape_label.pack()

        self.shape_var = tk.StringVar()
        self.shape_var.set("Circle")  # Mặc định là hình tròn
        self.shape_menu = tk.OptionMenu(master, self.shape_var, "Circle", "Rectangle", "Triangle", command=self.update_fields)
        self.shape_menu.pack()

        self.dimension_label = tk.Label(master, text="Nhập số liệu:")
        self.dimension_label.pack()

        self.radius_label = tk.Label(master, text="Bán kính:")
        self.radius_label.pack()

        self.radius_entry = tk.Entry(master)
        self.radius_entry.pack()

        self.length_label = tk.Label(master, text="Cạnh 1:")
        self.length_label.pack()

        self.length_entry = tk.Entry(master)
        self.length_entry.pack()

        self.width_label = tk.Label(master, text="Cạnh 2:")
        self.width_label.pack()

        self.width_entry = tk.Entry(master)
        self.width_entry.pack()

        self.height_label = tk.Label(master, text="Cạnh 3:")
        self.height_label.pack()

        self.height_entry = tk.Entry(master)
        self.height_entry.pack()

        self.calculate_button = tk.Button(master, text="Tính", command=self.calculate)
        self.calculate_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.result_label1 = tk.Label(master, text="")
        self.result_label1.pack()

        # Ẩn các trường nhập liệu không liên quan ban đầu
        self.hide_dimensions(["Length", "Width", "Height"])

    def update_fields(self, shape):
        self.clear_result()
        # Ẩn tất cả các trường nhập liệu
        self.hide_dimensions(["Radius", "Length", "Width", "Height"])

        # Hiển thị các trường nhập liệu phù hợp với hình được chọn
        if shape == "Circle":
            self.show_dimensions(["Radius"])
        elif shape == "Rectangle":
            self.show_dimensions(["Length", "Width"])
        elif shape == "Triangle":
            self.show_dimensions(["Length", "Width", "Height"])

    def hide_dimensions(self, dimensions):
        for dimension in dimensions:
            getattr(self, f"{dimension.lower()}_label").pack_forget()
            getattr(self, f"{dimension.lower()}_entry").pack_forget()

    def show_dimensions(self, dimensions):
        for dimension in dimensions:
            getattr(self, f"{dimension.lower()}_label").pack()
            getattr(self, f"{dimension.lower()}_entry").pack()

    def clear_result(self):
        self.result_label.config(text="")
        self.result_label1.config(text="")

    def calculate(self):
        self.clear_result()
        shape = self.shape_var.get()

        try:
            if shape == "Circle":
                radius = float(self.radius_entry.get())
                circumference = 2 * pi * radius
                area = pi * radius**2
            elif shape == "Rectangle":
                length = float(self.length_entry.get())
                width = float(self.width_entry.get())
                circumference = 2 * (length + width)
                area = length * width
            elif shape == "Triangle":
                side1 = float(self.length_entry.get())
                side2 = float(self.width_entry.get())
                side3 = float(self.height_entry.get())
                circumference = side1 + side2 + side3
                s = circumference / 2  # Semi-perimeter
                area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter valid numerical values.")
            return

        result_text = f"Chu vi: {circumference}"
        self.result_label.config(text=result_text)
        result_text1 = f"Diện tích: {area}"
        self.result_label1.config(text=result_text1)


root = tk.Tk()
root.geometry("400x300")
app = ShapeCalculator(root)
root.mainloop()
