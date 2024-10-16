# num_6
num: int = int(input("enter a number greater than 0:"))
while num > 0:
    print(num)
    num -= 1
#

# num_7
num_1: int = int(input("enter a number:"))
num_2: int = int(input("enter a number:"))
if num_1 > num_2:
    if not num_1 % 2 == 0:
        num_1 -= 1
    while num_1 >= num_2:
        print(num_1)
        num_1 -= 2
else:
    if not num_2 % 2 == 0:
        num_2 -= 1
    while num_2 >= num_1:
        print(num_2)
        num_2 -= 2
#

# num_8
num: int = int(input("enter a number greater than 0:"))
while num > 0:
    if num % 5 == 0:
        print(num)
    elif num % 3 == 0:
        print(num)
    num -= 1
#

# num_9
num: int = int(input("enter a number greater than 0:"))
while num > 0:
    if num % 7 == 0:
        print(num)
    num -= 1
#
