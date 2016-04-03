import math
from loadData import *
from featureExtraction import *
from naiveBayes import *
from perceptron import *
from mira import *

# Its the percentage of the training data
k = 20
################################################################################
                # Digit Classification with features as pixel information #
################################################################################
digittrainingitems = loadDataFile("data/digitdata/trainingimages","digit",28,28)
digittraininglabels = loadLabelsFile("data/digitdata/traininglabels")
digitvalidationitems = loadDataFile("data/digitdata/validationimages","digit",28,28)
digitvalidationlabels = loadLabelsFile("data/digitdata/validationlabels")
digittestingitems = loadDataFile("data/digitdata/testimages","digit",28,28)
digittestinglabels = loadLabelsFile("data/digitdata/testlabels")

# Combining training and validation to form full training set
#digittrainingitems = digittrainingitems + (digitvalidationitems)
#digittraininglabels = digittraininglabels + (digitvalidationlabels)

f = featureExtraction("digit")
digittrainingfeatures = [];
for i in range(len(digittrainingitems) - (len(digittrainingfeatures)*(100-k)/100)):
    feature = f.extractFeatures(digittrainingitems[i],1)
    digittrainingfeatures.append(feature)

digittestingfeatures = [];
for i in range(len(digittestingitems)):
    feature = f.extractFeatures(digittestingitems[i],1)
    digittestingfeatures.append(feature)

n = naiveBayes("digit",digittrainingfeatures,digittraininglabels)
print n.getAccuracy(digittestingfeatures,digittestinglabels)

################################################################################
                # Face Classification with features as pixel information #
################################################################################

facetrainingitems = loadDataFile("data/facedata/facedatatrain","face",60,70)
facetraininglabels = loadLabelsFile("data/facedata/facedatatrainlabels")
facevalidationitems = loadDataFile("data/facedata/facedatavalidation","face",60,70)
facevalidationlabels = loadLabelsFile("data/facedata/facedatavalidationlabels")
facetestingitems = loadDataFile("data/facedata/facedatatest","face",60,70)
facetestinglabels = loadLabelsFile("data/facedata/facedatatestlabels")

#print facetrainingitems[0].printData()
#print facetraininglabels[0]

facetrainingitems = facetrainingitems + facevalidationitems
facetraininglabels = facetraininglabels + facevalidationlabels

f = featureExtraction("face")
facetrainingfeatures = []

for i in range(len(facetrainingitems)  - (len(facetrainingitems)*(100-k)/100)):
    feature = f.extractFeatures(facetrainingitems[i],1)
    facetrainingfeatures.append(feature)

facetestingfeatures = [];
for i in range(len(facetestingitems)):
    feature = f.extractFeatures(facetestingitems[i],1)
    facetestingfeatures.append(feature)

n = naiveBayes("face",facetrainingfeatures,facetraininglabels)
print n.getAccuracy(facetestingfeatures,facetestinglabels)


################################################################################
   # Digit Classification with features as pixel information using perceptron#
################################################################################
p = Perceptron()
p.train(digittrainingfeatures,digittraininglabels,digitvalidationitems,digitvalidationlabels,1,2)
listOfEstimatedLabels = p.test(digittestingfeatures)
p.checkAccuracy(digittestinglabels,listOfEstimatedLabels)

################################################################################
   # Face Classification with features as pixel information using perceptron#
################################################################################

p = Perceptron()
p.train(facetrainingfeatures,facetraininglabels,facevalidationitems,facevalidationlabels,1,2)
listOfEstimatedLabels = p.test(facetestingfeatures)
p.checkAccuracy(facetestinglabels,listOfEstimatedLabels)

################################################################################
   # Digit Classification with features as pixel information using MIRA Algorithm #
################################################################################

p = mira("digit",digittrainingfeatures,digittraininglabels)
p.train(1,2)
listOfEstimatedLabels = p.test(digittestingfeatures)
p.checkAccuracy(digittestinglabels,listOfEstimatedLabels)

################################################################################
   # Face Classification with features as pixel information using MIRA Algorithm #
################################################################################

p = mira("face",facetrainingfeatures,facetraininglabels)
p.train(1,2)
listOfEstimatedLabels = p.test(facetestingfeatures)
p.checkAccuracy(facetestinglabels,listOfEstimatedLabels)
