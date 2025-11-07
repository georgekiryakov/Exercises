#Write a Python code to accept a string from the user and display characters present at an even index number.
#For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

input_string = input("Enter a string: ")
even_index_chars = [input_string[list] for list in range(len(input_string)) if list % 2 == 0]
print("Characters at even index numbers:", ' '.join(even_index_chars))


