import sys, json, math, time, gui, assetParser as assets
class unitHandler():

    #region Data
    with open("units.json", "r") as data:
        unitData = json.load(data)

    with open("user.json", "r") as user:
        userData = json.load(user)

    with open("game.json", "r") as game:
        gameData = json.load(game)
    #endregion

    #region helpers
    def createUnit(self, unitType):
        self.userData["units"][unitType] += 1 # adds the new unit to the current unit count
        print(self.userData["units"][unitType])
        # add the ability to save modified unit counts data to user.json

    def unitCapable(self, unitType):
        if unitType in self.userData["units"]: # checks if the player has access to the unit
            if assets.manpower >= self.unitData[unitType]['manpowerCost']: # checks if the player has enough manpower for the unit
                if assets.credits >= self.unitData[unitType]['creditCost']: # checks if the player has enough money to buy the unit
                    return True
        else: print(f"Not enough resources to create {unitType} or invalid unit type.") # gives an error in the console

    def getUnitCount(self, unitType): # gets the unit count for a specific unit type
        return self.userData["units"].get(unitType, 0)
    
    def unitContinuity(self):
        for unit in self.userData["units"]:
            if self.userData["units"].get(unit, 0) > 0: # checks for if a unit type has any units
                return True, self.getUnitCount(unit) # returns True and the number of units of said type
            else: return False
    #endregion
        
    #region Main
    def creationUnit(self, unitType):
        if not self.userData["unitCount"] >= self.gameData["maxUnitCount"]: # checks if it will exeed the unit cap
            if self.unitCapable(unitType) == True: # checks if the unit can be spawned
                assets.manpower -= self.unitData[unitType]['manpowerCost'] # Removes the amount of manpower needed to spawn the unit from the player
                assets.credits -= self.unitData[unitType]['creditCost'] # Removes the amount of money needed to spawn the unit from the player

                if self.unitData[unitType]['oil']: # checks if the unit requires oil
                    assets.oil -= self.unitData[unitType]['oil'] # removes the required oil amount from the player

                self.createUnit(unitType)
    #endregion