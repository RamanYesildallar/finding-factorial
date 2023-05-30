def factorial():
    fact=1
    num=int(input("number:"))
    if num==0:
        print(fact)
    elif num==1:
        print(fact)

    else:
        myList = list(range(1, num + 1))
        for element in myList:
            fact *= element
        print(fact)



factorial()