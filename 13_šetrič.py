import tkinter
import random

# Vytvorenie okna a canvas

root = tkinter.Tk() # vytváram si premennú pre okno aplikácie
root.title("setric")


canvas = tkinter.Canvas(width=600, height=600)
canvas.pack()


# Funkcia na zobrazenie textu a jeho zmiznutie
def setric():

    canvas.delete("all") 

    farba = random.choice(["red","black","green","cyan","blue"])

    x = random.randint(0, 560)  # Náhodná pozícia na x-ovej osi
    y = random.randint(0, 560)  # Náhodná pozícia na y-ovej osi
    canvas.create_text(x, y, text='MATURITY 2026', fill=farba)

    root.after(1000, setric)  # Po 1s vykonáme funkciu  znova setric --> rekurzívna funkcia


# Spustenie prvej iterácie
setric()

def ukoncenie(event):  # parameter event v sebe uchováva informáciu pre spustenie udalosti (napr. stlačenie klávesy)
    root.destroy()

root.bind("p", ukoncenie)


# Hlavná slučka Tkinteru
tkinter.mainloop()