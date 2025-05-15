import tkinter as tk
import json

class Lokaal:
    def __init__(self, naam, richting, x1, y1, x2, y2):
        self.naam = naam
        self.richting = richting
        self.coords = (x1, y1, x2, y2)

    def to_dict(self):
        return {
            "naam": self.naam,
            "richting": self.richting,
            "coords": self.coords
        }

    def middenonder(self):
        """Return het midden van de onderzijde van het lokaal."""
        x1, y1, x2, y2 = self.coords
        return ((x1 + x2) // 2, y2)

class LokaalApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, height=700, width=700)
        self.canvas.pack()

        self.gang_y = 150
        self.lokalen = []
        self.selected = []

        self.teken_ganglijn()
        self.voeg_lokalen_toe()
        self.canvas.bind("<Button-1>", self.on_click)

    def teken_ganglijn(self):
        self.canvas.create_line(0, self.gang_y, 700, self.gang_y, fill='red', width=2)

    def voeg_lokaal_toe(self, naam, richting, x1, y1, x2, y2):
        lokaal = Lokaal(naam, richting, x1, y1, x2, y2)
        self.lokalen.append(lokaal)

        # Teken lokaal op canvas
        self.canvas.create_rectangle(x1, y1, x2, y2, fill='blue', tags=naam)
        self.canvas.create_text((x1 + x2)//2, (y1 + y2)//2, text=naam, fill='white')

    def voeg_lokalen_toe(self):
        self.voeg_lokaal_toe("C1.06", "West", 50, 50, 100, 100)
        self.voeg_lokaal_toe("C1.04", "West", 175, 50, 225, 100)
        self.voeg_lokaal_toe("C1.13", "West", 300, 50, 350, 100)

        # Opslaan naar JSON
        with open("lokalen.json", "w") as f:
            json.dump([l.to_dict() for l in self.lokalen], f, indent=2)

    def on_click(self, event):
        for lokaal in self.lokalen:
            x1, y1, x2, y2 = lokaal.coords
            if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                self.selected.append(lokaal)
                print(f"Geselecteerd: {lokaal.naam}")
                self.teken_verticale_lijn(lokaal)
                if len(self.selected) == 2:
                    self.teken_route(self.selected[0], self.selected[1])
                    self.selected = []
                break

    def teken_verticale_lijn(self, lokaal):
        x, y = lokaal.middenonder()
        self.canvas.create_line(x, y, x, self.gang_y, fill='green', width=2)

    def teken_route(self, lokaal1, lokaal2):
        x1, _ = lokaal1.middenonder()
        x2, _ = lokaal2.middenonder()
        self.canvas.create_line(x1, self.gang_y, x2, self.gang_y, fill='green', width=2)

# Start app
root = tk.Tk()
app = LokaalApp(root)
root.mainloop()
