from random import randrange

class PlantModelClass():
    PlantModelCount = 0
    SwitchAlgorithmThreshold = 250;
    
    def Update(self, x):
        self.PlantModelCount+=1

        if self.PlantModelCount < self.SwitchAlgorithmThreshold:
            return x**2 + randrange(-15, 15)
        else:
            if self.PlantModelCount == self.SwitchAlgorithmThreshold+1:
                print('CHANGED!')
            return 0.0001 * x**4 - x**2 + 250 + randrange(-15, 15)
