# This program is for finding greatest common divisor.
# Input is a and b, both of the are integers. Then it will return the gcd.

def gcd(a,b):
    num1 = a
    num2 = b
    while b > 0:
        q = a / b
        r = a - q * b
        a = b
        b = r
    res = 'The GCD between ' + str(num1) + ' and ' + str(num2) + ' is ' + str(a)
    return res

# Call the gcd(a,b) with input. For example like this one below.
# gcd(15,9);

# Or you could try this main program. Change a and b therefore run the code.
a = 30 # Change this as your first input
b = 3098647 # Change thisbas your second input
num1 = a
num2 = b
while b > 0:
    q = a / b
    r = a - q * b
    a = b
    b = r
res = 'The GCD between ' + str(num1) + ' and ' + str(num2) + ' is ' + str(a)
print res 
# This is the result
