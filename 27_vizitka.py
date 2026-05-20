import tkinter
canvas=tkinter.Canvas(width = 800, height = 600)
canvas.pack()

canvas.create_rectangle(10,50,790,550)
canvas.create_line(20,130,780,130)
canvas.create_line(50,300,750,300, fill='magenta', width = 3 )
canvas.create_line(150,200,150,500, fill='magenta', width = 3 )
canvas.create_oval(100,250,200,350, outline='blue', width = 2)
canvas.create_text(400,100, text = 'Gymnázium v Ružomberku, Š. Moyzesa 21, 034 01 Ružomberok', font= 'Arial 18')
canvas.create_text(400,400, text = 'Janko Hraško', font = 'Arial 50 bold', fill = 'magenta')


tkinter.mainloop()