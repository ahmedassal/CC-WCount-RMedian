__author__ = 'Ahmed Assal'

from combiners import SimpleCombiner
from writers import wcWriter



from scaledWordcount import dataLoaderV3
from tokenizers import TokenizerV3
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
    start = time.clock()
    files = dataLoaderV3(inputPath, textPool)
    results = [TokenizerV3(x, files, inputPath) for x in range(len(textPool))]
    finalResults = SimpleCombiner(results)
    sortedByWord = sorted(finalResults, key=lambda k: k , reverse=False)
    wcWriter(outputPath, sortedByWord, finalResults, write_in_html= write_in_html, partial=False)
    end =  time.clock()
    print("(Manager)Time elapsed: " + str((end-start)) + ". Sequentially generated " + str(len(finalResults)) + " tokens from " + str(len(results)) + " files")


wordCountManager() #("../wc_input/", "../wc_output/", "../src/", False)


