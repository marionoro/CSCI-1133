def firstvowelfinder(word):
    number = 0
    vowel = False
    while number < len(word) and vowel == False:
        if word[number] in ['A', 'E', 'I', 'O', 'U', 'a','e','i','o','u']:
            vowel = True
        else:
            number += 1
    if number == len(word):
        return 'No vowel found'
    return number

def wordtranslator(word):
    capitalized = False
    a = firstvowelfinder(word)
    if a == 'No vowel found':
        return
    if a == 0:
        newword = word + 'way'
        return newword
    if word[0] == word[0].upper():
        capitalized = True
    newword = word[a:] + word[:a] + 'ay'
    if capitalized:
        newword = newword[0].upper() + newword[1:].lower()
    return newword

def igpay(phrase):
        
