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
class Distribution(object):
    
    def __init__(self,dist_names_list = []):
        self.dist_names = ['alpha',
'anglit',
'arcsine',
'argus',
'beta',
'betaprime',
'bradford',
'burr',
'burr12',
'cauchy',
'chi',
'chi2',
'cosine',
'crystalball',
'dgamma',
'dweibull',
'erlang',
'expon',
'exponnorm',
'exponweib',
'exponpow',
'f',
'fatiguelife',
'fisk',
'foldcauchy',
'foldnorm',
'frechet_r',
'frechet_l',
'genlogistic',
'gennorm',
'genpareto',
'genexpon',
'genextreme',
'gausshyper',
'gamma',
'gengamma',
'genhalflogistic',
'gilbrat',
'gompertz',
'gumbel_r',
'gumbel_l',
'halfcauchy',
'halflogistic',
'halfnorm',
'halfgennorm',
'hypsecant',
'invgamma',
'invgauss',
'invweibull',
'johnsonsb',
'johnsonsu',
'kappa4',
'kappa3',
'ksone',
'kstwobign',
'laplace',
'levy',
'levy_l',
'logistic',
'loggamma',
'loglaplace',
'lognorm',
'lomax',
'maxwell',
'mielke',
'moyal',
'nakagami',
'ncx2',
'ncf',
'nct',
'norm',
'norminvgauss',
'pareto',
'pearson3',
'powerlaw',
'powerlognorm',
'powernorm',
'rdist',
'reciprocal',
'rayleigh',
'rice',
'recipinvgauss',
'semicircular',
'skewnorm',
't',
'trapz',
'triang',
'truncexpon',
'truncnorm',
'tukeylambda',
'uniform',
'vonmises',
'vonmises_line',
'wald',
'weibull_min',
'weibull_max',
'wrapcauchy']
        self.dist_results = []
        self.params = {}
        
        self.DistributionName = ""
        self.PValue = 0
        self.Param = None
        
        self.isFitted = False
        
        
    def Fit(self, y):
        self.dist_results = []
        self.params = {}
        for dist_name in self.dist_names:
            dist = getattr(scipy.stats, dist_name)
            print dist_name
            param = dist.fit(y)
            
            self.params[dist_name] = param
            #Applying the Kolmogorov-Smirnov test
            D, p = scipy.stats.kstest(y, dist_name, args=param);
            self.dist_results.append((dist_name,p))

        #select the best fitted distribution
        sel_dist,p = (max(self.dist_results,key=lambda item:item[1]))
        #store the name of the best fit and its p value
        self.DistributionName = sel_dist
        self.PValue = p
        
        self.isFitted = True
        for l in self.dist_results:
            print l
        return self.DistributionName,self.PValue
    
    def Random(self, n = 1):
        if self.isFitted:
            dist_name = self.DistributionName
            param = self.params[dist_name]
            #initiate the scipy distribution
            dist = getattr(scipy.stats, dist_name)
            return dist.rvs(*param[:-2], loc=param[-2], scale=param[-1], size=n)
        else:
            raise ValueError('Must first run the Fit method.')
            
    def Plot(self,y):
        x = self.Random(n=len(y))
        plt.hist(x, alpha=0.5, label='Fitted', bins=50)
        plt.hist(y, alpha=0.5, label='Actual', bins=50)
        plt.legend(loc='upper right')
        plt.show()

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
    BytesRead = int(counter/8)
    cacheLine = int ( BytesRead/64 )
    ByteOffset = int ( BytesRead % 64 )
    BitOffset = (counter%8)
    faults = []
    for i in bitLocations[value]:
        faults.append((str(cacheLine), str(ByteOffset), str(BitOffset+i)))
    return faults        

def writeFaultLine( desc, fileName):
    FI_FILE= open(fileName, "w")
    for l in desc:
        FI_FILE.write('%s %s %s l1d\n' % l)
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
                if ( faults != 0): 
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
    numberBRAMS=int(sys.argv[1])
    sizeBRAM = int(sys.argv[2])
    pathToFaults= sys.argv[3]
    outDir = sys.argv[4]
    if not os.path.exists(outDir):
        os.makedirs(outDir)

    numberOfFaults,maxFaults = getNumFaults(numberBRAMS,sizeBRAM,pathToFaults,outDir)

    y = np.array(numberOfFaults["0.55V"])

    x = np.arange(len(y))

    dst = Distribution()
    ret = dst.Fit(y)
    print ret
    dst.Plot(y)

