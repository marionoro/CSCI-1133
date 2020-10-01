def letterFrequency(string):
    mydict = {}
    for x in string:
        if x not in mydict:
            mydict[x] = 1
        else:
            mydict[x] += 1
    return mydict

def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    mystring = input('Enter string: ')
    endstring = ''
    for x in mystring:
        if x != ' ':
            endstring += x.lower()
    dictionary = letterFrequency(endstring)
    for i in range(len(alphabet)):
        if alphabet[i] in dictionary:
            print(alphabet[i], dictionary[alphabet[i]])
    return

if __name__ == '__main__':
    main()
