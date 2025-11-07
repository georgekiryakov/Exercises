#Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.

for i in range(10):
    if i == 0:
        print(f"Current number: {i}, Previous number: {i}, Sum: {i}")
    else:
        print(f"Current number: {i}, Previous number: {i-1}, Sum: {i + (i-1)}")