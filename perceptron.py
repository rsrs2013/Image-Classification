import numpy as np
class Perceptron:
  """
  Perceptron classifier.

  Note that the variable 'datum' in this code refers to a counter of features
  (not to a raw samples.Datum).
  """
  def __init__( self):
    self.type = "perceptron"
    self.weights = {}


  def setWeights(self,sizeOfFeatureVector,distinctLabels,defaultWeight):

    if len(distinctLabels) > 0:
       #fill the weights dictionary with its keys as labels and values as a weight vector.
       for label in range(len(distinctLabels)):
         weightVector = [defaultWeight]*sizeOfFeatureVector
         self.weights[label] = weightVector

  def evaluateScore(self,featureVector,weightVector):
         score =0
         for i in range(0,self.sizeOfFeatureVector):
             #print featureVector[i]
             #print weightVector[i]
             score = score + featureVector[i]*weightVector[i]
             #print "The score is:"+`score`
         return score

  def updateWeightVectorForLabels(self,actualLabel,estimatedLabel,featureVector):
       weightVectorToBeIncreased = self.weights[actualLabel]
       weightVectorToBeDecreased = self.weights[estimatedLabel]
       for i in range(0,self.sizeOfFeatureVector):
           weightVectorToBeIncreased[i] = weightVectorToBeIncreased[i]+featureVector[i]
           weightVectorToBeDecreased[i] = weightVectorToBeDecreased[i]-featureVector[i]
           #if weightVectorToBeDecreased[i] <0:
              #weightVectorToBeDecreased[i]=0

  def train( self, trainingData, trainingLabels, validationData, validationLabels,defaultWeight,maxIterations):
    """
    The training loop for the perceptron passes through the training data several
    times and updates the weight vector for each label based on classification errors.
    See the project description for details.

    Use the provided self.weights[label] data structure so that
    the classify method works correctly. Also, recall that a
    datum is a counter from features to values for those features
    (and thus represents a vector a values).
    """
    numberOfFeatures = len(trainingData)
    self.sizeOfFeatureVector = len(trainingData[0])
    lengthOfTrainingData = len(trainingData)
    self.trainingData = trainingData
    self.trainingLabels = trainingLabels
    self.distinctLabels = list(set(trainingLabels))
    self.setWeights(self.sizeOfFeatureVector,self.distinctLabels,1)
    for i in range(0,maxIterations):
          for j in range(0,lengthOfTrainingData):
             featureVector = self.trainingData[j]
             actualLabel = trainingLabels[j]
             estimatedLabel = ''
             numberOfLabelsProcessed = 0
             maxScore = 0
             for label in self.distinctLabels:
                numberOfLabelsProcessed+=1
                #print "Checking for label:"+`label`
                weightVector = self.weights[label]
                score = self.evaluateScore(featureVector,weightVector)
                if numberOfLabelsProcessed == 1:
                   maxScore = score
                   estimatedLabel = label
                #print "Score is:"+`score`
                #print "Max Score is:"+`maxScore`
                #check for maximum score and corresponding label
                if score > maxScore:
                   maxScore = score
                   estimatedLabel = label
             #print "EstimatedLabel is: "+`estimatedLabel`
             #print "ActualLabel is: "+`actualLabel`
             if actualLabel != estimatedLabel:
                #print "Update"
                self.updateWeightVectorForLabels(actualLabel,estimatedLabel,featureVector)

         # s = raw_input()

             #if j == 1:
                #break;
    #print "Weights are:"
    #print self.weights

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
