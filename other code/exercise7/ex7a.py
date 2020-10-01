def power(a,n):
    if n % 1 != 0 or n<0:
        return "n must be a non-negative integer"
    if n == 0:
        return 1
    else:
        return a * power(a, n-1)
