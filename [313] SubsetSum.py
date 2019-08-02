def subSetSum(list):
    sum = 0

    for i in list:
        sum += i
        if (-i) in list:
            return True
    if sum == 0:
        return True
    return False

print(subSetSum([x for x in range(1,10000)]))