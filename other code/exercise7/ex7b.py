def series(n):
    if n % 1 != 0:
        return "n must be an integer."
    elif n <= 1:
        return 0
    else:
        if n == 2:
            return 1 + 2
        else:
            return (n**(n-1))/(n-1) + series(n-1)
