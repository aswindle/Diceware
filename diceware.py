"""
Creates a Diceware password of user-defined length from a list of words
"""

import random

def get_num():
    retnum = ""
    for x in range(5):
        retnum += str(random.randint(1,6))
    return retnum

def get_word(words, num):
    return words[num]

def main():
    # parse word list into dictionary of num:word pairs
    # nums stored as strings
    f = open("wordlist.txt")
    lines = f.readlines()
    words = {}
    for line in lines:
        word_info = line.split()
        words[word_info[0]] = word_info[1]

    # ask for how many words to get
    num_words = int(input("Enter an integer number of words for the password:\n"))

    # get numbers and then words
    password = ""
    for i in range(num_words):
        num = get_num()
        word = get_word(words, num)
        password += word + " "
    password = password.strip(" ")
    print("Your {}-word password is:\n{}".format(num_words, password))

if __name__ == "__main__":
    main()
