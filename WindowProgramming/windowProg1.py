from tkinter import *
from time import *

fnameList = ["bear.gif", "bee.gif", "cupid.gif", "dog.gif", "dog2.gif", "sun.gif", "sun2.gif", "tractor.gif", "unicorn.gif"]
num = 0

def clickNext():
    global num, photo, nameLabel  # <- nameLabel도 global로 지정
    num += 1
    if num > 8:
        num = 0
    photo = PhotoImage(file="C:\\Users\\태은\\Desktop\\파이썬\\python\\WindowProgramming\\" + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    nameLabel.configure(text=fnameList[num])  

def clickPrev():
    global num, photo, nameLabel  
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(file="C:\\Users\\태은\\Desktop\\파이썬\\python\\WindowProgramming\\" + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    nameLabel.configure(text=fnameList[num])

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text="<< 이전", command=clickPrev)
btnNext = Button(window, text="다음 >>", command=clickNext)

photo = PhotoImage(file="C:\\Users\\태은\\Desktop\\파이썬\\python\\WindowProgramming\\" + fnameList[0])
pLabel = Label(window, image=photo)

nameLabel = Label(window, text=fnameList[0])

btnPrev.place(x=200, y=10)
nameLabel.place(x=320, y=15)
btnNext.place(x=450, y=10)
pLabel.place(x=15, y=50)

window.mainloop()