__author__ = 'Ahmed Assal'

################################################
# Calculating the wordcounts sequentially
#
################################################

from scaledWordcount import seq_WcDataLoader
from combiners import WcCombiner
from tokenizers import WcTokenizer
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
    sequential calculations pipeline for the wordcounts

    :rtype : null
    """

    # Start Profiling
    # basic profiling for the speed of the algorithm
    start = time.clock()

    # Data Loading Stage
    # loading the input text files into the buffer textPool organized as chunks,
    # one for every text file textPool.txtFile.Line
    files = seq_WcDataLoader(inputPath, textPool)

    # Data Processing Stage - calculating the wordcounts sequentially
    # iterating through the different text data for every input file while calculating the wordcounts
    # for every chunk separately and then collecting the intermediate results inside a master list of tuples lists
    # [ [(word, 1), (word, 1), ....for Input Text File 1], [(word, 1), (word, 1), ....for Input Text File 1], ....]
    intermediateResults = [WcTokenizer(x, files, inputPath) for x in range(len(textPool))]

    # Results Consolidation Stage
    # combining the tuples list, i.e. the intermediate results of the previous stage into one master dictionary
    # the final result - a dictionary of all wordcounts for all input text files
    finalResults = WcCombiner(intermediateResults)

    # Results Preparation Stage
    # sorting the word alphabetically in preparation for writing them to text or html file
    sortedByWord = sorted(finalResults, key=lambda k: k , reverse=False)

    # Results Reporting Stage
    # writing the final results to a text or html file depending on the flag writeInHTML
    wcWriter(outputPath, sortedByWord, finalResults, "seq_", write_in_html= writeInHTML)

    end =  time.clock()
    print("(Manager)Time elapsed: " + str((end-start)) + ". Sequentially generated " + str(len(finalResults)) +
          " tokens from " + str(len(intermediateResults)) + " files")

# invoking the sequential calculations for the wordcounts
wordCountManager()


