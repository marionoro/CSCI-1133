class Vehicle:
    def __init__(self, name ='', cylindernum ='', owner = ''):
        self.name = name
        self.cylnum = cylindernum
        self.owner = owner
    def change_name(self, newname):
        self.name = newname
    def change_cylnum(self, newnum):
        self.cylnum = newnum
    def change_owner(self, newowner):
        self.owner = newowner

class Truck(Vehicle):
    def __init__(self, loadcap, towcap):
        super().__init__('Truck', 4)
        self.loadcap = loadcap
        self.towcap = towcap
    def change_loadcap(self, newcap):
        self.loadcap = newcap
    def change_towcap(self, newcap):
        self.towcap = newcap
