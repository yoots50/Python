class Calculator:
    def __init__(self, num):
        self.result = num
    def showMeTheResult(self):
        return self.result
    def plus(self, n):
        self.result += n 
        return self.result
class Car:

    def __init__(self, gas, engine, x, y, direction):
        self.fuel = gas
        self.speed = engine
        self.x = x
        self.y = y
        while not direction == "-x" or direction == "+x" or direction == "-y" or direction == "+y":
            direction = input(f"{direction}is wrong direction. Please enter the correct answer: ")
        else:
            self.direction = direction
        self.none = "none"

    def information(self):
        return f"Fuel is {self.fuel}, speed is {self.speed}, coordinate is ({self.x}, {self.y}), direction is {self.direction}."

    def goForward(self, meter):
        if meter/self.speed <= self.fuel:
            self.fuel -= meter / self.speed
            if self.direction == "-x":
                self.x -= meter
            elif self.direction == "+x":
                self.x += meter
            elif self.direction == "-y":
                self.y -= meter
            else:
                self.y += meter
        else:
            while meter/self.speed > self.fuel:
                meter = int(input(f"Your fuel is {self.fuel}. Please enter the right meter less than fuel. (Meter can't exceed {self.fuel * self.speed}): "))
            else:
                return self.goForward(meter)

    def changeDirection(self, direction):
        while not direction == "-x" or direction == "+x" or direction == "-y" or direction == "+y":
            direction = input(f"{direction}is wrong direction. Please enter the correct answer: ")
        else:
            self.direction = direction
            return f"Your direction is now {self.direction}"
                
