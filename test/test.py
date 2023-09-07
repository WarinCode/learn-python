# try:
#     a = input("ตัวเลข >> ")
#     b = 1 + int(a)
# except ZeroDivisionError as err:
#     print('Error!' , err)
# except ValueError as err:
#     print(err)
# except TypeError as err:
#     print(err)
# else: print(b)

# class A:
#     sum = 0
#     def __init__(self , *args):
#         self.args = args
#     def x(self):
#         self.sum = sum(self.args)
#         print(f'{self.sum:,}')
# A(*range(1,9000)).x()