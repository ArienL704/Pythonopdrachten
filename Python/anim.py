import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, bg='yellow', height=300, width=500)

canvas.pack()

def task(x):
    if x < 5:
        l = root.after(1000, task, x + 1)
    else:
        task2(0)


    canvas.create_rectangle(0, 0, x * 100, 100, fill='red')

task(1)




def task2(y):
   if y < 5:
       root.after(1000, task2, y + 1)

   canvas.create_rectangle(500, y * 100, 400, (y + 1) * 100, fill='red')


root.mainloop()