from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    key = event.keysym  

    # 방향키만 처리
    if key in ['Left', 'Right', 'Up', 'Down']:
        messagebox.showinfo("키보드 이벤트", "눌린 키 : " + key)

window = Tk()
window.bind("<Key>", keyEvent)
window.mainloop()