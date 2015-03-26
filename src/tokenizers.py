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

# delete all punctuation and digits
# table = str.maketrans(string.ascii_uppercase,string.ascii_lowercase, string.punctuation.join("0123456789"))

# Alternative 3
# the regular expression pattern used for matching a token/word
# word/token is any number of alphabetic symbols
tokenPattern = re.compile(r'([a-z]+)')

# old slower implementation of the tokenizer
def TokenizerV1(file_num, text):
    """thread worker function"""

    cleaned_text = text[file_num].translate(table)
    words = re.findall(tokenPattern, cleaned_text)
    wordcount = {}
    for word in words:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    return wordcount

# old implementation of the tokenizer that does not load the text itself but use the text provided in the arg list
# This approach is for distributing the loading of data among the different processes
def TokenizerV2(text):
    """thread worker function"""

    cleaned_text = text.translate(table)
    words = re.findall(tokenPattern, cleaned_text)
    wordcount = [ (word, 1) for word in words ]
    return wordcount


def textLoader(filename):
    """


    :rtype :            list of strings
    :param filename:    path and filename for the input text file to be loaded into the lines list
    :return:            list of lines of text from the input file
    """
    # the list which is going to hold the text lines
    lines = ""

    try:
        f = open(filename, "rU")
    except:
        print('Cannot open file %s for reading' % f)
        sys.exit(1)

    # iterates over the different file lines and add them to list
    for  line in f:
        lines += line

    f.close()
    return lines


def WcTokenizer(file_num, files, path):
    """
    thread worker function
    Computes the wordcount for text list supplied. Text loading into the text list is delegated to textLoader(filename).
    This approach is for distributing the loading of data among the different processes.
    Currently the sequential implementation is identical to the parallel implementation.

    :rtype :            null
    :param file_num:    an index pointing to the file to be processing in the input files
    :param files:       list of input text files
    :param path:        path to the input text files
    """

    # Data Loading
    # loads the input text off the input file, the scheduler or the invoking pipeline decides which file to
    # load using the supplied file number.
    text = textLoader(path+files[file_num])

    # is a fast conversion of uppercase to lowercase and removal of the following `'-_
    cleaned_text = text.translate(table)

    # matching words/tokens
    words = re.findall(tokenPattern, cleaned_text)

    # emits a tuple (word,1) for every occurrence of the word, ata a later stage the combiner/reducer will sum these
    # occurrences into a wordcount
    wordcount = [ (word, 1) for word in words ]

    # return the wordcount list. list of tuples [(word1, 1), (word2, 1), ..., (word1, 1)]
    return wordcount