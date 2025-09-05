class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        
    def info(self):
        infos = {"Brand": self.brand, "Year": self.year}
        return infos
    
    def start_engine(self):
        return "Engine Started"

class Car(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand, year)

    def start_engine(self):
        print("Car engine starts with a key!")
        return super().start_engine()

class Motorcycle(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand, year)

    def start_engine(self):
        print("Motorcycle engine starts with a button!")
        return super().start_engine()

class Truck(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand, year)

    def start_engine(self):
        print("Truck Engine starts with a button!")
        return super().start_engine()

class Garage(Vehicle):
    def __init__(self):
        self.vehicle_list = []
        
    def add_vehicle(self, Vehicle):
        self.vehicle_list.append(Vehicle)
        print("Vehicle Added")
        
    def all_info(self, brand, year):
        return super().info(self, brand, year)
    
def main():
    garage = Garage()
    garage_door = True
    
    def car_brand():
        car_brand = input("Input Vehicle Brand : ")
        while car_brand.isdigit == True:
            print("Invalid input")
            car_brand = input("Input Vehicle Brand : ")
        return car_brand
            
    def year_model():
        year_model = input("Input Year Model : ")
        while year_model.isdigit == False:
            print("Invalid input")
            year_model = input("Input Year Model : ")
        return year_model

    while garage_door:
        types = input("Vehicle Type (Truck, Motor, Car) : ")
        
        if types.lower() == 'truck':
            garage.add_vehicle(Truck(car_brand(), year_model()))
            garage_door = False
        elif types.lower() == 'motor':
            garage.add_vehicle(Motorcycle(car_brand(), year_model()))
            garage_door = False
        elif types.lower() == 'car':
            garage.add_vehicle(Car(car_brand(), year_model()))
        else:
            print("Invalid Input")        
    

if __name__ == '__main__':
    main()