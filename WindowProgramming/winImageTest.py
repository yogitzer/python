from tkinter import *
window = Tk()

photo1 = PhotoImage(file = "C:\\Users\\태은\\Desktop\\파이썬\\python\\WindowProgramming\\dog.gif",)
photo2 = PhotoImage(file = "C:\\Users\\태은\\Desktop\\파이썬\\python\\WindowProgramming\\dog2.gif",)
label1 = Label(window, image = photo1)
label2 = Label(window, image = photo2)

label1.pack(side=LEFT)
label2.pack(side=LEFT)

window.mainloop()