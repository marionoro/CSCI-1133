def convertBase(n,base):
    numbers = '0123456789ABCDEFG'
    if n // 1 == n % base:
        return numbers[int(n)]
    elif n // base == 0:
        i = -1
        remainder = n % 1
        decimals = ''
        while remainder != 0:
            decimals += numbers[int(remainder // (base**i))]
            remainder = remainder % (base**i)
            i -= 1
        return convertBase(n // 1) + '.' + convertBase(decimals, base)
    else:
        return convertBase(n // base, base) + numbers[int(n) % base]
