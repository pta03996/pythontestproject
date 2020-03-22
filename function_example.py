# function = collection of code that perform a specific task
def sayhi():
    print('Hello User')


# this is how you call the function
sayhi()


# function with parameter
def sayhi_with_parameter(user_name, user_age):
    print('Hello ' + user_name + '(%s)' % user_age)


sayhi_with_parameter('Tom', 37)


# function with parameter and return
def cube(num):
    return num * num * num


result = cube(4)
print(result)
