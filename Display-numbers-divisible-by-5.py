#Write a Python code to display numbers from a list divisible by 5

#Given list is  [10, 20, 33, 46, 55]
#10, 20, 55

numbers = [10, 20, 33, 46, 55]

for number in numbers:
    if number % 5 == 0:
        print(number)
# Output: 10, 20, 55