class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking = [big,medium,small]

    def addCar(self, carType: int) -> bool:
            if self.parking[carType-1]>0: # since carType is index + 1
                self.parking[carType-1] -=1
                return True
            return False