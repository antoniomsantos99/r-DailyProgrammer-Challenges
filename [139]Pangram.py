def Pangram(string):
    list = []
    for i in string:
        if i not in list and i != " ":
            list.append(i.lower())
    if len(list) == 26:
        return True
    return False

print(Pangram("abcdefghijklmnopqrstuvxyzw"))