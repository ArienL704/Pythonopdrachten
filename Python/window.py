import tkinter as tk
import json

window = tk.Tk()
window.title("Hallo")

window.geometry("1000x1000")
window.minsize(200, 200)

with open("C:\\Users\\neapo\\Documents\\tmp\\Pythonopdrachten\\Python\\Muziek.json", 'r') as f:
    data = json.load(f)
    print(data)

o = tk.Label(window, text="tekst")
o.pack()
#T = window.Text(window, )

    

goodbye = tk.Button(window, text="Goodbye", command=window.destroy)
goodbye.pack()

window.mainloop()