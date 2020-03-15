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

#Tip4: Dictionary
ages = {
    'Mary'      : 31,
    'Jonathan'  : 28
}
#the bad way
if 'Dick' in ages:
    age = ages['Dick']
else:
    age = 'Na'
print('Dick is %s years old' %age)
