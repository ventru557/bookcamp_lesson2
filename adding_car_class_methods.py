"""Creating a Car class with methods and instances"""

# Define the Car class
class Car:
    """Creating a Car class with parameters and methods"""
    def __init__(self, make, model, body, engine, year, color):
        self.make = make
        self.model = model
        self.body = body
        self.engine = engine
        self.year = year
        self.color = color

    # Create a method to get the make of the car
    def get_make(self):
        """Returns the make of the car"""
        return self.make

    # Create a method to get the model of the car
    def get_model(self):
        """Returns the model of the car"""
        return self.model

    # Create a method to get the body of the car
    def get_body(self):
        """Returns the body of the car"""
        return self.body

    # Create a method to get the engine of the car
    def get_engine(self):
        """Returns the engine of the car"""
        return self.engine

    # Create a method to get the year of the car
    def get_year(self):
        """Returns the year of the car"""
        return self.year

    # Create a method to get the color of the car
    def get_color(self):
        """Returns the color of the car"""
        return self.color

    # Create three setter methods to change three parameters of the `Car` class.
    # YOUR SETTER METHODS GO HERE
    def set_year(self, new_year):
        """Get New Year of the Car"""
        self.year = new_year

    def set_color(self, new_color):
        """Get new Color of the car"""
        self.color = new_color

    def set_model(self, new_model):
        """Get new Car Model"""
        self.model = new_model

 

# Create an instance of the Car class
# Use the following default information or create your own default data.
car = Car("Subaru", "CrossTrek Limited", "SUV", "2.5L, 4 cylinder","2020", "Pearl Blue")

# Get the current information on the car.
print('Here are the details of the car.')
print(f"Make: {car.get_make()}")
print(f"Model: {car.get_model()}")
print(f"Body: {car.get_body()}")
print(f"Engine Type: {car.get_engine()}")
print(f"Year made: {car.get_year()}")
print(f"Color: {car.get_color()}")

# Prompt the user to change the three parameters for the car.
# Hint create new variables for each prompt.
new_year = int(input("Please enter the new year of the car:"))
new_color = input("Enter the new color of the car:")
new_model = input("Enter the new model of the car:")


# Pass the updated car information from the user to the setter method you created above.
car.set_color(new_color)
car.set_year(new_year)
car.set_model(new_model)

# Print the updated information of the car.
print('Here are the updated details of the car.')
print(f"Make: {car.get_make()}")
print(f"Model: {car.get_model()}")
print(f"Body: {car.get_body()}")
print(f"Engine Type: {car.get_engine()}")
print(f"Year made: {car.get_year()}")
print(f"Color: {car.get_color()}")
