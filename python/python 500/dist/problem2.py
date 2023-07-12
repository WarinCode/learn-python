# %% [markdown]
# <h1>บทที่ 2 (Print Command)</h1>
# <style>
#     h1{
#         text-align:center;
#     }
# </style>

# %% [markdown]
# <h4>Print String</h4>
# <hr>

# %%
# ข้อ 1
print("Hello")

# %%
# ข้อ 2
print("Hello World")

# %%
# ข้อ 3
print("hello_python")

# %%
# ข้อ 4
print("Merry X'Mas")

# %%
# ข้อ 6
print('I want to ask you "Why don\'t you drive to work"')

# %%
# ข้อ 7
print("You got a ne job !? That's so exciting")

# %%
# ข้อ 8
print("สวัสดีวันจันทร์")

# %%
# ข้อ 9
print("ความแตกต่างระหว่างนเก่งกับคนไม่เก่ง คือ \"การใช้เวลาว่างให้เ็นระโยชน์\"")

# %%
# ข้อ 10
print("/\\/\\/\\")

# %%
# ข้อ 11
print("a" , "an" , "ant" ,sep="\n")

# %%
# ข้อ 12
print('''
\t*\t\n
*\t*\t*\t\n
\t*\t
      ''')

# %%
# ข้อ 13
print('''
*\t+\t*\n
+\t*\t+\n
*\t+\t*
      ''')

# %%
# ข้อ 14
print('Just becaue something')
print('thinks differently from you.')
print('does that mean it\'s not thinking ?')

# %%
# ข้อ 15
print('''
\\\t\t\t\t/\n
\t\tx\n      
/\t\t\t\t\\
      ''')

# %% [markdown]
# <h4>Print Numeric</h4>
# <hr>

# %%
# ข้อ 16
print(25)

# %%
# ข้อ 17
print(f'{100:.6f}')

# %%
# ข้อ 18
import math as m 
print(m.pi)

# %%
# ข้อ 19
a = 2
print(a)

# %%
# ข้อ 20
a = 12.5
print(a)

# %% [markdown]
# <h4>Print String + Numeric</h4>
# <hr>

# %%
# ข้อ 21
a = 2
b = 3
print(a , 'x' , b , '=' , a * b , sep=" ")

# %%
# ข้อ 22
print(f'{a} + {b} = {b} + {a} = {a + b}')

# %%
# ข้อ 23
c = 5
print(f'{a}*({b} + {c}) = {a}*{b} + {a}*{c}')

# %%
# ข้อ 24
a = 2.4
b = 2.5
print(f'{a} + {b} = {a + b:.4f}')

# %%
# ข้อ 25
a = 5
b = 2
print(f'{a:.2f} - {b:.2f} = {a - b:.4f}')

# %%
# ข้อ 26
brithday = 25
print('ฉันเกิดวันที่' , brithday , 'ธันวาคม')

# %%
# ข้อ 27
a = 5
b = 100
print(f'{a} เท่าของ {b} มีค่าเท่ากับ {b * a}')

# %%
# ข้อ 28
a = 3.5
print('เขามีเงินเยอะกว่าฉัน' , format(a , ".2f") , 'บาท')

# %%
# ข้อ 29
a = 5
print('ฉันได้กำไร' , f'{a}%')

# %%
# ข้อ 30
a = 2
b = 3.5
print(f'เมื่อวานนี้ฉันขาดทุน {a}% วันนี้ฉันได้กำไร {b:.2f}%')


 