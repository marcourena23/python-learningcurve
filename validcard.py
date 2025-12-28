'''
Python credit card validator program

1. Remove any '-' or ' '
2. Add all digits in the odd places from right to left
3. Double every second digit from right to left.
(If result is a two-digit number,
add the two-digit number together to get a single digit.)
4. Sum the totals of steps 2 & 3
5. If sum is divisible by 10, the credit card # is valid

American Express 378282246310005
American Express 371449635398431
American Express Corporate 378734493671000
Australian Bankcard 5610591081018250
Diners Club 30569309025904
Diners Club 38520000023237
Discover 6011111111111117
Discover 6011000990139424
JCB 3530111333300000
JCB 3566002020360505
MasterCard 5555555555554444
MasterCard 5105105105105100
Visa 4111111111111111
Visa 4012888888881881
'''
import string
digits = string.digits
total_odd = 0
total_par = 0
#two_digits = 0
sum_two_digits = []
n = 0

def clean_credit_card_number(credit_card_number):
    for digit in credit_card_number:
        if digit not in digits:
            index = credit_card_number.index(digit)
            credit_card_number.pop(index)

def add_odd_numbers(credit_card_number):
    for digit in credit_card_number[::-1]:
        index = credit_card_number.index(digit)
        if index % 2 != 0:
            total_odd += credit_card_number.index(digit)

def add_par_number(credit_card_number):
    for digit in credit_card_number[::-1]:
        index = credit_card_number.index(digit)
        if index % 2 == 0:
            two_digits += credit_card_number.index(digit)
            if two_digits >= 10:
                sum_two_digits = two_digits
                n = sum_two_digits[0] + sum_two_digits[1]


def add_two_digits():
    for digit in credit_card_number[::-1]:
        pass

def sum_total():
    pass

def is_valid():
    pass

# main

# Get credit card number
credit_card_number = list(input("Enter your credit card number: "))

clean_credit_card_number(credit_card_number) # clean other innecesary characters

for digit in credit_card_number[::-1]:
        index = credit_card_number.index(digit)
        if index % 2 != 0:
            total_odd += credit_card_number.index(digit)
print(total_odd)


for digit in credit_card_number[::-1]:
        index = credit_card_number.index(digit)
        if index % 2 == 0:
            two_digits += credit_card_number.index(digit)
            if two_digits >= 10:
                sum_two_digits: int = two_digits
                n = sum_two_digits[0] + sum_two_digits[1]

print(n)