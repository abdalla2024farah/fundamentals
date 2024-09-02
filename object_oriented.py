class Car:
    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")

def get_car_info():
    make = input("Enter the car make: ")
    model = input("Enter the car model: ")
    year = int(input("Enter the car year: "))
    return make, model, year

make, model, year = get_car_info()
my_car = Car(make, model, year)
my_car.display_info()
