class Tool():
    def __init__(self, strength, type):
        self.__strength = strength
        self.__type = type
    def setStrength(self, newstrength):
        self.__strength = newstrength
    def get_strength(self):
        return self.__strength
    def get_type(self):
        return self.__type

class Rock(Tool):
    def __init__(self, strength):
        super().__init__(strength, 'r')
    def fight(self, Tool):
        if Tool.__type == 's':
            if 2 * self.__strength > Tool.__strength:
                return
        if Tool.__type == 'p':
            if 0.5 * self.__strength > Tool.__strength:
                return
        else:
            if self.__strength > Tool.__strength:
                return

class Paper(Tool):
    def __init__(self, strength):
        super().__init__(strength, 'p')
    def fight(self, Tool):
        if Tool.__type == 'r':
            if 2 * self.__strength > Tool.__strength:
                return
        if Tool.__type == 's':
            if 0.5 * self.__strength > Tool.__strength:
                return
        else:
            if self.__strength > Tool.__strength:
                return

class Scissors(Tool):
    def __init__(self, strength):
        super().__init__(strength, 's')
    def fight(self, Tool):
        if Tool.__type == 'p':
            if 2 * self.__strength > Tool.__strength:
                return
        if Tool.__type == 'r':
            if 0.5 * self.__strength > Tool.__strength:
                return
        else:
            if self.__strength > Tool.__strength:
                return

def main():
    myrock = Rock(10)
    mysci = Scissors(12)
    mypaper = Paper(4)

