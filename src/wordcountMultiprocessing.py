__author__ = 'Ahmed Assal'

################################################
# Calculating the wordcounts in parallel using
# Multiprocessing package
#
################################################

from scaledWordcount import mp_WcDataLoader, mp_WcScheduler
from combiners import WcCombiner
from writers import wcWriter
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

def wordCountManager():
    """
    parallel calculations pipeline for the wordcounts

    :rtype : null
    """

    # Start Profiling
    # basic profiling for the speed of the algorithm
    start= time.clock()

    # Data Loading Stage
    # reporting the paths of the different input text files only. Actual loading is deferred to the next stage
    # the data is loading occurs in the tokenizers, which are invoked by the scheduler.
    files = mp_WcDataLoader(inputPath)


    # Data Processing Stage - calculating the wordcounts in parallel
    # the calculations are divided into jobs, each job involves a data loading stage from the assigned input file
    # while collecting the intermediate results inside a master list of tuples lists
    # [[(word, 1), (word, 1), ....for Input Text File 1], [(word, 1), (word, 1), ....for Input Text File 1], ....]
    intermediateResults = mp_WcScheduler(inputPath, *files)

    # Results Consolidation Stage
    # combining the tuples lists, i.e. the intermediate results of the previous stage into one master dictionary
    # the final result - a dictionary of all wordcounts for all input text files
    finalResults = WcCombiner(intermediateResults)

    # Results Preparation Stage
    # sorting the word alphabetically in preparation for writing them to text or html file
    sortedByWord = sorted(finalResults, key=lambda k: k , reverse=False)

    # Results Reporting Stage
    # writing the final results to a text or html file depending on the flag writeInHTML
    wcWriter(outputPath, sortedByWord, finalResults, "mp_", write_in_html= writeInHTML)

    end =  time.clock()
    print("(Manager)Time elapsed: " + str(end-start) + ". Using Multiprocessing, generated "+
          str(len(finalResults)) + " tokens from " + str(len(intermediateResults)) + " files")



# invoking the parallel calculations for the wordcounts
wordCountManager()








