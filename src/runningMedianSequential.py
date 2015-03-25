__author__ = 'Ahmed Assal'

################################################
# Calculating the running medians sequentially
#
################################################

from scaledRunningMedian import seq_MedDataLoader
from runningMedianCalculator import MedianCalculator
from combiners import MedCombiner
from writers import medWriter
import time

# paths to different parts of the project
workingPathPrefix = "../"  # ""
inputPath = workingPathPrefix + "wc_input/"
outputPath = workingPathPrefix + "wc_output/"
srcPath = workingPathPrefix + "src/"

# optional flag to right the results as HTML file instead of TXT file
writeInHTML =False

# buffer that is going to hold all the text from all the input text files
textPool = []

# intermediate results variable used to pass it between the different stages
intermediateResults=[]

def runningMedianManager():
    """
    sequential calculations pipeline for the running median

    :rtype : null
    """
    # Start Profiling
    # basic profiling for the speed of the algorithm
    start = time.clock()

    # Data Loading Stage
    # loading the input text files, ordered alphabetically, into the buffer textPool organized as chunks,
    # one for every text file textPool.txtFile.Line
    files = seq_MedDataLoader(inputPath, textPool)

    # Data Processing Stage - calculating the running medians
    # iterating through the different text data for every input file while calculating the running median
    # for every chunk separately and the collecting the intermediate results inside a list of lists
    # [[List 1 for Input Text File 1], [List 2 for Input Text File 2], ....]
    intermediateResults = [MedianCalculator(x, textPool[x]) for x in range(len(textPool))]

    # Results Consolidation Stage
    # combining the sub lists, i.e. the intermediate results of the previous stage into one master list
    # the final result - a list of all running medians for all input text files
    finalResults = MedCombiner(intermediateResults)

    # Results Reporting Stage
    # writing the final results to a text or html file depending on the flag writeInHTML
    medWriter(outputPath, finalResults, "seq_", write_in_html= writeInHTML)

    end =  time.clock()
    print("(Manager)Time elapsed: "+ str((end-start)) + ". Sequentially generated " + str(len(finalResults)) +
          " medians from " + str(len(intermediateResults)) + " files")






# invoking the sequential calculations for the running medians
runningMedianManager()







