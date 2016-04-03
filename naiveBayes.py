import math
import numpy as np
class naiveBayes:

    def __init__(self,dataType,trainingData,trainingLabels):
        self.dataType = dataType
        self.trainingData = trainingData
        self.trainingLabels = trainingLabels
        self.seperatedTrainingData = self.seperateTrainingDataByClass()

    def seperateTrainingDataByClass(self):
        seperatedTrainingData = {}
        for i in range(len(self.trainingData)):
            if self.trainingLabels[i] not in seperatedTrainingData:
                seperatedTrainingData[self.trainingLabels[i]] = []
            seperatedTrainingData[self.trainingLabels[i]].append(self.trainingData[i])
        return seperatedTrainingData

    def getClassMeanAndStd(self):
        meanAndStd = {}
        for label, data in self.seperatedTrainingData.items():
            meanAndStd[label] = self.calculateMeanAndStd(data)
        return meanAndStd

    def mean(self,attributes):
        return sum(attributes)/float(len(attributes))

    def stddev(self,attributes):
        avg = self.mean(attributes)
        variance = sum([pow(x - avg,2) for x in attributes])/float(len(attributes) - 1)
        return math.sqrt(variance)

    def calculateMeanAndStd(self,data):
        meanAndStd = [(self.mean(attribute), self.stddev(attribute)) for attribute in zip(*data) ]
        return meanAndStd

    def calculateGaussianProbability(self,attribute,avg,std):
        if std == 0:
            return 1
        else:
            exponent = math.exp(-(math.pow(attribute-avg,2)/(2*math.pow(std,2))))
        return (1 / (math.sqrt(2*math.pi) * std)) * exponent

    def calculateClassProbabilities(self,classMeanAndStd,inputTestVector):
        probabilities = {}
        for classLabel, classStdMean in classMeanAndStd.items():
            probabilities[classLabel] = 1
            for i in range(len(classStdMean)):
                avg,std = classStdMean[i]
                x = inputTestVector[i]
                probabilities[classLabel] *= self.calculateGaussianProbability(x,avg,std)
        return probabilities

    def predict(self,classMeanAndStd,inputTestVector):
        probabilities = self.calculateClassProbabilities(classMeanAndStd,inputTestVector)
        bestLabel, bestProb = None, -1
        for classLabel , probability in probabilities.items():
            if bestLabel is None or probability > bestProb:
                bestProb = probability
                bestLabel = classLabel
        return bestLabel

    def predictTestSet(self,classMeanAndStd,testSet):
        predictions = []
        for i in range(len(testSet)):
            result = self.predict(classMeanAndStd,testSet[i])
            predictions.append(result)
        return predictions

    def getAccuracy(self,testSet,testLabels):
        classMeanAndStd = self.getClassMeanAndStd()
        predictions = self.predictTestSet(classMeanAndStd,testSet)
        confusionMatrix = np.zeros((len(classMeanAndStd),len(classMeanAndStd)))
        truePositive =  0

        for i in range(len(testLabels)):
            confusionMatrix[testLabels[i]][predictions[i]] += 1
            if testLabels[i] == predictions[i]:
                truePositive += 1
        print confusionMatrix

        return (truePositive/float(len(testLabels)))*100
