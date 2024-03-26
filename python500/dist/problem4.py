# %% [markdown]
# <h1 style="text-align:center;">บทที่ 4 (Data Structure)</h1>
# 

# %% [markdown]
# <h5>Numeric</h5>
# <hr>
# 
 
# %%
# ข้อ 1
numeric1 = 5
print(5)
print(type(numeric1))

# %%
# ข้อ 2
numeric2 = -3
print(numeric2)
print(type(numeric2))

# %%
# ข้แ 3
numeric3 = 0
print(numeric3)
print(type(numeric3))

# %%
# ข้อ 4
_input = int(input("รับค่า >>> "))
print(_input)
print(type(_input))

# %%
# ข้อ 5
numeric1 = 5.0
print(numeric1)
print(type(numeric1))

# %%
# ข้อ 6
numeric2 = -3.1
print(numeric2)
print(type(numeric2))

# %%
# ข้อ 7
numeric3 = 0.0
print(numeric3)
print(type(numeric3))

# %%
# ข้อ 8
_input2 = input("รับค่าตัวเลขจำนวนจริง >>> ")
_input2 = int(_input2)
print(_input2)
print(type(_input2))

# %%
# ข้อ 9
int1 = int(input("จำนวนเต็มตัวที่ 1 >> "))
int2 = int(input("จำนวนเต็มตัวที่ 2 >> "))

plus = int1 + int2
minus = int1 - int2
multiply = int1 * int2
divide = int1 / int2

print(f"ค่าตัวแปรที่ 1 = {int1} \nค่าตัวแปรที่ 2 = {int2}")
print(f"ชนิดข้อมูลตัวที่ 1 คือ {type(int1)} \nชนิดข้อมูลตัวที่ 2 คือ {type(int2)}")
print(f"int1 + int2 = {plus}")
print(f"int1 - int2 = {minus}")
print(f"int1 * int2 = {multiply}")
print(f"int1 / int2 = {divide}")

# %%
# ข้อ 10
fl1 = float(input("ทศนิยมตัวที่ 1 >> "))
fl2 = float(input("ทศนิยมตัวที่ 2 >> "))

print(f"ค่าตัวแปรที่ 1 = {fl2} \nค่าตัวแปรที่ 2 = {fl2}")
print(f"ชนิดข้อมูลตัวที่ 1 คือ {type(fl1)} \nชนิดข้อมูลตัวที่ 2 คือ {type(fl2)}")
print(f"{fl1} + {fl2} = {fl1 + fl2}")
print(f"{fl1} - {fl2} = {fl1 - fl2}")
print(f"{fl1} * {fl2} = {fl1 * fl2}")
print(f"{fl1} / {fl2} = {fl1 / fl2}")

# %%
# ข้อ 11
_int = int(input("จำนวนเต็ม >> "))
_float = float(input("ทศนิยม >> "))

print(f"จำนวนเต็ม = {_int}")
print(f"ทศนิยม = {_float}")
print(f"ชนิดข้อมูลของ _int คือ {type(_int)} \nชนิดข้อมูลของ _float คือ {type(_float)}")
print(f"{_int} + {_float} = {_int + _float}")
print(f"{_int} - {_float} = {_int - _float}")
print(f"{_int} * {_float} = {_int * _float}")
print(f"{_int} / {_float} = {_int / _float}")

# %%
# ข้อ 12
logic1 = True
print("ต่าของ logic1 = ", logic1)
print("ชนิดข้อมูลของ logic1", "คือ", type(logic1), sep=" ")

# %%
# ข้อ 13
logic2 = False
print("ต่าของ logic2 = ", logic2)
print("ชนิดข้อมูลของ logic1", "คือ", type(logic2), sep=" ")

# %%
# ข้อ 14
logic1 = True
logic2 = False
print(logic1 and logic2)

# %%
# ข้อ 15
logic1 = True
logic2 = False
print(logic1 or logic2)

# %%
# ข้อ 16
complex1 = 1 + 2j
print(f"ค่าของ complex1 = {complex1}")
print(f"ชนิดข้อมูล complex1 = {type(complex1)}")

# %%
# ข้อ 17
complerx1 = 1 + 2j
print(f"ค่าจริงของ complex1 คือ {complerx1.real}")

# %%
# ข้อ 18
complex1 = 1 + 2j
print(f"จำนวนจินตภาพ complex1 = {complex1.imag}")

# %% [markdown]
# <h4>String</h4>
# <hr>
# 

