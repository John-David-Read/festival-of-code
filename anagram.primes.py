from math import sqrt
import random

def is_prime(n):
    """
    Basic prime testing program.
    """
    if n<2:
        return False
    i=2
    while i<= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

alphabet = "abcdefghijklmnopqrstuvwxyz"

letter_id = {}
n=2
while alphabet != "":
    if is_prime(n):
        letter_id[alphabet[0]] = n
        alphabet = alphabet[1:]
    n += 1

def get_word_id(word):
    """
    Turns each letter of a word into a prime using letter_id and returns their product.
    """
    product = 1
    for letter in word:
        product = product * letter_id[letter]
    return product


def Target():
    with open("Resource/words-alpha.txt", "r") as file: 
        allText = file.read() 
        words = list(map(str, allText.split())) 
    target_word = random.choice(words)
    print(target_word,end = " [ ")
    return target_word

def Anagrams(target_word):
    word_file = open("Resource/words-alpha.txt", "r")
    target_word_id = get_word_id(target_word.lower())
    for word in word_file:
        word = word.rstrip('\r\n')
        word_id = get_word_id(word)
        if word_id == target_word_id:
            print(word,end = " ")
    print("]")
    return ()

for x in range (100):
    Anagrams(Target())
