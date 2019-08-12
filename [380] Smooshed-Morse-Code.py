import string

def SMorseCode(input):
    alphabet = list(string.ascii_lowercase)
    malphabet = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
    result = ""
    for i in input.lower():
        if i != ' ':
            result += malphabet[alphabet.index(i)]
    print(result)

SMorseCode('aaAA')