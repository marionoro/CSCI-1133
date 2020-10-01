def wordlist(prose):
    mylist = []
    newprose = prose.lower()
    while len(newprose)>0:
        if newprose[0] not in [' ', ',', '.', ';']:
            word = ''
            i = 0
            while i<len(newprose) and newprose[i] not in [' ', ',', '.', ';']:
                word += newprose[i]
                i += 1
            if word not in mylist:
                mylist.append(word)
            newprose = newprose[i+1:]
        else:
            newprose=newprose[1:]
    return mylist
