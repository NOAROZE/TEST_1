# num_11
SENTINEL: int = 0
sum_up: int = 0
while True:
    num: int = int(input("enter a number:"))
    if num == SENTINEL:
        break
    if num < 0:
        sum_up += num
print(sum_up)
#

# num_12
numbers: list[int] = [int(input("enter a number:")) for i in range(10)]
print(numbers)
print(numbers[::-1])
#

# num_13
divider: int = 2
SENTINEL: int = 0
counter: int = 0
while True:
    num: int = int(input("enter a number:"))
    if num == SENTINEL:
        break
    elif num == 1:
        continue
    while divider <= num ** 0.5:
        if num % divider == 0:
            break
        divider += 1
    else:
        counter += 1
    divider = 2
print(counter)
#

# num_14
numbers: list[int] = []
sum_up: int = 0
counter: int = 0
for i in range(5):
    num: int = int(input("enter a number:"))
    sum_up += num
    numbers.append(num)
print(f"The average of numbers is: {sum_up / 5}")
for num in numbers:
    if num > sum_up / 5:
        counter += 1
print(counter)
#

# num_15
num1: int = int(input("enter a number:"))
num2: int = int(input("enter a number:"))
save_num1: int = num1
save_num2: int = num2
counter: int = 0
if num1 <= num2:
    while num1 < num2:
        counter += 1
        num1 += save_num1

else:
    while num2 <= num1:
        counter += 1
        num2 += save_num2
print(f"The result is: {counter}")
#
