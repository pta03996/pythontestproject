is_male = True
is_tall = True

if is_male or is_tall:
    print("you're a tall man")
elif is_male or not is_tall:
    print("you're a short man")
else:
    print("You're either not male or tall")

# if statement comparison
def max_number(number1, number2, number3):
    if number1 >= number2 and number1 >= number3:
        return number1
    elif number2 >= number1 and number2 >= number3:
        return number2
    else:
        return number3

print(max_number(300,400,1))

# ''' exercise
# price of a house is $1 millions
# if buyer has a good credits,
# buyer need to put down only 10%
# otherwise
#  buyer need to put down 20%
# and print down the payment
# '''

price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2

print(f'Amount of down payment you have to pay: ${down_payment}')
