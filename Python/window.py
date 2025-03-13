import tkinter as tk

window = tk.Tk()
window.title("Hallo")

Label_hallo = tk.Label(text="Hello")
Label_hallo.pack()
    

goodbye = tk.Button(window, text="Goodbye", command=window.destroy)
goodbye.pack()

window.mainloop()