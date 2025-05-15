import tkinter as tk
import json

class Lokaal:
    def __init__(self, naam, richting):
        self.naam = naam
        self.richting = richting

    def to_dict(self):
        return {"naam": self.naam, "richting": self.richting}


# Lokalen defineren
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

# Posities van lokalen (x1, y1, x2, y2)
lokalen_pos = {
    "C1.06": (50, 50, 100, 100),
    "C1.04": (175, 50, 225, 100),
    "C1.13": (300, 50, 350, 100),
}

# tekenen
for naam, (x1, y1, x2, y2) in lokalen_pos.items():
    canvas.create_rectangle(x1, y1, x2, y2, fill='blue', tags=naam)
    canvas.create_text((x1 + x2)//2, (y1 + y2)//2, text=naam, fill='white')

# Main-Line
gang_y = 150
canvas.create_line(0, gang_y, 700, gang_y, width=0)

# Klik-logica
selected = []

def on_click(event):
    global selected
    for naam, (x1, y1, x2, y2) in lokalen_pos.items():
        if x1 <= event.x <= x2 and y1 <= event.y <= y2:
            selected.append(naam)
            print(f"Geselecteerd: {naam}")
            teken_verticale_lijn(naam)
            if len(selected) == 2:
                teken_horizontale_route(selected[0], selected[1])
                selected = []
            break

def teken_verticale_lijn(lokaal_naam):
    x1, y1, x2, y2 = lokalen_pos[lokaal_naam]
    x_midden = (x1 + x2) // 2
    y_onderkant = y2
    canvas.create_line(x_midden, y_onderkant, x_midden, gang_y, fill='green', width=2)

def teken_horizontale_route(lokaal1, lokaal2):
    x1, _, x2, _ = lokalen_pos[lokaal1]
    x_start = (x1 + x2) // 2

    x3, _, x4, _ = lokalen_pos[lokaal2]
    x_end = (x3 + x4) // 2

    # Line
    canvas.create_line(x_start, gang_y, x_end, gang_y, fill='green', width=2)

# Click
canvas.bind("<Button-1>", on_click)



root.mainloop()