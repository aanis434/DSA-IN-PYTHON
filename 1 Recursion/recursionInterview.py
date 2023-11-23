#   Created by Elshad Karimov on 4/01/20.
#   Copyright © 2020 AppMillers. All rights reserved.

import sys

sys.setrecursionlimit
sys.set_ne

# Question 1
# How to find the sum of digits of a positive integer number using recursion?
def sumofDigits(n):
    assert n>=0 and int(n) == n , 'The number has to be a postive integer only!'
    if n == 0:
        return 0
    else:
        return int(n%10) + sumofDigits(int(n/10))

print(sumofDigits(11111))


#Question 2
# How to calculate power of a number using recursion?
print(pow())
def power(base,exp):
    if exp == 0:
        return 1
    if(exp==1):
        return(base)
    if(exp!=1):
        return (base*power(base,exp-1))

print(power(4,2))

# Question 3 - How to find GCD ( Greatest Common Divisor) of two numbers using recursion?
'''
    ** GCD also knows as Greatest Common Denominator, Greatest Common Factor, Highest Common Factor.
    ** GCD is the largest postive integer that divides the numbers without a remainder.
    *** Euclidean algorithm is the another popular method to find GCD like gcd(48, 18)
    step 1: 48 / 18 = 2 reminder 12
    step 2: 18 / 12 = 1 reminder 6
    step 3: 12 / 6 = 2 reminder 0

    gcd (a, 0) = a
    gcd(a, b) = gcd (b, a % b)
'''

def gcd(a, b):
    assert int(a) == a and int(b) == b, 'The numbers must be integer only!'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(12,1.2))

# Question 4 - How to convert a number from Decimal to Binary using recursion?
'''
    ** f(13)
    ** step 1: Divided the number by 2
    ** step 2: Get the integer quotient for the next iteration
    ** step 3: Get the reminder for the binary digit
    ** step 4: Repeat the steps until the quotient is equal to 0
    13 to binary
    Division - Quotient - Reminder 
    13 / 2 - 6 - 1
    6 / 2 - 3 - 0
    3 / 2 - 1 - 1
    1 / 2 - 0 - 1
    from the last step the answer is 1101. 
    formula is: f(n) = n % 2 + 10 * f(n // 2)
'''
def decimalToBinary(n):
    if n == 0:
        return 0
    else:
        return n%2 + 10*decimalToBinary(int(n/2))


print(decimalToBinary(1))

