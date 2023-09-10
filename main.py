"""Create a program that reads two integer from the user and display some arithmetic
a+b
a-b
aXb
a/b
a%b
log10 value of a and b using math module
"""

#call log from math

from math import log10

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

#formulas for arithmetic
sum = a+b
difference = a-b
product = a*b
qoutient = a/b
remainder = a%b
result_of_log_a = log10(a)
result_of_log_b = log10(b)

#showing the results

print(f"The sum of {a} and {b} is {sum}.")
print(f"The difference of {a} and {b} is {difference}.")
print(f"The products of {a} and {b} is {product}.")
print(f"The qoutient of {a} and {b} is {qoutient:.2f}.")
print(f"The remainder of {a} and {b} is {remainder:.2f}.")
print(f"The result of log of {a}  is {result_of_log_a:.3f}.")
print(f"The result of log of {b}  is {result_of_log_b:.3f}.")

