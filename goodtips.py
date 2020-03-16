#Disclaimer: these  tips are from Sebastiaan Mathôt channel
#Tip1: we want a cities in the list and the index number
cities = ['Bangkok', 'Amsterdam','Seattle','New York']
# the bad way
i = o
for city in cities:
    print(i, city)
    i += 1

# the better way use enumerate()
for i, city in enumerate(cities):
    print(i,city)


#Tip2: want to printout through 2 list at the same time
x_list = [1,2,3]
y_list = [2,4,6]
# the bad way
for i in range(len(x_list)):
    x = x_list[i]
    y = y_list[1]
    print(x,y)

# the better way use Zip()
for x,y in zip(x_list,y_list):
    print(x,y)

#Tip3: we want to swap 2 values
x = 10
y = -10
print('before: x = %d, y = %d' %(x,y))
#the bad way
temp = y
y = x
x = temp
print('After: x = %d, y = %d' %(x,y))
# the better way Tuple unpacking
# we can also declare sth like this x,y = 10,-10
x, y = y, x
print('After: x = %d, y = %d' %(x,y))

#Tip4: Default Dictionary Value
ages = {
    'Mary'      : 31,
    'Jonathan'  : 28,
    'Dick'      : 51
}
#the bad way
if 'Dick' in ages:
    age = ages['Dick']
else:
    age = 'Na'
print('Dick is %s years old' %age)
#the better way use get()
age = ages.get('Dick','Na')
print('Dick is %s years old' %age)

#Tip5: for...else
needle = 'd'
haystack = ['a', 'b', 'c']

#the bad way
found = False
for letter in haystack:
    if needle == letter:
        print('Found!')
        found = True
        break
if not found:
    print('Not Found!')

#the better way for...else() to do something if the loop is finish
#and not yet to find it
for letter in haystack:
    if needle == letter:
        print('Found!')
        break
else
    print('Not Found!')

#Tip6: file reading
#the bad way
file_object = open('pimin-aint-easy.txt')
text = file_object.read()
for line in text.split('\n'):
    print(line)
file_object.close()
#the better way -> we dont need to read the entile file &
#we don't need split we just loop directly
file_object = open('pimin-aint-easy.txt')
for line in file_object:
    print(line)
file_object.close()

#the even better way use the context with "with statement"
#the line under "with" are execute within the context and file automatically close
with open('pimin-aint-easy.txt') as file_object
for line in file_object:
    print(line)

#Tip7: try...except statement
#the normal way
print('Converting!')
try:
    print(int('X'))
except:
    print('conversion failed!')
print('Done!')
#the noone knows way
print('Converting!')
try:
    print(int('X'))
except:
    print('conversion failed!')
else: #we can also use else after except
    print('conversion Successful!')
finally: #regardless it does work or not
    print('Done!')


#Tip8: inline if statement
latest_python = 3
my_python = 3
#the bad way
message = 'It's up to date'
for i in range (len(latest_python)):
    if latest_python[i] > my_python[i]:
        message = 'Update available'
        break
print('Update check %s' % message)
#the better way
message  = 'Update available' if atest_python > my_python else 'Up ot date'
print('Update check %s' % message)

#Tip9: sequence comparison
latest_python = (3,5,2)
my_python = (3,5,2)
#the bad way
notification_message = 'Up to date'
for i in range(len(latest_python)):
    if latest_python[i] > my_python[i]:
        notification_message = 'Update available'
        break

#the better way
for latest_subversion, my_subversion in zip(latest_python,my_python):
    if latest_subversion > my_subversion:
        notification_message = 'Update available'
        break
    else
    notification_message = 'Up to Update'
print('Update check: %s' % notification_message)

#the best way use inline if...else, it also works with list
#but it doesnot work with the lists dont have the same length
notification_message = 'Update available' if latest_python > my_python else 'Up to date '
print('Update check: %s' %notification_message)

#Tip10: extended unpacking
cities_list = ['groningen','Marseille', 'Buenos Aires', 'Mumbai']
#the bad way -> assume a four list element
smallest, _, _, largest = cities_list
print('smallest: %s' % smallest)
print('largest: %s' % largest)
#a better way
smallest = cities_list[0]
largest = cities_list[-1]
print('smallest: %s' % smallest)
print('largest: %s' % largest)
# the best way -> use extended unpacked
smallest, *rest, largest = cities_list
print('smallest: %s' % smallest)
print('largest: %s' % largest)

#tip11: collection ordered Dictionary

cities = ['groningen','marseille', 'buenos aires', 'mumbai']
populations = [197823, 852516, 2890151, 12442373]
#the bad way
#we wanna capitalized the cities name
d = {}
for city, population in zip(cities, populations):
    d[string.capwords(city)] = population
print(d)
#the better way use dictionary comprehension
#but somehow does not preserve the order
d = {string.capwords(city): population for city, population in zip(cities,populations)}
print(d)
#we gonna order it
d = collection.OrderdDict()
for city, population in zip(cities,populations):
    d[string.capwords(city)] = population


#tip12: default dictionary
#we wanna handle when something is not in the dict yet

buttterfly_observation = {
    'Brown clipper'     : 2,
    'Common Mormon'     : 11,
    'Gailant Atlas Moth': 1,
    'Blue Peacock'      : 3
}
#the bad way
if 'Palmfly' in buttterfly_observation:
    palmfly_observation = buttterfly_observation['Palmfly']
else
    palmfly_observation = 0
print('Palmfly obervation: %d' %palmfly_observation)
#the better way use lamda (lambda is the way to create function inline of code)
# lambda : 0 is equvalent to def dummy(): return 0
d = collection.defaultdict(lambda : 0)
d.update(buttterfly_observation)
palmfly_observation = d['Palmfly']
print('Palmfly obervation: %d' %palmfly_observation)

#tip13
#using the same buttterfly_observation
butterfly_counter = collection.Counter(buttterfly_observation) #we gotta import collections
palmfly_observation = butterfly_counter['Palmfly'] #obviously it will return 0
print('Palmfly obervation: %d' %palmfly_observation)
