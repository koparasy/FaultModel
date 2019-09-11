#!/usr/bin/python3
import pandas as pd
import numpy as np
import scipy
from sklearn.preprocessing import StandardScaler
import scipy.stats
import matplotlib.pyplot as plt
from sklearn import datasets
import os
import glob
import sys
import seaborn as sns
import numpy as np
import pandas as pd
from scipy import stats

import warnings
warnings.filterwarnings("ignore")


import scipy
import scipy.stats

import matplotlib
import matplotlib.pyplot as plt

hashFaults={}
hashFaults["0"] = 4
hashFaults["1"] = 3 
hashFaults["2"] = 3
hashFaults["3"] = 2
hashFaults["4"] = 3
hashFaults["5"] = 2
hashFaults["6"] = 2
hashFaults["7"] = 1
hashFaults["8"] = 3
hashFaults["9"] = 2
hashFaults["A"] = 2
hashFaults["B"] = 1
hashFaults["C"] = 2
hashFaults["D"] = 1
hashFaults["E"] = 1
hashFaults["F"] = 0
hashFaults[" "] = 0
hashFaults[""] = 0

bitLocations={}
bitLocations["0"] = [0,1,2,3]
bitLocations["1"] = [0,1,2]
bitLocations["2"] = [0,1,3]
bitLocations["3"] = [0,1]
bitLocations["4"] = [0,2,3]
bitLocations["5"] = [0,2]
bitLocations["6"] = [0,3]
bitLocations["7"] = [0]
bitLocations["8"] = [1,2,3]
bitLocations["9"] = [1,2]
bitLocations["A"] = [1,3]
bitLocations["B"] = [1]
bitLocations["C"] = [2,3]
bitLocations["D"] = [2]
bitLocations["E"] = [3]
bitLocations["F"] = []
bitLocations[' '] = []
bitLocations[''] = []


def createFaults(counter, value):
    faultType = 0
    BytesRead = int(counter/8)
    cacheLine = int ( BytesRead/64 )
    ByteOffset = int ( BytesRead % 64 )
    BitOffset = (counter%8)
    faults = []
    for i in bitLocations[value]:
        faults.append((str(faultType), str(cacheLine), str(ByteOffset), str(BitOffset+i)))
    return faults        

def writeFaultLine( desc, fileName):
    FI_FILE= open(fileName, "w")
    for l in desc:
        FI_FILE.write('%s %s %s %s l1d\n' % l)
    FI_FILE.close()        
        

def getFaults(faultFile,nBRAMS, sBRAM,numFaults,outDir):
    with open(faultFile) as f:
        print (faultFile)
        for i in range(0,nBRAMS):
                counter = 0
                faults = 0
                faultDesc = []
                while counter < sBRAM:
                    c = f.read(1)
                    if c != '' and c != ' ':
                        faults += hashFaults[c]
                        counter += 4
                        if ( hashFaults[c] != 0 ):
                            faultDesc += createFaults(counter,c)
                
                if (faults != 0):
                    writeFaultLine(faultDesc,outDir + "/BRAM_"+str(i)+".txt") 
                    numFaults.append(np.float64(faults))                    

def getNumFaults(nBRAMS, sBRAM, pathToFiles,outDir):
    fileNames = glob.glob(pathToFiles + "*.bin")
    numFaults = {}
    maxFaults=0
    for name in fileNames:
        voltage = name.split("/")[-1].split("-")[1][:4] +"V"
        if not os.path.exists(outDir + voltage ):
            os.makedirs(outDir + voltage)

        numFaults[voltage] = []
        getFaults( name, nBRAMS, sBRAM, numFaults[voltage], outDir + voltage) 
        mFaults = max(numFaults[voltage])
        if mFaults > maxFaults:
            maxFaults = mFaults

    return numFaults,maxFaults


if __name__ == "__main__":
    if (len(sys.argv) != 5 ):
        print "Wrong Command :"
        print sys.argv[0], "'Number of BRAMs' 'Size OF BRAM' 'Path to fault MAPS' 'output directory'"
        sys.exit(-1)

    numberBRAMS=int(sys.argv[1])
    sizeBRAM = int(sys.argv[2])
    pathToFaults= sys.argv[3]
    outDir = sys.argv[4]
    if outDir[-1] != "/":
        outDir += "/"
    if not os.path.exists(outDir):
        os.makedirs(outDir)

    numberOfFaults,maxFaults = getNumFaults(numberBRAMS,sizeBRAM,pathToFaults,outDir)

    for l in sorted(numberOfFaults):
        print l, "AVG : ", np.average(numberOfFaults[l]), "STD : ", np.std(numberOfFaults[l]) , "MIN : " , np.min(numberOfFaults[l]), "MAX: " , np.max(numberOfFaults[l]), "Total :", np.sum(numberOfFaults[l])

