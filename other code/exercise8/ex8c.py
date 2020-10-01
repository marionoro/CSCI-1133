# this is not correct

def letterFrequency(string):
    mydict = {}
    for x in string:
        if x not in mydict:
            mydict[x] = 1
        else:
            mydict[x] += 1
    return mydict

def main():
    mystring = input('Enter string: ')
    endstring = ''
    for x in mystring:
        if x != ' ':
            endstring += x.lower()
    dictone = letterFrequency(endstring)
    dicttwo = {}
    for y in dictone:
        a = dictone[x]
        dicttwo[a] = x
    i = max(dicttwo)
    while i > 0:
        if i in dicttwo:
            print (dicttwo[i], i)
        i -= 1
    return

if __name__ == '__main__':
    main()
