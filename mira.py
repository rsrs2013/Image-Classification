import numpy as np
class mira:

    def __init__(self,dataType,trainingData,trainingLabels):
        self.dataType = dataType
        self.trainingData = trainingData
        self.trainingLabels = trainingLabels
        self.sizeOfFeatureVector = len(trainingData[0])
        self.distinctLabels = list(set(trainingLabels))
        self.C = 0.1
        self.weights = {}

    def setWeights(self,sizeOfFeatureVector,distinctLabels,defaultWeight):
        for label in range(len(distinctLabels)):
          weightVector = [defaultWeight]*sizeOfFeatureVector
          self.weights[label] = weightVector

    def evaluateScore(self,featureVector,weightVector):
        score =0
        for i in range(0,self.sizeOfFeatureVector):
            score = score + featureVector[i]*weightVector[i]
        return score

    def updateWeightVectorForLabels(self,actualLabel,estimatedLabel,featureVector):
         weightVectorToBeIncreased = self.weights[actualLabel]
         weightVectorToBeDecreased = self.weights[estimatedLabel]
         T = [0]*self.sizeOfFeatureVector;
         for i in range(0,self.sizeOfFeatureVector):
             T[i] = weightVectorToBeDecreased[i] - weightVectorToBeIncreased[i]
         Norm = 0
         Multi = 0;
         for i in range(0,self.sizeOfFeatureVector):
             Multi = Multi + T[i]*featureVector[i]
             Norm = Norm + (featureVector[i]*featureVector[i])

         Factor = float(( Multi + 1 ) / ( 2 * Norm ))
         Factor = min(float(self.C),Factor)
         for i in range(0,self.sizeOfFeatureVector):
             weightVectorToBeIncreased[i] = weightVectorToBeIncreased[i] + Factor*featureVector[i]
             weightVectorToBeDecreased[i] = weightVectorToBeDecreased[i] - Factor*featureVector[i]


    def train(self,defaultWeight,maxIterations):
        self.setWeights(self.sizeOfFeatureVector,self.distinctLabels,1)
        for i in range(0,maxIterations):
              for j in range(0,len(self.trainingData)):
                 featureVector = self.trainingData[j]
                 actualLabel = self.trainingLabels[j]
                 estimatedLabel = 0
                 numberOfLabelsProcessed = 0
                 maxScore = 0
                 for label in self.distinctLabels:
                    numberOfLabelsProcessed+=1
                    weightVector = self.weights[label]
                    score = self.evaluateScore(featureVector,weightVector)
                    if numberOfLabelsProcessed == 1:
                       maxScore = score
                       estimatedLabel = label

                    if score > maxScore:
                       maxScore = score
                       estimatedLabel = label

                 if actualLabel != estimatedLabel:
                    self.updateWeightVectorForLabels(actualLabel,estimatedLabel,featureVector)

    def test(self, testingData):
      numberOfFeatures = len(testingData)
      listOfEstimatedLabels = []
      lengthOfTestingData = len(testingData)
      self.testingData = testingData
      for j in range(0,lengthOfTestingData):
          featureVector = self.testingData[j]
          maxScore = 0
          estimatedLabel = ''
          numberOfLabelsProcessed = 0

          #print self.distinctLabels
          for label in self.distinctLabels:
             weightVector = self.weights[label]
             score = self.evaluateScore(featureVector,weightVector)
                  #check for maximum score and corresponding label
             if numberOfLabelsProcessed == 1:
                     maxScore = score
                     estimatedLabel = label
             if score > maxScore:
                maxScore = score
                estimatedLabel = label
          listOfEstimatedLabels.append(estimatedLabel)
             #print "EstimatedLabel is: "
             #print estimatedLabel
      return listOfEstimatedLabels



    def checkAccuracy(self,testingLabels,estimatedLabels):
        print len(self.distinctLabels)
        confusionMatrix = np.zeros((len(self.distinctLabels),len(self.distinctLabels)))
        count =0
        totalCount = len(testingLabels)
        for i in range(0,totalCount):
            confusionMatrix[testingLabels[i]][estimatedLabels[i]] += 1
            if testingLabels[i] == estimatedLabels[i]:
               count = count+1

        print confusionMatrix
        print "The total labels are: " + str(totalCount)
        print "The total matching labels are:" + str(count)
        accuracy =  100*count/float(totalCount)
        print "The accuracy is : " + str(accuracy)
