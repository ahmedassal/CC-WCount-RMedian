from combiners import SimpleCombiner
from writers import Writer

__author__ = 'Ahmed Assal'

import sys, os, re, datetime
from scaled import dataLoaderV3
from tokenizers import TokenizerV3

# files = []
inputPath = "wc_input/"
outputPath = "wc_output/"
src_path = "src/"
write_in_html =False
textPool = []
results=[]

def wordCountManager():
    files = dataLoaderV3(inputPath, textPool)

    results = [TokenizerV3(x, files, inputPath) for x in range(len(textPool))]
    finalResults = SimpleCombiner(results)
    sortedByWord = sorted(finalResults, key=lambda k: k , reverse=False)
    Writer(outputPath, sortedByWord, finalResults, write_in_html= write_in_html, partial=False)
    print("Sequentially Generated "+ str(len(finalResults)) + " tokens from " + str(len(results)) + " files")


# wordCountManager()


