from tkinter import Tk , StringVar , mainloop , CENTER 
from tkinter.ttk import Label , Entry 
from random import randint

def card():
    card1 = randint(1,13)
    return card1

def point(c1 , c2):
    if c1 > 10:
        c1 = 10
    if c2 > 10:
        c2 = 10
    score = (c1 + c2) % 10
    return score

root = Tk()
root.title("Card 89")

labP1 = Label(root , text='Player 1 : ')
labP2 = Label(root , text='Player 2 :')
labC1 = Label(root , text='Card1')
labC2 = Label(root , text='Card2')
labPoint = Label(root , text='Point')

# player1 card1
p1c1 = StringVar()
txtP1C1 = Entry(root , textvariable=p1c1 , justify=CENTER)

# player1 card2
p1c2 = StringVar()
txtP1C2 = Entry(root , textvariable=p1c2 , justify=CENTER)

# player1 point
p1point = StringVar()
txtP1Point = Entry(root , textvariable=p1point , justify=CENTER)

# player2 card1
p2c1 = StringVar()
txtP2C1 = Entry(root , textvariable=p2c1 , justify=CENTER)

# player2 card2
p2c2 = StringVar()
txtP2C2 = Entry(root , textvariable=p2c2 , justify=CENTER)

# player2 point
p2point = StringVar()
txtP2Point = Entry(root , textvariable=p2point , justify=CENTER)

# Player WIN
pWin = StringVar()
txtPWin = Entry(root , textvariable=pWin , justify=CENTER)

# วางลง Grid
# row0
labC1.grid(column=1,row=0,padx=5,pady=5)
labC2.grid(column=2,row=0,padx=5,pady=5)
labPoint.grid(column=3,row=0,padx=5,pady=5)
#row1
labP1.grid(column=0,row=1,padx=5,pady=5)
txtP1C1.grid(column=1 , row=1 , padx=5 , pady=5)
txtP1C2.grid(column=2 , row=1 , padx=5 , pady=5)
txtP1Point.grid(column=3 , row=1 , padx=5 , pady=5)
#row2
labP2.grid(column=0,row=2,padx=5,pady=5)
txtP2C1.grid(column=1, row=2, padx=5, pady=5)
txtP2C2.grid(column=2, row=2, padx=5, pady=5)
txtP2Point.grid(column=3, row=2, padx=5, pady=5)
#row3
txtPWin.grid(column=1, row=3 ,rowspan=3 , padx=5 , pady=5)

# ใส่ค่าไพ่ และคะแนน
p1c_li = (card() , card())
p2c_li = (card() , card())
# แสดงไพ่ player1
p1c1.set(p1c_li[0])
p1c2.set(p1c_li[1])
p1point.set(point(*p1c_li))
# แสดงไพ่ player2
p2c1.set(p2c_li[0])
p2c2.set(p2c_li[1])
p2point.set(point(*p2c_li))

# แสดงว่าใครชนะ
def winer(p1: int , p2: int) -> None:
    text = ''
    if p1 > p2: text = "Player1 Win!!"
    elif p2 > p1: text = "Player2 Win!!"
    elif p1 == p2: text = "Draw++"
    pWin.set(text) 
    
winer(int(p1point.get()) , int(p2point.get()))
mainloop()