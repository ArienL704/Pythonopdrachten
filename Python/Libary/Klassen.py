import tkinter as tk
import json

class Lokaal:
    def __init__(self, naam, richting):
        self.naam = naam
        self.richting = richting

    def to_dict(self):
        return {"naam": self.naam, "richting": self.richting}



L1 = Lokaal("C1.06", "West")
L2 = Lokaal("C1.04", "West")
L3 = Lokaal("C1.13", "West")

print(L1.naam)
print(L1.richting)
print(L2.naam)
print(L2.richting)
print(L3.naam)
print(L3.richting)

lokalen = [L1.to_dict(), L2.to_dict(), L3.to_dict()]

# JSON file
with open("lokalen.json", "w") as f:
    json.dump(lokalen, f, indent=2)

    
root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700)

canvas.pack()

# Lokaal 1
canvas.create_rectangle(50, 50, 100, 100, fill='blue')
canvas.create_text(75, 75, text=L1.naam, fill='white')

# Lokaal 2
canvas.create_rectangle(175, 50, 225, 100, fill='blue')
canvas.create_text(200, 75, text=L2.naam, fill='white')

# Lokaal 3
canvas.create_rectangle(300, 50, 350, 100, fill='blue')
canvas.create_text(325, 75, text=L3.naam, fill='white')

canvas.create_line(50, 120, 350, 120, fill='red', width=1)


root.mainloop()