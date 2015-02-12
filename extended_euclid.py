# This program is for find two integers as proof of gcd.
# Extended Euclid could be noted s*a + t*b = gcd(a,b). See gcd.py about
# the greatest common divisor.


def ext_euclid(a, b):
    num1 = a
    num2 = b
    s1, s2, t1, t2 = 1, 0, 0, 1
    while b > 0:
       q = a/b
        r = a - q*b
        a = b
        b = r
        s = s1 - q * s2
        s1 = s2
        s2 = s
        t = t1 - q * t2
        t1 = t2
        t2 = t
    res = 'Value of s is ' + str(s1) + '\nValue of t is ' + str(t1) + '\nValue of gcd is ' + str(a)
    print res
    check = s1 * num1 + s2 * num2
    if check == a:
        print 'Extended Euclid is proved'
    else:
        print 'Extended Euclid is not proved'
    return True

print '##############################################################################'
print 'Welcome to Extended Euclid Program 1.0!'
print 'This program is for finding greatest common divisor.'
print 'Input is two numbers, both of the are integers. Then it will prove extended euclid for the gcd.'
print '##############################################################################\n'
number1 = raw_input('Type your first number: ')
number2 = raw_input('Type your second number: ')
print '\n=============================================================================='
try:
    print ext_euclid(int(number1), int(number2))
except ValueError:
    print 'One of your inputs is not integer.'
    print 'Please give integer input(s).'
print '=============================================================================='
