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

# 1. Remove any '-' or ' '
def cleanCreditCardNumber(credit_card_number):
    cleanedCreditCard = [digit for digit in credit_card_number if digit in digits] # add only digits to new list
    return cleanedCreditCard

# 2. Sum all digits in the odd places from right to left
def sumOddPlaces(credit_card_number):
    total_odd = 0
    odd = [digit for digit in credit_card_number[::-2]]
    for num in odd:
        total_odd += int(num)
    return total_odd

# 3 Add all digits in the pair places from right to left (If result is a two-digit number, add the two-digit number together to get a single digit.)
def sumPairPlaces(credit_card_number):
    sum_two_digits = 0
    total_pair = 0
    pair = [int(digit) * 2 for digit in credit_card_number[-2::-2]]
    for number in pair:
        if number >= 10:
            sum_two_digits = (number // 10) + (number % 10) # // integer division
            total_pair += sum_two_digits
        else:
            total_pair += number
    return total_pair

# 4 Sum the totals of steps 2 & 3
def sum_total(total_odd, total_pair):
    return total_odd + total_pair

# 5 If sum is divisible by 10, the credit card # is valid
def is_valid(total):
    return total % 10 == 0

# Market: Main program
# Get credit card number
credit_card_number = list(input("Enter your credit card number: "))

cleanedCreditCard = cleanCreditCardNumber(credit_card_number) # clean other innecesary characters
total = sum_total(sumOddPlaces(cleanedCreditCard), sumPairPlaces(cleanedCreditCard))
if is_valid(total):
    print("The credit card number is valid.")
else:
    print("The credit card number is invalid.")