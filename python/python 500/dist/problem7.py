# %% [markdown]
# <h1 style="text-align: center;">บทที่ 7 IF-ELSE(CODE-FLOWCHART)</h1>
# <hr>

# %%
# สร้างตัวแปร

# สร้างเงื่อนไข
myBool = bool(True or False)
condition1 = myBool
condition2 = myBool
condition3 = myBool
condition4 = myBool
condition5 = myBool
condition6 = myBool
condition7 = myBool

# สร้างตัวดำเนินการ
isEmpty = None
operation1 = isEmpty
operation2 = isEmpty
operation3 = isEmpty
operation4 = isEmpty
operation5 = isEmpty
operation6 = isEmpty
operation7 = isEmpty
operation8 = isEmpty
operation9 = isEmpty
operation10 = isEmpty
operation11 = isEmpty
operation12 = isEmpty
operation13 = isEmpty
operation14 = isEmpty
operation15 = isEmpty
operation16 = isEmpty
operation17 = isEmpty


# %%
# ข้อ 1
if condition1:
    operation1
else:
    operation2
operation3
operation4

# %%
# ข้อ 2
if condition1:
    operation1
else:
    operation2

# %%
# ข้อ 3
if condition1:
    operation1
operation2

# %%
# ข้อ 4
if condition1:
    operation1

# %%
# ข้อ 5
if condition1:
    operation1
elif condition2:
    operation2
else:
    operation3
    operation4
operation5

# %%
# ข้อ 6
if condition1:
    operation1
elif condition2:
    operation2
else:
    operation3

# %%
# ข้อ 7
if condition1:
    operation1
elif condition2:
    operation2
elif condition3:
    operation3
else:
    operation4
operation5

# %%
# ข้อ 8
if condition1:
    operation1
elif condition2:
    operation2
elif condition3:
    operation3
else:
    operation4
    operation5

# %%
# ข้อ 9
if condition1:
    operation1
elif condition2:
    operation2
operation3

# %%
# ข้อ 10
if condition1:
    operation1
elif condition2:
    operation2

# %%
# ข้อ 11
if condition1:
    operation1
elif condition2:
    operation2
elif condition3:
    operation3
    operation4
operation5

# %%
# ข้อ 12
if condition1:
    operation1
elif condition2:
    operation2
elif condition3:
    operation3

# %%
# ข้อ 13
if condition1:
    if condition2:
        operation1
    else:
        operation2
else:
    operation3
    if condition3:
        operation4
    elif condition4:
        operation5
    else:
        operation6
operation7

# %%
# ข้อ 14
if condition1:
    if condition2:
        operation1
    elif condition3:
        operation2
    else:
        operation3
    operation4
else:
    operation5
    if condition4:
        operation6
        operation7
    else:
        operation8
operation9

# %%
# ข้อ 15
if condition1:
    if condition2:
        operation1
        operation2
    operation3
    operation4
else:
    if condition3:
        operation5
    elif condition4:
        operation6
    else:
        operation7
        operation8
    operation9
operation10

# %%
# ข้อ 16
if condition1:
    if condition2:
        operation1
    elif condition3:
        operation2
else:
    if condition4:
        operation3
    elif condition5:
        operation4
    operation5
operation6

# %%
# ข้อ 17
if condition1:
    operation1
    if condition2:
        operation2
    else:
        operation3
    operation4
operation5
operation6

# %%
# ข้อ 18
if condition1:
    operation1
    operation2
    if condition2:
        operation3
    elif condition3:
        operation4
    else:
        operation5
    operation6
    operation7
operation8

# %%
# ข้อ 19
if condition1:
    if condition2:
        operation1
    else:
        operation2
elif condition3:
    if condition4:
        operation3
    else:
        operation4
        operation5
    operation6
else:
    operation7
    if condition5:
        operation8
    operation9
operation10

# %%
# ข้อ 20
if condition1:
    operation1
    if condition2:
        operation2
elif condition3:
    if condition4:
        operation3
    else:
        operation4
    operation5
    operation6
else:
    operation7
    if condition5:
        operation8
        operation9
    else:
        operation10
operation11

# %%
# ข้อ 21
if condition1:
    operation1
    if condition2:
        operation2
        operation3
    elif condition3:
        operation4
        operation5
    else:
        operation6
        operation7
elif condition4:
    if condition5:
        operation8
    else:
        operation9
    operation10
else:
    operation11
    if condition6:
        operation12
    else: 
        operation13
        operation14
    operation15
operation16
operation17

# %%
# ข้อ 22
if condition1:
    if condition2:
        operation1
    elif condition3:
        operation2
    else:
        operation3
elif condition4:
    if condition5:
        operation4
        operation5
    elif condition6:
        operation6
    else:
        operation7
    operation8
    operation9
else: 
    operation10
    if condition7:
        operation11
    else:
        operation12
        operation13
    operation14
operation15

# %%
# ข้อ 23
if condition1:
    operation1
    operation2
    if condition2:
        operation3
    elif condition3:
        operation4
        operation5
    operation6
    operation7
elif condition4:
    if condition5:
        operation8
        operation9
else:
    if condition6:
        operation10
    elif condition7:
        operation11
operation12
operation13

# %%
# ข้อ 24 
if condition1:
    if condition2:
        operation1
elif condition3:
    if condition4:
        operation2
else:
    if condition5:
        operation3
    operation4
operation5

# %%
# ข้อ 25
if condition1:
    operation1
    if condition2:
        operation2
    else:
        operation3
        operation4
elif condition3:
    if condition4:
        operation5
    elif condition5:
        operation6
    else:
        operation7
    operation8
operation9

# %%
# ข้อ 26
if condition1:
    if condition2:
        operation1
    elif condition3:
        operation2
    operation3
elif condition4:
    operation4
    if condition5:
        operation5
    else:
        operation6
    operation7
operation8

# %%
# ข้อ 27
if condition1:
    if condition2:
        operation1
elif condition3:
    if condition4:
        operation2
    elif condition5:
        operation3
        operation4
    else:
        operation5
operation6

# %%
# ข้อ 28
if condition1:
    operation1
    if condition2:
        operation2
    else:
        operation3
    operation4
    operation5
elif condition3:
    operation6
    operation7
    if condition4:
        operation8
    elif condition5:
        operation9
    operation10
    operation11
operation12

# %%
# ข้อ 29
if condition1:
    if condition2:
        operation1
        operation2
        if condition3:
            operation3
    else:
        operation4
        if condition4:
            operation5
    operation6
else: 
    operation7
    operation8
    if condition5:
        if condition6:
            operation9
        else:
            operation10
        operation11
    else:
        operation12
        if condition7:
            operation13
operation14

# %%
# ข้อ 30
if condition1:
    if condition2:
        operation1
        operation2
        if condition3:
            operation3
    else:
        operation4
        if condition4:
            operation5
        else:
            operation6
    operation7
operation8


