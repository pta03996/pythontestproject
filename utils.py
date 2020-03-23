import random

feet_in_mile = 5280
meter_in_kilometer = 1000


def get_file_extension(filename):
    return filename[filename.inxex(".") + 1:]


def roll_dice(num):
    return random.randint(1, num)


def find_max_number(numbers):
    maximun = numbers[0]
    for number in numbers:
        if number > maximun:
            maximun = number
    return maximun
