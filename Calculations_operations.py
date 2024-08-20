# Create our x and y variables
x = 3
y = 5
# Addition problem
addition = x + y
print (" x + y = " + str(addition))
# Subtraction problem
subtraction = x - y
print ("x - y = " + str(subtraction))
# Multiplication problem
Multiplication = x * y
print (" x * y =" + str(Multiplication))
# Division problem
Division = x/y
print (" x / y =" + str(Division))
# Modulus problem
Modulus = x%y
print (" x % y =" + str(Modulus))
# Floor division problem
Floor_Division = x//y
print (" x // y = " + str(Floor_Division))
# Exponent problem
Exponent = x ** y
print ("x ** y =" + str(Exponent))
# Order of operations problem without parenthesis
operation_no_parenthesis = x + y * x % y / x // y ** x
print ("x + y * x % y / x // y ** x = " + str(operation_no_parenthesis))
# Order of operations problem with parenthesis
operations_with_parenthesis = ((x % y) + x//y ) - ((x ** y)/ x - y)
print ("((x % y) + x//y ) - ((x ** y)/ x - y) = " + str(operations_with_parenthesis))