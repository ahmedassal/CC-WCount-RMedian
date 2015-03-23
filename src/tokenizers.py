__author__ = 'Ahmed Assal'

import re, sys
sub_pattern = re.compile(r"['\d-]?")
#token_pattern = re.compile(r'([a-zA-Z]+[\d\'-]?[a-zA-Z]*)')
token_pattern = re.compile(r'([a-zA-Z]+[\d\'-]?[a-zA-Z]*)')

def TokenizerV1(file_num, text):
    """thread worker function"""
    #print(text_pool[process_no])
    cleaned_text = re.sub(sub_pattern,"",text[file_num])
    words = re.findall(token_pattern, cleaned_text.lower())
    #words = re.findall(token_pattern, text.lower())
    #words = text.lower().split()
    # print(words)
    wordcount = {}
    for word in words:
    #     # print(word)
    #     # new_word = re.match(r'', word)
    #     # for thing in things_to_strip:
    #     #     if thing in word:
    #     #         word = word.replace(thing, "")
    #     # if word not in words_to_ignore and len(word)>=words_min_size:

    # print(wordcount)
    #wordcount[word] = [ 1 if word not in wordcount else wordcount[word]+1 for word in words ]

    # wordcount2 = { word: 1 if word not in wordcount2 for word in words }
    #wordcount2 = { word: 1 for word in words }
    #print(wordcount2)

    #wordcount3 = { word: words.count(word) for word in words }
    # print(wordcount3)

    #wordcount4 = { word1: [(word2, 1) if word2 == word1 else (word2, 0 )for word2 in words ] for word1 in words}
    #print(wordcount4)
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

    #sortedbyfrequency = sorted(wordcount, key=lambda k: k , reverse=False)
    # print(sortedbyfrequency)
    # WriteTXT(sortedbyfrequency, file_num, wordcount)
    return wordcount

def TokenizerV2(file_num, text):
    """thread worker function"""
    # print(text)
    cleaned_text = re.sub(sub_pattern,"",text)
    words = re.findall(token_pattern, cleaned_text.lower())
    #words = re.findall(token_pattern, text.lower())
    #words = text.lower().split()
    # print(words)
    wordcount = [ (word, 1) for word in words ]

    #####################
    # wordcount = {}
    # for word in words:
    #     if word in wordcount:
    #         wordcount[word] += 1
    #     else:
    #         wordcount[word] = 1

    ######################
    #wordcount[word] = [ 1 if word not in wordcount else wordcount[word]+1 for word in words ]
    # wordcount2 = { word: 1 if word not in wordcount2 for word in words }
    #wordcount2 = { word: 1 for word in words }
    #wordcount3 = { word: words.count(word) for word in words }
    #wordcount4 = { word1: [(word2, 1) if word2 == word1 else (word2, 0 )for word2 in words ] for word1 in words}

    #########################
    #sortedbyfrequency = sorted(wordcount, key=lambda k: k , reverse=False)
    # print(sortedbyfrequency)
    # WriteTXT(sortedbyfrequency, file_num, wordcount)
    # print("TokenizerV2 , File No.: ", file_num, wordcount)
    return wordcount


def textLoader(filename):
    lines = ""
    # print(filename)
    try:
        f = open(filename, "rU")
    except:
        print('Cannot open file %s for reading' % f)
        sys.exit(1)

    lineNo = 0
    for  line in f:
        lines += line
    # print(filename + " "+ str(len(lines)))
    f.close()
    return lines


def TokenizerV3(file_num, files, path):
    """thread worker function"""
    text = textLoader(path+files[file_num])
    cleaned_text = re.sub(sub_pattern,"",text)
    words = re.findall(token_pattern, cleaned_text.lower())
    wordcount = [ (word, 1) for word in words ]
    return wordcount