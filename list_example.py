friends = ['Kevin', 'Katarina', 'Kro', 'Belladeon']
print(friends)
print(friends[2])
print(friends[-1])
print(friends[0:2])

lucky_number = [23, 4, 8, 42, 15, 16, 23, 4]

friends.extend(lucky_number)  # add everything at the end of the first list
friends.append('Creed')  # add everything at the end of the first list
print(friends)

friends.insert(1, 'Kelly')
friends.remove('Kevin')
print(friends)

friends.pop()  # remove the last element in the list

# search an index from a friend name
print(friends.index('Oscar'))  # will show error
print(friends.count('Kro'))

lucky_number.sort()
print (lucky_number)

lucky_number.reverse()
print(lucky_number)

# remove a duplicate copy on the list
unique_number = []
for number in lucky_number:
    if number not in unique_number:
        unique_number.append(number)
