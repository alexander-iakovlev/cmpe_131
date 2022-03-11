def sort_list(myList):
    try:
        n = len(myList)
        i = 0
        while i < n:
            j = 0
            while j < n-i-1:
                if myList[j] > myList[j+1]:
                    temp = myList[j]
                    myList[j] = myList[j+1]
                    myList[j+1] = temp
                j += 1
            i += 1
    except TypeError:
        print("invalid list input")
    return myList
