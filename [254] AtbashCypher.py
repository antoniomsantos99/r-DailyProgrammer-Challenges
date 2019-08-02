import string

def Cypher(word):
    new = ""
    alphabet = list(string.ascii_lowercase)
    for i in word:
        if i == " ":
            new+=' '
        else:
            new += alphabet[len(alphabet)-1-alphabet.index(i)]


    print(new)

Cypher("gsrh rh zm vcznkov lu gsv zgyzhs xrksvi")