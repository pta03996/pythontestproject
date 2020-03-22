import random

feet_in_mile = 5280
meter_in_kilometer = 1000


def get_file_extension(filename):
    return filename[filename.inxex(".") + 1:]


def roll_dice(num):
    return random.randint(1, num)