# %%
# ข้อ 19
string1 = "Python"
print(string1)
print(type(string1))

# %%
# ข้อ 20
string1 = "Python"
print(string1[0])

# %%
# ข้อ 21
string1 = "Python"
print(string1[1])

# %%
# ข้อ 22
string1 = "Pytohn"
print(string1[-1])

# %%
# ข้อ 23
string1 = "Python"
print(string1[-2])

# %%
# ข้อ 24
string1 = "Python"
print(string1[2])

# %%
# ข้อ 25
string1 = "Python"
print(string1[3])

# %%
# ข้อ 26
string1 = "Python"
s = string1
print(f"s[1] = {s[1]}")
print(f"s[2] = {s[2]}")
print(f"s[3] = {s[3]}")

# %%
# ข้อ 27
string1 = "Python"
s = string1
print(f"s[2] = {s[2]}")
print(f"s[1] = {s[1]}")
print(f"s[0] = {s[0]}")
print(f"s[-1] = {s[-1]}")
print(f"s[-2] = {s[-2]}")

# %%
# ข้อ 28
string1 = "Python"
s = string1
print(f"s[2] = {s[2]}")
print(f"s[1] = {s[1]}")
print(f"s[0] = {s[0]}")
print(f"s[-1] = {s[-1]}")

# %%
# ข้อ 29
string1 = "Python"
for i in range(-4, 4 + 1, 1):
    print(f"string[{i}] = {string1[i]}")

# %%
# ข้อ 30
string1 = "Python"
for i in range(-6, 4 + 1, 1):
    print(f"string[{i}] = {string1[i]}")

# %%
# ข้อ 31
string1 = "Python"
for i in range(-4, -2 + 1):
    print(f"string[{i}] = {string1[i]}")

# %%
# ข้อ 32
_str = input("ข้อความ >>> ")
print(f"อักขระของคุณคือ {_str}")
print(f"ความยาวของอักขระคือ {_str.__len__()}")

# %%
# ข้อ 33
_str = input("ข้อความ >>> ")
strIndex = _str.find("ก")


def covertToBoolean(b):
    myBool = bool(b)
    return myBool


if strIndex == -1:
    strIndex = 0
else:
    strIndex = 1

txt = ""
if covertToBoolean(strIndex):
    txt = "มี"
else:
    txt = "ไม่มี"

print(f"ข้อความของคุณคือ {_str}")
print(f'ข้อความนี้มี "ก" หรือไม่ = {txt}({covertToBoolean(strIndex)})')

# %%
# ข้อ 34
s1 = input("ข้อความที่ 1 >> ")
s2 = input("ข้อความที่ 2 >> ")

print(f"1.) {s1}")
print(f"2.) {s2}")
print(f"{s1} อยู่ใน {s2} = {s1 in s2}")

# %%
# ข้อ 35
sInput = input("ข้อความ >> ")
print(f"ข้อความเก่า {sInput}")
sInput = sInput.replace("a", "A")
print(f"ข้อความใหม่ {sInput}")

# %%
# ข้อ 36
sInput = input("ข้อความ >> ")
print(f"sInput = {sInput}")
string2 = sInput.replace("a", "A")
print(f"string2 = {string2}")

# %%
# ข้อ 37
sentence = input("บทสนทนา >> ")
print(sentence)
sentence = sentence.split(" ")
print(sentence)

# %%
# ข้อ 38
sentence = input("บทสนาทนา >> ")
c = input("")
print(sentence)
sentence = sentence.split(c)
print(sentence)

# %%
# ข้อ 39
str1 = input("ข้อความที่ 1 >> ")
str2 = input("ข้อความที่ 2 >> ")
concatStr = str1 + str2
print(f"str1 = {str1}\nstr2 = {str2}\nรวมกันได้ = {concatStr}")

# %% [markdown]
# <h4>List</h4>
# <hr>
# 

# %%
# ข้อ 40
li = [0, 1, 2, "a", "b", "c"]
print(li)

# %%
# ข้อ 41
list1 = [0, 1, 2, "a", "b", "c"]
print(list1[2])

# %%
# ข้อ 42
list1 = [0, 1, 2, "a", "b", "c"]
print(list1[-3])

# %%
# ข้อ 43
list1 = [0, 1, 2, "a", "b", "c"]
print(list1[0])

# %%
# ข้อ 44
list1 = [0, 1, 2, "a", "b", "c"]
print(list1[list1.index("b")])

