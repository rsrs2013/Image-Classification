class Datum:

    def __init__(self,data,dataType,height,width):
        self.dataType = dataType
        self.height = height
        self.width = width
        if data == None:
            data = [[' ' for i in range(height)] for j in range(width) ]
        self.pixels = self.convertToInteger(data)

    def convertToInteger(self,data):
        introws = []
        for row in data:
            introw = []
            for item in row:
                if item == '+':
                    introw.append(1)
                elif item == '#':
                    #if self.dataType == "digit":
                    introw.append(2)
                    #elif self.dataType == "face":
                    #    introw.append(1)
                else:
                    introw.append(0)
            introws.append(introw)
        return introws

    def __str__(self):
        rows = []
        for row in self.pixels:
            characters = map(self.integerMapping,row)
            rows.append("".join(characters))
        return "\n".join(rows)


    def integerMapping(self,pixel):
        if pixel == 0:
            return ' '
        elif pixel == 1:
            #if self.dataType == "digit":
            return '+'
            #elif self.dataType == "face":
            #    return '#'
        elif pixel == 2:
            return '#'
        else:
            return ' '

    def printData(self):
        for rows in self.pixels:
            print rows
        print self.__str__()

    def getPixels(self):
        return self.pixels
