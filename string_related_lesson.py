name = input('Enter your name: ')
age = input('Enter your age: ')
print('Hello,' + name + ' ! you are ' + age)

#  basic calculator
num1 = input('Enter a number: ')
num2 = input('Enter another number: ')
result = int(num1) + int(num2)
#  result = float(num1) + float(num2) for the float number because int() canonly put zinteger
print(result)

#  madlip game + user put in your input

color = input('Enter your favorite color: ')
plural_noun = input('Enter a plural noun: ')
celebrity = input('Enter a celebrity: ')

print('Roses are ' + color)
print(plural_noun + ' are blues')
print('I love ' + celebrity)

# type of input // convert
birth_year = input('Birth Year: ')
print(type(birth_year))
age = 2020 - int(birth_year)
print(type(age) + " " + age)

# multiple string line

paragraph_context = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Phasellus orci urna, egestas id turpis ut, ultrices porta ipsum. 
Donec in semper urna, sed semper nisi.
'''

print(paragraph_context)
mock_sentense = 'Python is fun'
print(mock_sentense[3:])
print(mock_sentense[:5])
print(mock_sentense[:]) # will result like print(mock_sentense)

# full in the bracket example len()/upper()/lower()/title()/find()/replace()/'...' in ...
first_name = 'John'
last_name = 'Doe'
message = f' {first_name} {last_name} is a coder'
print(message + " and word count = " + len(message))
print('Capitalized: ' +message.upper())
print('Lower case: ' +message.lower())
print(message.find('h'))
print(message.replace('John Doe','Jane Doe'))
print('Python' in message) # check if some words are in the sentense
