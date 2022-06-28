# This program is for finding greatest common divisor.
# Input is a and b, both of the are integers. Then it will return the gcd.


def gcd(a, b):
    if isinstance(a, int) and isinstance(b, int):
        num1 = a
        num2 = b
        while b > 0:
            q = a / b
            r = a - q * b
            a = b
            b = r
        res = 'The GCD between ' + str(num1) + ' and ' + str(num2) + ' is ' + str(a)
    else:
        res = 'One of your inputs is not integer'
    return res

# Call the gcd(a,b) with input.
print '##############################################################################'
print 'Welcome to GCD 1.0'
print 'This program is for finding greatest common divisor.'
print 'Input is two numbers, both of the are integers. Then it will return the gcd.'
print '##############################################################################\n'
number1 = raw_input('Type your first number: ')
number2 = raw_input('Type your second number: ')
print '\n=============================================================================='
try:
    print gcd(int(number1), int(number2))
except ValueError:
    print 'One of your inputs is not integer.'
    print 'Please give integer input(s).'
print '=============================================================================='
