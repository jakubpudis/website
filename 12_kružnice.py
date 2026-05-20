import tkinter
import random
canvas = tkinter.Canvas(width = 600, heigh = 600)
canvas.pack()

n=int(input('Zadajte počet kružnic:' ))
x=300
y=300
for i in range(n):
    r=i*10
    f=random.choice(['red', 'green', 'blue', 'cyan', 'magenta'])
    canvas.create_oval(x-r,y-r,x+r,y+r, outline=f, width =2)
tkinter.mainloop()