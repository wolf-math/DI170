# Create another file called calculator.py, and import the operators module. Call the 2 functions and display the results


# Do this process 3 times :

# once by importing the whole module
import operators

print(operators.addOperator(9,7))
print(operators.divideOperator(9,7))
# the second time by importing specific functions
from operators import addOperator, divideOperator

print(addOperator(9,7))
print(divideOperator(9,7))
# the third time by using alias
from operators import addOperator as add, divideOperator as divide

print(add(9,7))
print(divide(9,7))