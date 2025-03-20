import tkinter as tk
from tkinter import ttk
import json

# Create window
window = tk.Tk()
window.title("Hallo")

# window size
window.geometry("800x400")
window.minsize(200, 200)

# JSON file
with open("C:\\Users\\neapo\\Documents\\tmp\\Pythonopdrachten\\Python\\Muziek.json", 'r') as f:
    data = json.load(f)

# display
text_widget = tk.Text(window, height=20, width=80)
text_widget.pack()

text_widget.insert(tk.END, json.dumps(data, indent=4))

# read-only
text_widget.config(state=tk.DISABLED)

# goodbye
goodbye = tk.Button(window, text="Goodbye", command=window.destroy)
goodbye.pack()

window.mainloop()
