import random


def check_letter(letter, twice_letter, word):
    j = 0
    if len(letter) != 1:
        print("You should input a single letter")
        j += 4
    elif letter.isupper() or not letter.isalpha():
        print("Please enter a lowercase English letter")
        j += 1
    elif letter in twice_letter:
        print("You've already guessed this letter")
        j += 3
    elif letter not in word:
        print("That letter doesn't appear in the word")
        j += 2
    return j


def init_list(word):
    l_word = list(word)
    for i in range(len(l_word)):
        l_word[i] = '-'
    return l_word


def list_in_word(l_word):
    word = ""

    for i in range(len(l_word)):
        word += l_word[i]
    return word


def add_letter(l_word, word, letter):
    for i in range(len(word)):
        if word[i] == letter:
            l_word[i] = letter


def play():
    twice_letter = ""
    words = ['python', 'java', 'kotlin', 'javascript']
    my_word = random.choice(words)
    list_word = init_list(my_word)
    user_input = input(f'''{list_in_word(list_word)}
    Input a letter: ''')
    i = 0
    ret = check_letter(user_input, twice_letter, my_word)
    if ret == 0:
        add_letter(list_word, my_word, user_input)
        twice_letter += user_input
    elif ret == 2:
        i += 1
        twice_letter += user_input
    elif ret == 3:
        twice_letter += user_input
    while i < 8 and '-' in list_word:
        print()
        user_input = input(f'''{list_in_word(list_word)}
Input a letter: ''')
        ret = check_letter(user_input, twice_letter, my_word)
        if ret == 0:
            add_letter(list_word, my_word, user_input)
            twice_letter += user_input
        elif ret == 2:
            i += 1
            twice_letter += user_input
        elif ret == 3:
            twice_letter += user_input

    if '-' in list_word:
        print("You lost!")
    else:
        print()
        print(my_word)
        print("You guessed the word!")
        print("You survived!")


if input(f'''H A N G M A N
Type "play" to play the game, "exit" to quit: ''') == "play":
    print()
    play()
    ret = input('Type "play" to play the game, "exit" to quit: ')
    while ret != "exit":
        if ret == "play":
            play()
        ret = input('Type "play" to play the game, "exit" to quit: ')