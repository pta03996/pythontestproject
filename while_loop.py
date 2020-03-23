i = 1
while i <= 10:
    print(i)
    i += 1

print("We are done with loop")

# while loop game => guess the movie name

secret_word = "parasite"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input('Enter guess word: ')
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guess, you lose")
else:
    print("You win!")


# car example 3 command and help other than that it won't do anything
command = ""
started = False
while True:    # meaning if the block of code is executed, run until break
    command = input('> ').lower()
    if command == 'start':
        if started:
            print("Car is already started")
        else:
            started = True
            print('Car started...')
    elif command == 'stop':
        if not started:
            print('Car is already stopped')
        else:
            started = False
            print('Car stopped...')
    elif command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to quit
        ''')
    elif command == 'quit':
        break
    else:
        print("Sorry, I don't unerstand")
