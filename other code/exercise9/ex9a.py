def createdictionary():
    mydict = {}
    listofterms = ['False','class','finally','is','return','None','continue',
            'for','lambda','try','True','def','from','nonlocal','while','and','del','global', 'not', 'with', 'as','elif',
            'if','or','yield','assert','else','import','pass','break','except','in','raise']
    for x in listofterms:
        mydict[x] = 0
    return mydict

def main():
    mydict = createdictionary()
    filename = input("File name: ")
    myfile = open(filename, 'r')
    document = myfile.read()
    for x in document
    mylist = []
    for x in mydict:
        if mydict[x] > 0:
            mylist.append((x.lower(),mydict[x]))
    finallist = mylist.sort()
    return finallist

if __name__ == '__main__':
    main()
