def right_justify(str):
    while(len(str) < 70):
        str = ' ' + str
    print(str)
    print(len(str))


right_justify('test')