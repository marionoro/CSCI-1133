def spreadsheet():
    filename = input("What is your file name: ")
    csvfile = open(filename, 'r')
    document = csvfile.read()
    spreadsheet = ''
    for x in document:
        if x == ',':
            spreadsheet += '    '
        else:
            spreadsheet += x
    return spreadsheet
