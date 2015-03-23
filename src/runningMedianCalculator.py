__author__ = 'Ahmed Assal'

import re
from sortedcontainers import SortedList
import time

sub_pattern = re.compile(r"['\d-]?")
token_pattern = re.compile(r'([a-zA-Z]+[\d\'-]?[a-zA-Z]*)')



def MedianCalculator(file_num, text):
    """thread worker function"""
    start =  time.clock()
    medianNumbers= []
    linesWordCount = SortedList()
    lineNO = 0
    for line in text:
        cleaned_line = re.sub(sub_pattern,"",line)
        words = re.findall(token_pattern, cleaned_line)
        lineWordCount = len(words)
        linesWordCount.add(lineWordCount)
        index = int((lineNO)/2)
        if (lineNO)%2 == 0:
            medianNumbers.append(float(linesWordCount[index]))
        else:
            medianNumbers.append(float((linesWordCount[index] + linesWordCount[index+1])/2))
        lineNO += 1
        # print("Line NO: " + str(lineNO) + " wordcount: " + str(lineWordCount))
        # print("Size: " + str(len(linesWordCount)) + " linesWordCount elm: " + str(linesWordCount) )
        # print("Median NOs: " + str(medianNumbers))
    end =  time.clock()
    print("(Calculator)Time elapsed: ", (end-start), "Using Multiprocessing, Generated ", len(medianNumbers) , " medians from " , 1 , " file")

    # medianNumbers = [count[i]+count[i-1]/2 if i%2!= 0 else for count in lineWordCount, for i in (range(len(lineWordCount))]
    return medianNumbers