# %%
# ข้อ 45
list1 = [0, 1, 2, "a", "b", "c"]
for i in range(2, 3 + 1):
    print(list1[i])

# %%
# ข้อ 46
list1 = [0, 1, 2, "a", "b", "c"]
for j in range(1, -2 - 1, -1):
    print(list1[j])

# %%
# ข้อ 47
list1 = [0, 1, 2, "a", "b", "c"]
list1.pop(-1)
list1.pop(0)
print(list1)

# %%
# ข้อ 48
list1 = [0, 1, 2, "a", "b", "c"]
for k in range(2, 0 - 1, -1):
    list1.pop(k)
print(list1)

# %%
# ข้อ 49
list1 = [0, 1, 2, "a", "b", "c"]
newList = []
for i in range(0, 3):
    newList.append(list1[i])
list1 = newList
print(list1)

# %%
# ข้อ 50
list2 = ["and", "bird", "cat", "dog", "eagle"]
index = list2.index("dog")
list2[index] = "duck"
print(list2)

# %%
# ข้อ 51
list2 = ["and", "bird", "cat", "dog", "eagle"]
list2[0] = "ape"
print(list2)

# %%
# ข้อ 52
list2 = ["and", "bird", "cat", "dog", "eagle"]
list2.append("fish")
print(list2)

# %%
# ข้อ 53
empty_list = []
for i in range(0, 3):
    _str = input(f"ข้อความที่ {i + 1} >> ")
    empty_list.append(_str)
print(empty_list)

# %%
# ข้อ 54
list3 = ["apple", "cherry", "eggfruit"]
list3.insert(1, "banana")
print(list3)

# %%
# ข้อ 55
list3 = ["apple", "banana", "cherry", "eggfruit"]
list3.insert(-2, "kiwi")
print(list3)

# %%
# ข้อ 56
list4 = [0, 4, 2, 3, 1]
list4.sort()
print(list4)

# %%
# ข้อ 57
list4 = [0, 4, 2, 3, 1]
list4.sort()
list4.reverse()
print(list4)

# %%
# ข้อ 58
list4 = [0, 4, 2, 3, 1]
sorted_list4 = sorted(list4)
print(sorted_list4)

# %%
# ข้อ 59
list4 = [0, 4, 2, 3, 1]
sorted_list4 = sorted(list4, reverse=True)
print(sorted_list4)

# %%
# ข้อ 60
list5 = ['d','a','c','b','e']
list5.sort()
print(list5)

# %%
# ข้อ 61
list5 = ['d','a','c','b','e']
list5.sort(reverse=True)
print(list5)

# %%
# ข้อ 62
list1 = ['a','b','c']
list2 = [0,1,2]
for item in list2:
    list1.append(item)
print(f'{list1} \n{list2}')

# %%
# ข้อ 63
list1 = ['a','b','c']
list2 = [0,1,2]
list2.extend(list1)
print(f'{list1} \n{list2}')

# %%
# ข้อ 64
list1 = [1,2,3,1,2,3]
del list1[1]
print(list1)

# %%
# ข้อ 65
list1 = [1,2,3,1,2,3]
while True:
    if(3 in list1):
        idx = list1.index(3)
        del list1[idx]
    else: break
print(list1)

# %%
# ข้อ 66
list1 = [1,2,3,1,2,3]
list1.remove(1)
print(list1)

# %%
# ข้อ 67
list1 = [1,2,3,1,2,3]
while 1 in list1:
    list1.remove(1)
print(list1)

# %%
# ข้อ 68
list1 = [1,2,3,1,2,3]
list1.clear()
print(list1)

# %%
# ข้อ 69
list1 = [1,2,3,'a','b','c']
print(len(list1))

# %%
# ข้อ 70
list1 = [*range(1,5+1)]
_input = int(input('ตัวเลข >> '))
_bool = list1.__contains__(_input) # _bool = _input in list1
print(_bool)

# %% [markdown]
# <h4>Tuple</h4>
# <hr>

# %%
# ข้อ 71
tu = tuple(['America' , 'Brazil' , 'China' , 'Do-minican' , 'Egypt'])
print(tu)
print(type(tu))

# %%
# ข้อ 72
tu = ('America' , 'Brazil' , 'China' , 'Do-minican' , 'Egypt')
print(tu[1])

# %%
# ข้อ 73
print(tu[-2])

# %%
# ข้อ 74
tuple1 = tu
print(tuple1[2])

# %%
# ข้อ 75
print(tuple1[-1])

