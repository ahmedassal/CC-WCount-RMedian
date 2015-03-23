__author__ = 'Ahmed Assal'

import re
from sortedcontainers import SortedList

sub_pattern = re.compile(r"['\d-]?")
token_pattern = re.compile(r'([a-zA-Z]+[\d\'-]?[a-zA-Z]*)')
linesWordCount = SortedList()


def MedianCalculator(file_num, text):
    """thread worker function"""
    medianNumbers= []
    for line in text:
        cleaned_line = re.sub(sub_pattern,"",line)
        words = re.findall(token_pattern, cleaned_line)
        lineWordCount = len(words)

        linesWordCount.add(lineWordCount)

    print(linesWordCount)
    curMedians = SortedList()
    for i in range(len(linesWordCount)):
        curMedians.update(linesWordCount[:i+1])# = sorted(linesWordCount[:i+1], key= lambda v: v, reverse=False)
        index = int((i)/2)
        if (i)%2 == 0:
            medianNumbers.append(float(curMedians[index]))
        else:
            medianNumbers.append(float((curMedians[index] + curMedians[index+1])/2))

    # medianNumbers = [count[i]+count[i-1]/2 if i%2!= 0 else for count in lineWordCount, for i in (range(len(lineWordCount))]
    return medianNumbers
