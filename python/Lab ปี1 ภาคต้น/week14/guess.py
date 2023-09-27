import tkinter as tk

from tkinter import messagebox , ttk , Label
from random import randint

root = tk.Tk()
root.title("Fundamental Tkinter")
root.geometry('550x180')

randNum = randint(1,10)
showCount = tk.StringVar()
counter = 0

def btn_clicked(theNum):
    global showCount
    global counter
    counter += 1    
    showCount.set(counter)
    if theNum == randNum:
        messagebox.showinfo(title="แจ้งเตือน",message=f"{theNum} ถูกต้อง")
    elif theNum > randNum:
        messagebox.showerror(title="แจ้งเตือน",message=f"{theNum} มากเกินไป")
    elif theNum < randNum:
        messagebox.showerror(title="แจ้งเตือน",message=f"{theNum} น้อยเกินไป")
        
def newGame():
    global randNum
    global showCount
    global counter
    counter = 0   
    showCount.set('')
    randNum = randint(1,10)
    messagebox.showinfo(title="แจ้งเตือน", message='เริ่มเล่นเกมใหม่!')
    
btn1 = ttk.Button(root,text='1',command=lambda:btn_clicked(1)).grid(row=1,column=1,padx=15 , pady=10)
btn2 = ttk.Button(root,text='2',command=lambda:btn_clicked(2)).grid(row=1,column=2,padx=15 , pady=10)
btn3 = ttk.Button(root,text='3',command=lambda:btn_clicked(3)).grid(row=1,column=3,padx=15 , pady=10)
btn4 = ttk.Button(root,text='4',command=lambda:btn_clicked(4)).grid(row=2,column=1,padx=15 , pady=10)
btn5 = ttk.Button(root,text='5',command=lambda:btn_clicked(5)).grid(row=2,column=2,padx=15 , pady=10)
btn6 = ttk.Button(root,text='6',command=lambda:btn_clicked(6)).grid(row=2,column=3,padx=15 , pady=10)
btn7 = ttk.Button(root,text='7',command=lambda:btn_clicked(7)).grid(row=3,column=1,padx=15 , pady=10)
btn8 = ttk.Button(root,text='8',command=lambda:btn_clicked(8)).grid(row=3,column=2,padx=15 , pady=10)
btn9 = ttk.Button(root,text='9',command=lambda:btn_clicked(9)).grid(row=3,column=3,padx=15 , pady=10)
playAgain = ttk.Button(root, text='เล่นอีกรอบ?',command=lambda:newGame()).grid(row=4,column=2,padx=15 , pady=10)

label = Label(root , text='จำนวนรอบที่ใช้ในการสุ่ม : ').place(x=330,y=10)
txtAll = ttk.Entry(root,textvariable=showCount)
txtAll.config(width=6 , justify='center')
txtAll.place(x=460,y=10)

root.mainloop()