def separate(phrase):
    output = phrase
    for i in range(1, len(output)):
        if output[i].upper() == output[i]:
            output = output[:i] + ' ' + output[i].lower() + output[i+1:]
    return output

def combine(phrase):
    output = phrase
    i = 0
    while i<len(output):
        if output[i] == ' ':
            output = output[:i] + output[i+1].upper() + output[i+2:]
        else:
            i += 1
    return output

def main():
    prose = input("Input your phrase: ")
    a = combine(prose)
    print (a)
    b = separate(a)
    return b

if __name__ == '__main__':
    main()
