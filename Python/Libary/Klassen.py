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

# Posities van lokalen op canvas (x1, y1, x2, y2)
lokalen_pos = {
    "C1.06": (50, 50, 100, 100),
    "C1.04": (175, 50, 225, 100),
    "C1.13": (300, 50, 350, 100),
}

# Lokalen tekenen
for naam, (x1, y1, x2, y2) in lokalen_pos.items():
    canvas.create_rectangle(x1, y1, x2, y2, fill='blue', tags=naam)
    canvas.create_text((x1 + x2)//2, (y1 + y2)//2, text=naam, fill='white')

canvas.create_line(50, 120, 350, 120, fill='red', width=1)

root.mainloop()