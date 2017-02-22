#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import csv
import numpy as np

#Task 1
def readCSV(pathToFile):
    array = []
    with open(pathToFile, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            array.append(row)    
    return array

def calculateCenter(train_in):
    center = []
    for i in range(len(train_in)):
        totaal = 0
        for j in range(len(train_in[0])):
            totaal = totaal + float(train_in[i][j])
        center.append(totaal/len(train_in[0]))
    return center

def calculateRadius(train_in, center): # euclidean
    radius = []
    for i in range(len(train_in)):
        maxRadius = 0
        for j in range(len(train_in[0])):
            if (maxRadius < np.linalg.norm(center[i] - float(train_in[i][j]))):
                maxRadius = float(train_in[i][j])  
            radius.append(maxRadius)
    return radius

def start():
    train_in = readCSV('data/train_in.csv')
    train_out = readCSV('data/train_out.csv')
    center = calculateCenter(train_in)
    radius = calculateRadius(train_in, center)
    
    