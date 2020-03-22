is_male = True
is_tall = True

if is_male or is_tall:
    print("you're a tall man")
elif is_male or not (is_tall):
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