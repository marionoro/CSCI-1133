def spaceit(istr):
    if len(istr) == 1:
        return istr
    else:
        if istr[0] == istr[1]:
            return istr[0] + ' ' + spaceit(istr[1:])
        else:
            return istr[0] + spaceit(istr[1:])
