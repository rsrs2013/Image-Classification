class featureExtraction:

    def __init__(self,dataType):
        self.dataType = dataType

    def extractFeatures(self,data,type):
        if type == 1:
            return self.extractBasicFeatures(data)
        elif type == 2:
            return self.extractEdgeFeatures(data)


    def extractBasicFeatures(self,data):
        pixels = data.getPixels()
        feature = [item for sublist in pixels for item in sublist]
        return feature

    def extractEdgeFeatures(self,data):
        pixels = data.getPixels()
        feature = [item for sublist in pixels for item in sublist]
        feature = [ x if x != 1 else 0 for x in feature ]
        return feature
