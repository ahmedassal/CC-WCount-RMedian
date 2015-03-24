__author__ = 'Ahmed Assal'

################################################
# Calculating the wordcounts in parallel
#
################################################

from scaledWordcount import dataLoaderV2, schedulerV2
from combiners import WordcountsCombiner
from writers import wcWriter
import time

# paths to different parts of the project
workingPathPrefix = "../"  # ""
inputPath = workingPathPrefix + "wc_input/"
outputPath = workingPathPrefix + "wc_output/"
src_path = workingPathPrefix + "src/"

# optional flag to right the results as HTML file instead of TXT file
writeInHTML =False

# buffer that is going to hold all the text from all the input text files
textPool = []

# intermediate results variable used to pass it between the different stages
intermediateResults=[]

# parallel calculations pipeline for the wordcounts
def wordCountManager():
    # Start Profiling
    # basic profiling for the speed of the algorithm
    start= time.clock()

    # Data Loading Stage
    # reporting the paths of the different  input text files only. Actual loading is deferred to the next stage
    # the data is loading occurs in the tokenizers, which are invoked by the scheduler.
    files = dataLoaderV2(inputPath)


    # Data Processing Stage - calculating the wordcounts in parallel
    # the calculations are divided into jobs, each job involves a data loading stage from the assigned input file
    # while collecting the intermediate results inside a list of dictionaries
    # [{Dict 1 for Input Text File 1}, [{Dict 2 for Input Text File 2}, ....]
    results = schedulerV2(inputPath, *files)

    # Results Consolidation Stage
    # combining the dictionaries, i.e. the intermediate results of the past stage into one master dictionary
    # the final result - a dictionary of all wordcounts for all input text files
    finalResults = WordcountsCombiner(results)

    # Results Preparation Stage
    # sorting the word alphabetically in preparation for writing them to text or html file
    sortedByWord = sorted(finalResults, key=lambda k: k , reverse=False)

    # Results Reporting Stage
    # writing the final results to a text or html file depending on the flag writeInHTML
    wcWriter(outputPath, sortedByWord, finalResults, "mp_", write_in_html= writeInHTML)

    end =  time.clock()
    print("(Manager)Time elapsed: " + str(end-start) + ". Using Multiprocessing, generated "+
          str(len(finalResults)) + " tokens from " + str(len(results)) + " files")



# invoking the parallel calculations for the wordcounts
wordCountManager()








