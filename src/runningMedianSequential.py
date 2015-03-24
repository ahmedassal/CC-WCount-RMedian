import runningMedianCalculator
from runningMedianCalculator import MedianCalculator

__author__ = 'Ahmed Assal'

from scaled import dataLoaderV2, schedulerV2, schedulerV3, dataLoaderV3
from combiners import SimpleCombiner, MediansCombiner
from writers import medWriter

import time


inputPath = "../wc_input/"
outputPath = "../wc_output/"
src_path = "../src/"
write_in_html =False
textPool = []
results=[]

def runningMedianManager():
    start = time.clock()
    files = dataLoaderV3(inputPath, textPool)
    #print(files)
    results = [MedianCalculator(x, textPool[x]) for x in range(len(textPool))]

    finalResults = MediansCombiner(results)
    # print(finalResults)
    medWriter(outputPath, finalResults, write_in_html= write_in_html, partial=False)
    end =  time.clock()
    print("(Manager)Time elapsed: ", (end-start) , "Using Multiprocessing, Generated ", len(finalResults), " medians from ", len(results), " files")



runningMedianManager()






