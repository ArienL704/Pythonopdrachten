import tkinter as tk

window = tk.Tk()
window.title("Hallo")

window.geometry("200x200")
window.minsize(200, 200)

Label_hallo = tk.Label(text="Hello")
Label_hallo.pack(pady = 20)
    

goodbye = tk.Button(window, text="Goodbye", command=window.destroy)
goodbye.pack()

window.mainloop()