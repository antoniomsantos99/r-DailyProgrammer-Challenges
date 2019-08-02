def disenvoweler(string):
    removal = ['a','e','i','o','u',' ','A','E','I','O','U']
    nstring =''
    vowels = ''
    for i in string:
        if i not in removal:
            nstring += i
        elif i != ' ':
            vowels += i
    print(nstring)
    print(vowels)

disenvoweler("All those who believe in psychokine sis raise my hand")