import tkinter as tk
from tkinter import ttk

root = tk.Tk()

canvas = tk.Canvas(root, height=100, width=300)

canvas.pack()

# De sprite is 
image = tk.PhotoImage(file="Mushroom-Run.png")
# Display it within a label.
label = ttk.Label(image=image)
label.pack()

root.mainloop()