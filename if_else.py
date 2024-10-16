# num_1
num: float = float(input("enter a decimal number:"))
print(f"The result is: {(num - 10) if num > 10 else (num * 10)}")
#

# num_2
sum_up: int = 0
l: list[int] = [sum_up := sum_up + int(input("enter a number:")) for _ in range(3)]
print(f"The sum is {sum_up if sum_up > 100 else f"smaller than 100"}")
#

# num_3 bonus
num_1: float = float(input("enter a decimal number:"))
num_2: float = float(input("enter a decimal number:"))
print(
    f"The fraction is:{"same" if (num_1 - num_1 // 1) == (num_2 - num_2 // 1) else {num_1 if (num_1 - num_1 // 1) > (num_2 - num_2 // 1) else num_2} } ")
#

# num_4
age: int = int(input("enter your age:"))
print(f"The age is: {age if 0 < age < 120 else "Incorrect"}")
#

# num_5
num: int = int(input("enter a 3 digit number:"))
print(num // 10 - num // 100 * 10)
#
