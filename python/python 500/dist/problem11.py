# %% [markdown]
# <h1 style="text-align:center">บทที่ 11 FOR & WHILE LOOP(PROBLEM)</h1>
# <hr>

# %%
# ข้อ 1
for i in range(20): print(i ,end=', ')

# %%
# ข้อ 2
for i in range(19): print(i ,end=', ')

# %%
# ข้อ 3
for i in range(1 ,20): print(i , end=', ')

# %%
# ข้อ 4
for i in range(19 , -1 , -1): print(i , end=', ')

# %%
# ข้อ 5
for i in range(18 , -1 , -1): print(i , end=', ')

# %%
# ข้อ 6
for i in range(19 , 0 ,-1): print(i , end=', ')

# %%
# ข้อ 7
for i in range(-3 , 10): print(i , end=', ')

# %%
# ข้อ 8
for i in range(-9 , 1 , 1): print(i , end=', ')

# %%
# ข้อ 9
for i in range(-5 , -16 ,-1): print(i , end=', ')

# %%
# ข้อ 10
for i in range(-5 , -16 ,-2): print(i , end=', ')

# %%
# ข้อ 11
n = int(input("ตัวเลข >> "))
s = 0
for i in range(1 , n + 1):
    s += i
    print(i , end=' + ') 
print(' = ',s)

# %%
# ข้อ 12
n = int(input("ตัวเลข >> "))
s = 1
for i in range(1 , n + 1):
    s *= i
    print(i , end=' x ')
print('= ',s)

# %%
# ข้อ 13
n = int(input("ตัวเลข >> "))
s = 0
for i in range(1, n + 1):
    s += 1 / i
    print(f'1 / {i}' , end=' + ')
print('= %.2f' %(s))

# %%
# ข้อ 14
n = int(input("ตัวเลข >> "))
s = 0
for i in range(1, n + 1):
    s += 1 / pow(i , 2)
    print(f'1 / {i}^2' , end=' + ')
print('= %.2f' %(s))

# %%
# ข้อ 15
import math

n = int(input("ตัวเลข >> "))
_sum = 1
for i in range(1, n + 1):
    _sum *= 1 / pow(i , 2)
result = math.sqrt(6 * _sum)
print('= %f' %(result))


