class Car():
    def __init__(self,
                 make: str = "Honda",
                 model: str = "Civic",
                 colour: str = "grey"):
        self.make = make
        self.model = model
        self.colour = colour
        self.position = 0

    def forward(self, distance):
        """Moves the car forward."""
        if distance > 0:
            self.position += distance
        return

    def backward(self, distance):
        if distance > 0:
            self.position -= distance


if __name__ == "__main__":
    my_car = Car(colour="silver")
    print(f"The car starts at {my_car.position}")
    print(f"It is a {my_car.colour} {my_car.make} {my_car.model}")
    print(f"Driving the car forward...")
    my_car.forward(10)
    print(f"The car is now at {my_car.position}")
    print(f"Moving back a bit...")
    my_car.backward(3)
    print(f"The car is now at {my_car.position}")