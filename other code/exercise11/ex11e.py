class Vehicle:
    def __init__(self, make, model, year, mileage, price):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price
    def change_make(self, inputval):
        self.make = inputval
    def change_model(self, inputval):
        self.model = inputval
    def change_year(self, inputval):
        self.year = inputval
    def change_mileage(self, inputval):
        self.mileage = inputval
    def change_price(self, inputval):
        self.price = inputval
    def get_make(self):
        return self.make
    def get_model(self):
        return self.model
    def get_year(self):
        return self.year
    def get_mileage(self):
        return self.mileage
    def get_price(self):
        return self.price
    def Display(self):
        print('Make: ', self.make)
        print('Model: ', self.model)
        print('Year: ', self.year)
        print('Mileage: ', self.mileage)
        print('Price: ', self.price)

class Car(Vehicle):
    def __init__(self, make, model, year, mileage, price, numdoors):
        super().__init__(make, model, year, mileage, price)
        self.numdoors = numdoors
    def get_doors(self):
        return self.numdoors
    def change_doors(self, inputval):
        self.numdoors = inputval
    def Display(self):
        print('Inventory Unit: Car')
        super().Display()
        print('Number of Doors: ', self.numdoors)

class Truck(Vehicle):
    def __init__(self, make, model, year, mileage, price, wheeldrive):
        super().__init__(make, model, year, mileage, price)
        self.wheeldrive = wheeldrive
    def get_wheeldrive(self):
        return self.wheeldrive
    def change_wheeldrive(self, inputval):
        self.wheeldrive = inputval
    def Display(self):
        print('Inventory Unit: Truck')
        super().Display()
        print('Drive Type: ', self.wheeldrive)

class SUV(Vehicle):
    def __init__(self, make, model, year, mileage, price, capacity):
        super().__init__(make, model, year, mileage, price)
        self.capacity = capacity
    def get_capacity(self):
        return self.capacity
    def change_capacity(self, inputval):
        self.capacity = inputval
    def Display(self):
        print('Inventory Type: SUV')
        super().Display()
        print('Passenger Capacity: ', self.capacity)

class Inventory:
    def __init__(self, mylist = []):
        Inventory.list = mylist
    def addVehicle(self, vehicle):
        Inventory.list.append(vehicle)
    def Display():
        for i in range(len(Inventory.list)):
            Inventory.list[i].Display()
            print('')
            print('')

def main():
    inventory = Inventory()
    myinput = 'a'
    while myinput != '':
        myinput = input('Enter Vehicle Type (null string ends entry): ')
        if myinput == 'car' or myinput == 'Car' or myinput == 'CAR':
            make = input('Enter Make: ')
            model = input('Enter Model: ')
            year = input('Enter Year: ')
            mileage = input('Enter Mileage: ')
            price = input('Enter Price: ')
            numdoors = input('Enter Number of Doors: ')
            newcar = Car(make, model, year, mileage, price, numdoors)
            inventory.addVehicle(newcar)
        elif myinput == 'truck' or myinput == 'Truck' or myinput == 'TRUCK':
            make = input('Enter Make: ')
            model = input('Enter Model: ')
            year = input('Enter Year: ')
            mileage = input('Enter Mileage: ')
            price = input('Enter Price: ')
            drivetype = input('Enter Drive Type: ')
            newtruck = Truck(make, model, year, mileage, price, drivetype)
            inventory.addVehicle(newtruck)
        elif myinput == 'SUV' or myinput == 'suv' or myinput == 'Suv':
            make = input('Enter Make: ')
            model = input('Enter Model: ')
            year = input('Enter Year: ')
            mileage = input('Enter Mileage: ')
            price = input('Enter Price: ')
            capacity = input('Enter Passenger Capacity: ')
            newsuv = SUV(make, model, year, mileage, price, capacity)
            inventory.addVehicle(newsuv)
        elif myinput == '':
            pass
        else:
            print('INVALID INPUT')
    Inventory.Display()
