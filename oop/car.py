class Car:
    # attributes- what an object has
    # methods = actions

    # constructor
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        # self - the method that is using that object
        print("This car is driving")
    def stop(self):
        print("This car is stoping")


