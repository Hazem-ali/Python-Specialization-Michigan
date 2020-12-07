import re

numbers = []
with open(input("Enter File Name: ")) as file:
    for line in file:
        num = re.findall('[0-9]+', line)
        if num:
            for i in range(len(num)):
                numbers.append(int(num[i]))

print(numbers)
