__author__ = 'Ahmed Assal'


import re, sys
sub_pattern = re.compile(r"['\d-]?")
#token_pattern = re.compile(r'([a-zA-Z]+[\d\'-]?[a-zA-Z]*)')
token_pattern = re.compile(r'([a-zA-Z]+[\d\'-]?[a-zA-Z]*)')
linesWordCount = []

def MedianCalculator(file_num, text):
    """thread worker function"""
    medianNumbers= []
    for line in text:
        cleaned_line = re.sub(sub_pattern,"",line)
        words = re.findall(token_pattern, cleaned_line)
        lineWordCount = len(words)
        # print(line)

        linesWordCount.append(lineWordCount)
    # words = re.findall(token_pattern, text.lower())
    # words = text.lower().split()
    # print(words)
    # wordcount = [ (word, 1) for word in words ]
    print(linesWordCount)
    for i in range(len(linesWordCount)):
        # print("i " + str(i))
        curMedians = sorted(linesWordCount[:i+1], key= lambda v: v, reverse=False)
        # print("curMedians  " + str(curMedians))
        index = int((i)/2)
        # print("index " + str(index))
        if (i)%2 == 0:
            medianNumbers.append(float(curMedians[index]))
        else:
            medianNumbers.append(float((curMedians[index] + curMedians[index+1])/2))

        # print("medianNum  " +str(medianNumbers))

    # medianNumbers = [count[i]+count[i-1]/2 if i%2!= 0 else for count in lineWordCount, for i in (range(len(lineWordCount))]
    #####################
    # wordcount = {}
    # for word in words:
    #     if word in wordcount:
    #         wordcount[word] += 1
    #     else:
    #         wordcount[word] = 1
    # medianNumbers = []
    ######################
    # wordcount[word] = [ 1 if word not in wordcount else wordcount[word]+1 for word in words ]
    # wordcount2 = { word: 1 if word not in wordcount2 for word in words }
    # wordcount2 = { word: 1 for word in words }
    # wordcount3 = { word: words.count(word) for word in words }
    # wordcount4 = { word1: [(word2, 1) if word2 == word1 else (word2, 0 )for word2 in words ] for word1 in words}

    #########################
    # sortedbyfrequency = sorted(wordcount, key=lambda k: k , reverse=False)
    # print(sortedbyfrequency)
    # WriteTXT(sortedbyfrequency, file_num, wordcount)
    # print("TokenizerV2 , File No.: ", file_num, wordcount)
    return medianNumbers