# %%
# ข้อ 76
tuple2 = ('one' , 'two' , 'three' , 1 , 2 , 3)
for i in range(1 , 3 + 1):
    print(f'index ที่ {i} ของ tuple2 คือ {tuple2[i]}')

# %%
# ข้อ 77
for j in tuple2[2:]: print(j , end=' ')

# %%
# ข้อ 78
li = ['three' , 1]
k = 0
while k < li.__len__():
    idx = tuple2.index(li[k])
    print(tuple2[idx])
    k += 1

# %%
# ข้อ 79
print(tuple2[0 : 2 + 1])

# %%
# ข้อ 80
print(tuple2[3:])

# %%
# ข้อ 81
tuple3 = ('one','two','three','four','five')
print(len(tuple3))

# %%
# ข้อ 82
str1 = input("")
boo = str1 in tuple3
print(f'{str1} อยู่ใน Tuple3') if boo else print(f'{str1} ไม่อยู่ใน Tuple3')
print(boo)

# %% [markdown]
# <h4>Dictionary</h4>
# <hr>

# %%
# ข้อ 83
dic = {
    'first_name': 'John',
    'last_name': 'Doe'
}
print(dic , type(dic))

# %%
# ข้อ 84
print(dic["first_name"])

# %%
# ข้อ 85
print(dic["last_name"])

# %%
# ข้อ 86
print(dic.keys())

# %%
# ข้อ 87
l = list(dic.values())
print(l)

# %%
# ข้อ 88
dict1 = dic
dict1["first_name"] = "Jane"
print(dict1)

# %%
# ข้อ 89
dict1["age"] = 32
print(dict1)

# %%
# ข้อ 90
dict1["age"] = 32
dict1['hobby'] = ['coding' , 'studying']
print(dict1)

# %%
# ข้อ 91
dictionary = {}
str1 = input("Key of dictionary >> ")
str2 = input("Value of dictionary >> ")
dictionary[str1] = str2
print(dictionary)

# %%
# ข้อ 92
dict1 = {
    'first_name': 'John ', 
    'last_name': 'Doe', 
    'age': 32
}
del dict1['age']
print(dict1)

# %%
# ข้อ 93
dict1 = {
    'first_name': 'John', 
    'last_name': 'Doe', 
    'age': 32
}
dict1.clear()
print(dict1)

# %%
# ข้อ 94
dict1 = {
    'first_name': 'John', 
    'last_name': 'Doe', 
    'age': 32
}
print(len(dict1))

# %%
# ข้อ 95
def checkKeys():
    str1 = input("รับค่า >> ")
    boo = str1 in dict1
    print(f"{str1} อยู่ใน dict1" if boo else f"{str1} ไม่อยู่ใน dict1")
    print(boo)
    
checkKeys()
checkKeys()

# %%
# ข้อ 96
str1 = input("รับค่า >> ")
li = list(dict1.values())
print(li)
print(str1 in li)

# %% [markdown]
# <h4>Set</h4>
# <hr>

# %%
# ข้อ 97
s = {1,2,3,'i','ii','iii'}
print(s , type(s))

# %%
# ข้อ 98
print(*s , sep=' , ')

# %%
# ข้อ 99
s.add('iv')
print(s)

# %%
# ข้อ 100
s.add(1)
print(s)

# %%
# ข้อ 101
emp_set = set({})
for i in range(1 , 4):
    str1 = input(f"รับค่าข้อมูล set ตัวที่ {i}")
    emp_set.add(str1)
print(emp_set)

# %%
# ข้อ 102
emp_set = set({})
for i in range(1 , 4):
    str1 = input(f"รับค่าข้อมูล set ตัวที่ {i}")
    emp_set.update(str(str1))
new_set = emp_set 
print(new_set)

# %%
# ข่้อ 103
set1 = {1,2,3,'i','ii','iii'}
set1.discard('i')
print(set1)

# %%
# ข้อ 104
set1 = {1,2,3,'i','ii','iii'}
print(set1.__len__())

# %%
# ข้อ 105
int1 = int(input("ตัวเลข >> "))
print(set1.__contains__(int1))


# %%
# ข้อ 106
set1 ={ *range(1,5 + 1) }
set2 = { *range(3,6 + 1) }
result = set1.union(set2)
print(result)

# %%
# ข้อ 107
result = set1.intersection(set2)
print(result)

# %%
# ข้อ 108
print(set1 - set2)

# %%
# ข้อ 109
print(set2 - set1)

# %%
# ข้อ 110
print(set1.symmetric_difference(set2))


