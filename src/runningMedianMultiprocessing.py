

__author__ = 'Ahmed Assal'

from scaledRunningMedian import schedulerV3, dataLoaderV3
from combiners import MediansCombiner
from writers import medWriter
import time


workingPath = "../"  # ""
inputPath = workingPath + "wc_input/"
outputPath = workingPath + "wc_output/"
src_path = workingPath + "src/"
write_in_html =False
textPool = []
results=[]
msg =""

def runningMedianManager(): #(inputPath, outputPath, src_path, write_in_html=False):
    start = time.clock()
    files = dataLoaderV3(inputPath, textPool)
    #print(files)
    results = schedulerV3(textPool)

    finalResults = MediansCombiner(results)
    # print(finalResults)
    medWriter(outputPath, finalResults, "mp_", write_in_html= write_in_html)
    end =  time.clock()
    print("(Manager)Time elapsed: ", (end-start) , ". Using Multiprocessing, generated ", len(finalResults), " medians from ", len(results), " files")



runningMedianManager() #("../wc_input/", "../wc_output/", "../src/", False)







