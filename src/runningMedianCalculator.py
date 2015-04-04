__author__ = 'Ahmed Assal'

################################################
# Counts the occurrences of words in a text file
# Extracts the tokens in a given text buffer.
# That is to say, it scan a buffer of a list of
# lines into for tokens/words. It then either
# count the occurrences of these words in the
# text or it just signals the repeated
# appearance of a token/word. Another module
# in the pipeline can later count the
# occurrences of these token/word.
#
################################################

import re, sys, string
sys.path.extend(['/home/administrator/PycharmProjects/CC-WCount-RMedian'])
import time

# sorted list data structure for the computation of the running median
from sortedcontainers.sortedlist import SortedList

# based on the assumptions, hyphens, underscores or apostrophes appear mid-word are not assumed to be word
# boundaries, i.e., they can be deleted safely and the token can be captured as if they were not present.
#
# Alternative 1
# a table for the translation of every line, it is a fast conversion of uppercase to
# lowercase and removal of the following `'-_
table = str.maketrans(string.ascii_uppercase ,string.ascii_lowercase , "`'-_")

# two other treatments of punctuation and digits
#
# Alternative 2
# delete digit and punctuation except `'-_ hyphens, underscores or apostrophes
# charsToDel = string.punctuation.translate(str.maketrans("", "", "`'-_"))+"0123456789"
# table = str.maketrans(string.ascii_uppercase,string.ascii_lowercase, charsToDel)

# Alternative 3
# delete all punctuation and digits
# table = str.maketrans(string.ascii_uppercase,string.ascii_lowercase, string.punctuation.join("0123456789"))


# the regular expression pattern used for matching a token/word
# word/token is any number of alphabetic symbols
tokenPattern = re.compile(r'([a-z]+)')

def MedCalculator(fileNum, text):
    """
    thread worker function
    Calculates the running median for the lines present in the text list supplied.
    Currently the sequential implementation is identical to the parallel implementation.

    :rtype :        null
    :param fileNum: an index pointing to the file to be processing in the input files
    :param text:    a text buffer to be loaded with the input text
    """

    # Start Profiling
    # basic profiling for the speed of the algorithm
    # start = time.clock()

    # the list that is going to hold the running medians
    medianNumbers= []

    # a sorted list to hold the word counts for input lines
    # the sorted list boosts performance substantially when computing the running median because this will not require
    # resorting the wordcount list every time we add an entry to it.
    linesWordCount = SortedList()
    lineNO = 0


    for line in text:

        # fast conversion of uppercase to lowercase and removal of the following `'-_
        cleaned_line = line.translate(table)

        # matching words/tokens
        words = re.findall(tokenPattern, cleaned_line)

        # counting wordcount of a line and adding it ot the respective list
        lineWordCount = len(words)
        linesWordCount.add(lineWordCount)

        # running median calculations
        # because I used a sorted list for the worcounts of lines, now it is straightforward to compute
        # the running median
        index = int(lineNO/2)
        if lineNO%2 == 0:
            medianNumbers.append(float(linesWordCount[index]))
        else:
            medianNumbers.append(float((linesWordCount[index] + linesWordCount[index+1])/2))
        lineNO += 1

        # optional profiling
        # print("Line NO: " + str(lineNO) + " wordcount: " + str(lineWordCount))
        # print("Size: " + str(len(linesWordCount)) + " linesWordCount elm: " + str(linesWordCount) )
        # print("Median NOs: " + str(medianNumbers))
        # end =  time.clock()

    # optional profiling
    # print("(Calculator)Time elapsed: ", (end-start), "Using Multiprocessing, Generated ", len(medianNumbers) , " medians from " , lineNO, " Lines")#, len(text) , " files")

    return medianNumbers

def mp_MedCalculator2(fileNum, text):
    """
    thread worker function
    Calculates the running median for the lines present in the text list supplied.
    Currently the sequential implementation is identical to the parallel implementation.

    :rtype :        null
    :param fileNum: an index pointing to the file to be processing in the input files
    :param text:    a text buffer to be loaded with the input text
    """

    # Start Profiling
    # basic profiling for the speed of the algorithm
    # start = time.clock()

    # the list that is going to hold the running medians
    medianNumbers= []

    # a sorted list to hold the word counts for input lines
    # the sorted list boosts performance substantially when computing the running median because this will not require
    # resorting the wordcount list every time we add an entry to it.
    linesWordCount = [] #SortedList()
    lineNO = 0


    for line in text:

        # fast conversion of uppercase to lowercase and removal of the following `'-_
        cleaned_line = line.translate(table)

        # matching words/tokens
        words = re.findall(tokenPattern, cleaned_line)

        # counting wordcount of a line and adding it ot the respective list
        lineWordCount = len(words)
        linesWordCount.append(lineWordCount)

        # running median calculations
        # because I used a sorted list for the worcounts of lines, now it is straightforward to compute
        # the running median
        # index = int(lineNO/2)
        # if lineNO%2 == 0:
        #     medianNumbers.append(float(linesWordCount[index]))
        # else:
        #     medianNumbers.append(float((linesWordCount[index] + linesWordCount[index+1])/2))
        # lineNO += 1

        # optional profiling
        # print("Line NO: " + str(lineNO) + " wordcount: " + str(lineWordCount))
        # print("Size: " + str(len(linesWordCount)) + " linesWordCount elm: " + str(linesWordCount) )
        # print("Median NOs: " + str(medianNumbers))
        # end =  time.clock()

    # optional profiling
    # print("(Calculator)Time elapsed: ", (end-start), "Using Multiprocessing, Generated ", len(medianNumbers) , " medians from " , lineNO, " Lines")#, len(text) , " files")

    return {fileNum: linesWordCount}