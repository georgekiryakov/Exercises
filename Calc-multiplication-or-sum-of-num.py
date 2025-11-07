#Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

class Solution:
    def __init__(self):

        self.number1 = int(input("Enter the first number: "))
        self.number2 = int(input("Enter the second number: "))

    def product_or_sum(self):

        product = self.number1 * self.number2

        if product <= 1000:
            print(f"Multiplication is equal to: {product}")
        else:
            product = self.number1 + self.number2
            print(f"Sum is equal to: {product}")

Solution().product_or_sum()