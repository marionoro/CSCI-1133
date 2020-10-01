def reverseTel(phonebook):
    mydict = {}
    for x in phonebook:
        a = phonebook[x]
        mydict[a] = x
    return mydict
