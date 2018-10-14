def printPattern():
    quantity=int(raw_input("Enter quantity of repetitions\n"))
    for x in range(0,quantity):
        string=''
        for x in range(0,quantity):
            string+=str('*')
        print string


printPattern()
