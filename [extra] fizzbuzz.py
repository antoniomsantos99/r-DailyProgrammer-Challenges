def fizzbuzz():
    for i in [x for x in range(1,1000)*45]:
        string = ""
        if(i%3 ==0):
            string += "fizz"
        if(i%5 ==0):
            string += "buzz"
        if(len(string)==0):
            print(i)
        else:
            print(string)


fizzbuzz()