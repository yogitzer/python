from tkinter import *
from tkinter import messagebox

def clickImage(event):
    messagebox.showinfo("마우스","강아지에서 마우스가 클릭됨")


window = Tk()
window.geometry("400x400")

photo = PhotoImage(file = "C:\\Users\\태은\\Desktop\\파이썬\\python\\WindowProgramming\\dog.gif",)
label1=Label(window, image=photo)
label1.bind("<Button>",clickImage)

label1.pack(expand=1, anchor=CENTER)
window.mainloop()