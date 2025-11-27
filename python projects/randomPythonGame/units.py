import pygame, sys, json, math, time, gui, assetParser as assets, timer

pygame.init()

with open("units.json", "r") as data:
    unitsData = json.load(data) 

class unitHandler():
    units = {
        'infantry': 0,
        'tank': 0,
        'artillery': 0,
        'aircraft': 0,
        'naval': 0,
    }
    
    def createUnit(self, unitType):
        self.units[unitType] += 1

    def creationUnit(self, unitType):
        if unitType in self.units and assets.manpower >= unitsData[unitType]['manpowerCost'] and assets.credits >= unitsData[unitType]['creditCost']:
            assets.manpower -= unitsData[unitType]['manpowerCost']
            assets.credits -= unitsData[unitType]['creditCost']
            
            self.createUnit(unitType)
            print(f"{unitType.capitalize()} created! Total {unitType.capitalize()}: {self.units[unitType]}")
        else:
            print(f"Not enough manpower or credits to create {unitType} or invalid unit type.")

    def getUnitCount(self, unitType):
        return self.units.get(unitType, 0)
    
    def unitContinuity(self):
        if unit in self.units >= 1:
            for unit in self.units:
                return True
        else:
            return False
            