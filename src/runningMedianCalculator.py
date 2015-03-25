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

# based on the assumptions, hyphens, digits or apostrophes appear mid-word are not assumed to be word
# boundaries, i.e., they can be deleted safely and the token can be captured as if they were not present.
#
# the regular expression pattern used for the deletion of digits, hyphens, and apostrophes.
# subPattern = re.compile(r"['\d-]?")

# the regular expression pattern used for matching a token/word
# word/token is any number of alphabetic symbols followed by an optional one or zero occurrence of
# digit/hyphen/apostrophe and then an optional any number of alphabetic symbols.
# token_pattern = re.compile(r'([a-zA-Z]+[\d\'-]?[a-zA-Z]*)')
# tokenPattern = re.compile(r'([a-zA-Z]+[\d\'-]?[a-zA-Z]*)')
# punctuationPattern = re.escape(r'[%s]' % re.escape(string.punctuation))
# table = str.maketrans("","", string.punctuation.join("0123456789"))
# table = str.maketrans(string.ascii_uppercase,string.ascii_lowercase, string.punctuation.join("0123456789"))
# charsToDel = string.punctuation.translate(str.maketrans("", "", "`'-_"))+"0123456789"
# table = str.maketrans(string.ascii_uppercase,string.ascii_lowercase, charsToDel)
# tokenPattern = re.compile(r'([a-z]+)')

table = str.maketrans(string.ascii_uppercase ,string.ascii_lowercase , "`'-_")
tokenPattern = re.compile(r'([a-z]+)')

def MedianCalculator(fileNum, text):
    """thread worker function"""
    start = time.clock()
    medianNumbers= []
    linesWordCount = SortedList()
    lineNO = 0
    for line in text:
        # cleaned_line = re.sub(sub_pattern,"",line)
        # cleaned_line = line.strip(string.punctuation)
        cleaned_line = line.translate(table)

        words = re.findall(tokenPattern, cleaned_line)
        lineWordCount = len(words)
        linesWordCount.add(lineWordCount)
        index = int(lineNO/2)
        if lineNO%2 == 0:
            medianNumbers.append(float(linesWordCount[index]))
        else:
            medianNumbers.append(float((linesWordCount[index] + linesWordCount[index+1])/2))
        lineNO += 1
        # print("Line NO: " + str(lineNO) + " wordcount: " + str(lineWordCount))
        # print("Size: " + str(len(linesWordCount)) + " linesWordCount elm: " + str(linesWordCount) )
        # print("Median NOs: " + str(medianNumbers))
    end =  time.clock()
    # print("(Calculator)Time elapsed: ", (end-start), "Using Multiprocessing, Generated ", len(medianNumbers) , " medians from " , lineNO, " Lines")#, len(text) , " files")

    # medianNumbers = [count[i]+count[i-1]/2 if i%2!= 0 else for count in lineWordCount, for i in (range(len(lineWordCount))]
    return medianNumbers
