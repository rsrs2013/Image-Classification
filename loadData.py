import os
from Datum import *

def loadDataFile(filename,dataType,width,height):
    fo = open(filename,"r")
    fin = fo.readlines()
    fin.reverse()
    items = []
    numimages = len(fin)/height
    for i in range(numimages):
        data = []
        for j in range(height):
            data.append(list(fin.pop()))
        items.append(Datum(data,dataType,height,width))
    return items

def loadLabelsFile(filename):
    fo = open(filename,"r")
    fin = fo.readlines()
    labels = []
    for line in fin:
        labels.append(int(line))
    return labels
