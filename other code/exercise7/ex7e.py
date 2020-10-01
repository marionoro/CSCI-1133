def int2str(n):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    if n // 10 == 0:
        return numbers[n]
    else:
        i = 1
        while n // (10**i) != 0:
            i += 1
        return numbers[n // (10**(i-1))] + int2str(n % (10**(i-1)))
