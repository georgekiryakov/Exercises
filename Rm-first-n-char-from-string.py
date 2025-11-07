#Write a Python code to remove characters from a string from 0 to n and return a new string.
#Note: n must be less than the length of the string.

def remove_chars(word, n):
    # write your code
    if n <= len(word):
        word_slice = word[n:]  # Remove characters from index 0 to n
        print("New string after removing characters:", word_slice)
    else:
        print("Error: Number must be less than the length of the word.")

remove_chars(word = input("Enter a string: "), n = int(input("Enter the number of characters to remove: ")))