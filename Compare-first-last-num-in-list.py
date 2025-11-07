# Check if the first and last numbers of a list are the same
# Write a code to return True if the list’s first and last numbers are the same. 
# If the numbers are different, return False.

list_length = int(input("Choose how long of a list you want to create (1-5): "))

for list_nums in range(list_length):

    if list_nums <= 5:
        list_nums = int(input("Enter a number: "))

        list = []
        list.append(list_nums)
        
        if list [0] == list[4]:
            print("True")

        elif list[0] != list[4]:
            print("False")
    else:
        print("You can only enter up to 5 numbers.")
        break