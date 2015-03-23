

__author__ = 'Ahmed Assal'

from scaled import dataLoaderV2, schedulerV2, schedulerV3, dataLoaderV3
from combiners import SimpleCombiner
from writers import Writer

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
    results = schedulerV3(textPool)
    end =  time.clock()
    print("(Manager)Time elapsed: ", (end-start) , "Using Multiprocessing, Generated ", len(results), " medians from ", len(results), " files")
    # print(results)
    # finalResults = SimpleCombiner(results)
    # sortedByWord = sorted(finalResults, key=lambda k: k , reverse=False)
    # Writer(outputPath, sortedByWord, finalResults, write_in_html= write_in_html, partial=False)
    # print("Generated "+ str(len(finalResults)) + " tokens from " + str(len(results)) + " files")


runningMedianManager()







