__author__ = 'Ahmed Assal'

from scaled import dataLoaderV2, schedulerV2
from combiners import SimpleCombiner
from writers import Writer


inputPath = "../wc_input/"
outputPath = "../wc_output/"
src_path = "../src/"
write_in_html =False
textPool = []
results=[]

def wordCountManager():
    files = dataLoaderV2(inputPath)
    # print(files)
    results = schedulerV2(inputPath, *files)
    # print(results)
    finalResults = SimpleCombiner(results)
    sortedByWord = sorted(finalResults, key=lambda k: k , reverse=False)
    Writer(outputPath, sortedByWord, finalResults, write_in_html= write_in_html, partial=False)
    print("Generated "+ str(len(finalResults)) + " tokens from " + str(len(results)) + " files")


wordCountManager()








