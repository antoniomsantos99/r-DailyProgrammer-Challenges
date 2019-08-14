import string
from collections import Counter

def SMorseCode(input):
    alphabet = list(string.ascii_lowercase)
    malphabet = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
    result = ""
    for i in input.lower():
        if i != ' ':
            result += malphabet[alphabet.index(i)]
    return result




def enable1L():
    file = open("enable1.txt", "r")
    return file
    #return


liste = enable1L().read().split()
wordm = map(SMorseCode,liste)
lista = zip(liste,wordm)

#BONUS 1
def bonus1():

    mf = most_frequent(wordm)
    print(mf)

    for word in liste:
        if SMorseCode(word) == mf:
            print(word)

def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]

#BONUS 2

#Podia fazer estilo C para ficar mais otimizado mas meh
def fifteendashes(morse):
    for i in morse:
       morsee = i[1].split('.')
       for p in morsee:
            if len(p) == 15:
                print(i)

def bonus2():
    fifteendashes(lista)

#BONUS 3
def bonus3():
    for i in lista:
        if i[1].count('.')  == i[1].count('-') and len(i[0]) == 21:
            print(i)

#BONUS 4
def palindrome(word):
    return (word == word[::-1])

def bonus4():
    for i in lista:
        if palindrome(i[1]) and len(i[0])==13:
            print(i)


def menu():
    choice = 'NULL'
    while choice == 'NULL':
        choice = input("Normal[0] or Bonus[1][2][3][4]? \n")
        if int(choice) == 0:
            text = input("Word? \n")
            print(SMorseCode(text))
        elif int(choice) == 1:
            bonus1()
        elif int(choice) == 2:
            bonus2()
        elif int(choice) == 3:
            bonus3()
        elif int(choice) == 4:
            bonus4()
        else:
            choice = 'NULL'

menu()