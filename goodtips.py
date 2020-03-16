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
#the bestter way
message  = 'Update available' if atest_python > my_python else 'Up ot date'
print('Update check %s' % message)

#Tip9: sequence comparison
