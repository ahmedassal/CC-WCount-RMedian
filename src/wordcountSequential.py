__author__ = 'Ahmed Assal'

################################################
# Calculating the wordcounts sequentially
#
################################################

from scaledWordcount import seq_WcDataLoader
from combiners import WordcountsCombiner
from tokenizers import TokenizerV3
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

# sequential calculations pipeline for the wordcounts
def wordCountManager():
    # Start Profiling
    # basic profiling for the speed of the algorithm
    start = time.clock()

    # Data Loading Stage
    # loading the input text files into the buffer textPool organized as chunks,
    # one for every text file textPool.txtFile.Line
    files = seq_WcDataLoader(inputPath, textPool)

    # Data Processing Stage - calculating the wordcounts
    # iterating through the different text data for every input file while calculating the wordcounts
    # for every chunk separately and the collecting the intermediate results inside a list of dictionaries
    # [{Dict 1 for Input Text File 1}, [{Dict 2 for Input Text File 2}, ....]
    intermediateResults = [TokenizerV3(x, files, inputPath) for x in range(len(textPool))]

    # Results Consolidation Stage
    # combining the dictionaries, i.e. the intermediate results of the past stage into one master dictionary
    # the final result - a dictionary of all wordcounts for all input text files
    finalResults = WordcountsCombiner(intermediateResults)

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


