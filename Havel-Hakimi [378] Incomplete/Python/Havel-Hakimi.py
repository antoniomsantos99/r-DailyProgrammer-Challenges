def remove0(list):
    while 0 in list:
        list.remove(0)
    print(list)
    return list

def isEmpty(list):
    return (len(list) == 0)

def sortRev(list):
    list.sort(reverse=True)
    print(list)
    return list

def step(list):
    return(list[0]>len(list)-1)

def removefirst(list):
    return list[1::]

def declist(list):
    list[:] = [x - 1 for x in list]
    print(list)
    return list

def hh(list):
    remove0(list)
    if isEmpty(list):
        return True
    else:
        sortRev(list)
        if(step(list)):
            return False
        else:
            removefirst(list)
            declist(list)
            hh(list)


print(hh([5,3,0,2,6,2,0,7,2,5]))
