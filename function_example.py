# function = collection of code that perform a specific task
def sayhi():
    print('Hello User')


# this is how you call the function
sayhi()


# function with parameter
def sayhi_with_parameter(user_name, user_age):
    print('Hello ' + user_name + '(%s)' % user_age)


sayhi_with_parameter('Tom', 37)
sayhi_with_parameter(usre_name='Tom', user_age=37)  # this is called keyword argument


# function with parameter and return
def cube(num):
    return num * num * num


result = cube(4)
print(result)


# emoji converter
def emoji_converter(message):
    words = message.split("")
    emojis = {
        ":)": "😀",
        ":(": "☹️"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


input_text_message = input(">")
print(emoji_converter(input_text_message))
