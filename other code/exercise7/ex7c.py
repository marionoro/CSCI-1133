def numDigits(n):
    if n // 10 == 0:
        return 1
    else:
        return 1 + numDigits(n//10)
