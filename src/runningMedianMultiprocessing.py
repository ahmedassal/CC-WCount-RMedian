__author__ = 'Ahmed Assal'

################################################
# Calculating the running medians in parallel
# using Multiprocessing package
#
################################################

from scaledRunningMedian import mp_MedScheduler, mp_MedDataLoader
from combiners import MedCombiner
from writers import medWriter
import time

# paths to different parts of the project
workingPath = "../"  # ""
inputPath = workingPath + "wc_input/"
outputPath = workingPath + "wc_output/"
srcPath = workingPath + "src/"

# optional flag to right the results as HTML file instead of TXT file
writeInHTML =False

# buffer that is going to hold all the text from all the input text files
textPool = []

# intermediate results variable used to pass it between the different stages
intermediateResults=[]

def runningMedianManager():
    """
    parallel calculations pipeline for the running medians

    :rtype : null
    """

    # Start Profiling
    # basic profiling for the speed of the algorithm
    start = time.clock()

    # Data Loading Stage
    # loading the input text files into the buffer textPool organized as chunks,
    # one for every text file textPool.txtFile.Line
    files = mp_MedDataLoader(inputPath, textPool)

    # Data Processing Stage - calculating the running medians in parallel
    # iterating through the different text data for every input file while calculating the running median
    # for every chunk separately and the collecting the intermediate results inside a list of lists
    # [[List 1 for Input Text File 1], [List 2 for Input Text File 2], ....]
    intermediateResults = mp_MedScheduler(textPool)

    # Results Consolidation Stage
    # combining the lists, i.e. the intermediate results of the previous stage into one master list
    # the final result - a list of all running medians for all input text files
    finalResults = MedCombiner(intermediateResults)

    # Results Reporting Stage
    # writing the final results to a text or html file depending on the flag writeInHTML
    medWriter(outputPath, finalResults, "mp_", write_in_html= writeInHTML)

    end =  time.clock()
    print("(Manager)Time elapsed: ", (end-start) , ". Using Multiprocessing, generated ", len(finalResults), " medians from ", len(results), " files")


# invoking the parallel calculations for the running median
runningMedianManager()







