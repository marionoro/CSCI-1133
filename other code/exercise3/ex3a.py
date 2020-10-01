def compound_interest(initial, target, interest_rate):
    years = 0
    a = initial
    while a < target:
        a = a * (1 + interest_rate)
        years += 1
    return (years)

def main():
    initial = float(input("Starting amount of money (dollars.cents): "))
    target = float(input("Target amount of money (dollars.cents): "))
    interest_rate = float(input("Interest rate: "))
    print(compound_interest(initial, target, interest_rate), " years")

if __name__ == '__main__':
    main()
