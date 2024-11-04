from tkinter import *
raiz=Tk()

raiz.title("Ventana de Gilbert")

#raiz.resizable(1,0)

raiz.iconbitmap("onepiece.ico")

#raiz.geometry("650x350")

raiz.config(bg="black")

miFrame=Frame()

miFrame.pack()

miFrame.config(bg="red")

miFrame.config(width="650", height="350")

miFrame.config(bd=35)

miFrame.config(relief="sunken")

miFrame.config(cursor="pirate")

raiz.mainloop()
