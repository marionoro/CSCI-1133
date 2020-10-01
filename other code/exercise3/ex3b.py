def perfect(n):
    a=1
    l = []
    while a < n:
        if n%a == 0:
            l.append(a)
        a += 1
    if n == sum(l):
        return("TRUE")
    else:
        return("FALSE")

def main():
    lower = int(input("Lower limit of your closed interval (must be positive integer): "))
    upper = int(input("Upper limit of your closed interval (must be positive integer): "))
    for i in range(lower, upper + 1):
        if perfect(i) == "TRUE":
            print(i)

if __name__ == '__main__':
    main()
