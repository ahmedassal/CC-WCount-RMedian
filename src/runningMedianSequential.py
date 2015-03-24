

__author__ = 'Ahmed Assal'


from scaledRunningMedian import dataLoaderV3
from runningMedianCalculator import MedianCalculator
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
    results = [MedianCalculator(x, textPool[x]) for x in range(len(textPool))]

    finalResults = MediansCombiner(results)
    # print(finalResults)
    medWriter(outputPath, finalResults, "seq_", write_in_html= write_in_html)
    end =  time.clock()
    print("(Manager)Time elapsed: "+ str((end-start)) + ". Sequentially generated " + str(len(finalResults)) + " medians from " + str(len(results)) + " files")



runningMedianManager() #("../wc_input/", "../wc_output/", "../src/", False)







