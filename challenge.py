# num_16
num: int = int(input("enter a 3 digit number:"))
sum_up: int = 0
while num > 0:
    sum_up += num % 10
    num /= 10
if sum_up % 3 == 0:
    print(f"The number divisible by 3")
else:
    print(f"The number not divisible by 3")
#

# num_17
string: str = input("enter a string:")
length: int = len(string)
half: int = length // 2
bool_list: list[bool] = []
location: int = -1
for letter in string[:half]:
    if letter == string[location]:
        location += -1
        bool_list.append(True)
    else:
        bool_list.append(False)
if all(bool_list):
    print(string[::-1])
else:
    print("The string does not turn over")
#
