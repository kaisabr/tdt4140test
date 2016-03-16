# Skrevet av Magnus og Aashild

from siren import siren
from carInput import carInput

class distanceToCar():

    def __init__(self):
        self.car = carInput()

    # Beregner optimal distanse.
    def calculateOptimalDistance(self):
        speed = self.car.currentSpeed()
        return speed*3

    # Sirenen varsler dersom avstanden til bilen foran er for liten
    def calculateIfTooCloseToCar(self):
        distance = self.car.distanceToCar()
        carIsOn = self.car.carIsOn()
        while carIsOn:
            if self.calculateOptimalDistance() > distance:
                siren.triggeredByDistanceToCar()
            else:
                continue
