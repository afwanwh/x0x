# This program is for finding greatest common divisor.
# Input is a and b, both of the are integers. Then it will return the gcd.


def gcd(a, b):
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
number1 = raw_input('Type your first number: ')
number2 = raw_input('Type your second number: ')
print gcd(int(number1), int(number2))
