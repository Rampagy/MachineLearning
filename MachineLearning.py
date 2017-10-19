from PlantModel import PlantModelClass
import pylab
import numpy

def WeightedAverageFilter(newVal, oldVal):
    newValWeight = 1/8
    oldValWeight = 1 - newValWeight
    return newValWeight*newVal + oldValWeight*oldVal


# create plant model
Plant = PlantModelClass()

# init dictionary with -10's that is 81 long (-40 to 40)
Delays = range(-40, 41)
DelayScores = [-10.] * len(Delays)
DelayDict = dict(zip(Delays, DelayScores))

# create plot for graphing
pylab.ion()
pylab.xlim(-40, 40)
pylab.ylim(-20, 300)
pylab.title('Machine learning time delay over time')
pylab.ylabel('Filtered pressure rise, kPa')
pylab.xlabel('Time Delay, ms')
graph = pylab.plot(list(DelayDict.keys()), list(DelayDict.values()), 'b-o')[0]


# run through multiple iterations of the learning algorithm
NumberOfIterations = 500
for i in range(0, NumberOfIterations):

    # find smallest score in the dict and try it
    LowestScore = 9999999
    for DelayTime, NewScore in DelayDict.items():
        #print(str(DelayTime) + ' ' + str(NewScore) + ' ' + str(LowestScore))
        if NewScore < LowestScore:
            LowestScore = NewScore
            LowestScoreDelay = DelayTime

    #print('plant: ' + str(Plant.Update(LowestScoreDelay)))
    DelayDict[LowestScoreDelay] = WeightedAverageFilter(Plant.Update(LowestScoreDelay), DelayDict[LowestScoreDelay])
    #print(DelayDict[LowestScoreDelay])
    
    # update the plot
    graph.set_ydata(list(DelayDict.values()))
    pylab.draw()
    pylab.pause(0.00000000001)


    
