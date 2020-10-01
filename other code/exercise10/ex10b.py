class Bug:
    def __init__(self, pos=0):
        self.position = pos
        self.direction = 1

    def move(self):
        if self.position != 0 or self.direction != -1:
            self.position += self.direction

    def turn(self):
        self.direction = - self.direction

    def display(self):
        for i in range(self.position):
            print (".", end = "")
        if self.direction == 1:
            print (">")
        else:
            print ("<")

def main():
    mybug = Bug(10)
    mybug.move()
    mybug.turn()
    for i in range(13):
        mybug.move()
        mybug.display()


if __name__ == "__main__":
    main()
