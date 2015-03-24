__author__ = 'Ahmed Assal'


from scaledWordcount import dataLoaderV2, schedulerV2
from combiners import SimpleCombiner
from writers import wcWriter
import time


workingPath = "../"  # ""
inputPath = workingPath + "wc_input/"
outputPath = workingPath + "wc_output/"
src_path = workingPath + "src/"
write_in_html =False
textPool = []
results=[]
msg =""

def wordCountManager(): #(inputPath, outputPath, src_path, write_in_html=False):
    start= time.clock()
    files = dataLoaderV2(inputPath)
    results = schedulerV2(inputPath, *files)
    finalResults = SimpleCombiner(results)
    sortedByWord = sorted(finalResults, key=lambda k: k , reverse=False)
    wcWriter(outputPath, sortedByWord, finalResults, "mp_", write_in_html= write_in_html)
    end =  time.clock()
    print("(Manager)Time elapsed: " + str(end-start) + ". Using Multiprocessing, generated "+ str(len(finalResults)) + " tokens from " + str(len(results)) + " files")



wordCountManager() #("../wc_input/", "../wc_output/", "../src/", False)








