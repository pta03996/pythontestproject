for anythingIwant in "Giraffe Academy":
    print(anythingIwant)

for index in range(3, 10):
    print(index)

summon = ["Wha", "Khamun", "Belladeon", "Fran"]

for index in range(len(summon)):
    print(summon[index])


def raise_to_number(base_number, power_number):
    result = 1
    for power in range(power_number):
        result = base_number * result
    return result


print(raise_to_number(16, 17))

# 2d-lists & nested loop

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[2][1])

for each_row in number_grid:
    print(each_row)

for row in number_grid:
    for col in row:
        print(col)


# basic word encryption

def word_encryption(phase):
    translation = ""
    for letter in phase:
        if letter in "aeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(word_encryption(input("Enter a phase: ")))
