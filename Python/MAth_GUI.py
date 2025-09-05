import tkinter as tk
from tkinter import ttk
import math

def pythagorean(a, b): return math.sqrt(a**2 + b**2)

def quadratic(a, b, c):
    disc = b**2 - 4*a*c
    if disc < 0:
        return "No real roots."
    r1 = (-b + math.sqrt(disc)) / (2*a)
    r2 = (-b - math.sqrt(disc)) / (2*a)
    return f"{r1:.2f}, {r2:.2f}"

def distance(x1, y1, x2, y2): return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def slope(x1, y1, x2, y2): return "Undefined" if x2 == x1 else (y2 - y1) / (x2 - x1)

def gcf(a, b):
    while b: a, b = b, a % b
    return a

def lcm(a, b): return abs(a * b) // gcf(a, b)

def triangle_area_heron(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def triangle_area_base_height(base, height): return 0.5 * base * height

def circle_area(radius): return math.pi * radius**2

def circle_circumference(radius): return 2 * math.pi * radius

def decimal_to_fraction(number):    
    s = str(number)
    if '.' not in s: return f"{int(number)}/1"
    decimal_part = len(s.split('.')[1])
    numerator = int(float(number) * (10 ** decimal_part))
    denominator = 10 ** decimal_part
    div = gcf(numerator, denominator)
    return f"{numerator//div}/{denominator//div}"

class MathSolverApp:
    def __init__(self, root):
        self.root = root
        root.title("Premium Math Solver")
        root.geometry("480x600")
        root.configure(bg="#1f1f2e")

        self.entries = []
        self.result_var = tk.StringVar()
        self.option = tk.StringVar()
        self.option.set("Pythagorean")

        tk.Label(root, text="Premium Math Solver", font=("Helvetica", 20, "bold"), fg="white", bg="#1f1f2e").pack(pady=10)
        ttk.OptionMenu(root, self.option, self.option.get(),
                       *["Pythagorean", "Quadratic", "Distance", "Slope",
                         "GCF", "LCM", "Triangle (3 sides)", "Triangle (base/height)",
                         "Circle Area", "Circle Circumference", "Decimal to Fraction"],
                       command=self.show_inputs).pack()

        self.input_frame = tk.Frame(root, bg="#1f1f2e")
        self.input_frame.pack(pady=15)
        tk.Button(root, text="Solve", command=self.solve, bg="#4CAF50", fg="white", font=("Arial", 12), width=20).pack()
        tk.Label(root, textvariable=self.result_var, font=("Arial", 16), bg="#1f1f2e", fg="#00ffcc", wraplength=440, justify="center").pack(pady=20)

        self.show_inputs("Pythagorean")

    def show_inputs(self, selection):
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        self.entries.clear()
        input_map = {
            "Pythagorean": ["Leg 1", "Leg 2"],
            "Quadratic": ["a", "b", "c"],
            "Distance": ["x1", "y1", "x2", "y2"],
            "Slope": ["x1", "y1", "x2", "y2"],
            "GCF": ["Number 1", "Number 2"],
            "LCM": ["Number 1", "Number 2"],
            "Triangle (3 sides)": ["Side A", "Side B", "Side C"],
            "Triangle (base/height)": ["Base", "Height"],
            "Circle Area": ["Radius"],
            "Circle Circumference": ["Radius"],
            "Decimal to Fraction": ["Decimal Number"]
        }
        for label in input_map.get(selection, []):
            tk.Label(self.input_frame, text=label, font=("Arial", 12), fg="white", bg="#1f1f2e").pack()
            entry = tk.Entry(self.input_frame, font=("Arial", 12))
            entry.pack(pady=5)
            self.entries.append(entry)

    def solve(self):
        try:
            values = [float(e.get()) for e in self.entries]
            sel = self.option.get()
            if sel == "Pythagorean":
                res = pythagorean(*values)
            elif sel == "Quadratic":
                res = quadratic(*values)
            elif sel == "Distance":
                res = distance(*values)
            elif sel == "Slope":
                res = slope(*values)
            elif sel == "GCF":
                res = gcf(int(values[0]), int(values[1]))
            elif sel == "LCM":
                res = lcm(int(values[0]), int(values[1]))
            elif sel == "Triangle (3 sides)":
                res = triangle_area_heron(*values)
            elif sel == "Triangle (base/height)":
                res = triangle_area_base_height(*values)
            elif sel == "Circle Area":
                res = circle_area(values[0])
            elif sel == "Circle Circumference":
                res = circle_circumference(values[0])
            elif sel == "Decimal to Fraction":
                res = decimal_to_fraction(values[0])
            else:
                res = "Unknown operation."
            self.result_var.set(f"Result: {res}")
        except Exception:
            self.result_var.set("Error: Invalid input.")

root = tk.Tk()
app = MathSolverApp(root)
root.mainloop()
