from gi.module import maketrans

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

# from string import maketrans

# based on the assumptions, hyphens, digits or apostrophes appear mid-word are not assumed to be word
# boundaries, i.e., they can be deleted safely and the token can be captured as if they were not present.
# regular expression pattern used for the deletion of digits, hyphens, and apostrophes

# subPattern = re.compile(r"['\d-]?")
# tokenPattern = re.compile(r'([a-zA-Z]+[\d\'-]?[a-zA-Z]*)')
# table = str.maketrans(string.ascii_uppercase,string.ascii_lowercase, "`'-_")
# punctuationToSpace = string.punctuation.translate(str.maketrans("", "", "`'-_"))+"0123456789"
# table = str.maketrans(string.ascii_uppercase + punctuationToSpace,string.ascii_lowercase + " "*len(punctuationToSpace), "`'-_")
# tokenPattern = re.compile(r'([a-z]+[\']?[a-z]*)')
# table = str.maketrans("","", string.punctuation.join("0123456789"))

table = str.maketrans(string.ascii_uppercase ,string.ascii_lowercase , "`'-_")
tokenPattern = re.compile(r'([a-z]+)')

def TokenizerV1(file_num, text):
    """thread worker function"""
    # cleaned_text = re.sub(sub_pattern,"",text[file_num])
    # cleaned_text = text[file_num].strip(string.punctuation)
    cleaned_text = text[file_num].translate(table)
    # words = re.findall(tokenPattern, cleaned_text.lower())
    words = re.findall(tokenPattern, cleaned_text)
    wordcount = {}
    for word in words:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    return wordcount

def TokenizerV2(text):
    """thread worker function"""
    # cleaned_text = re.sub(sub_pattern,"",text)
    # cleaned_text = text.strip(string.punctuation)
    cleaned_text = text.translate(table)
    # words = re.findall(tokenPattern, cleaned_text.lower())
    words = re.findall(tokenPattern, cleaned_text)
    wordcount = [ (word, 1) for word in words ]
    return wordcount


def textLoader(filename):
    lines = ""
    try:
        f = open(filename, "rU")
    except:
        print('Cannot open file %s for reading' % f)
        sys.exit(1)
    for  line in f:
        lines += line
    f.close()
    return lines


def TokenizerV3(file_num, files, path):
    """thread worker function"""
    text = textLoader(path+files[file_num])
    # cleaned_text = re.sub(sub_pattern,"",text)
    # cleaned_text = text.strip(string.punctuation)
    cleaned_text = text.translate(table)
    # words = re.findall(tokenPattern, cleaned_text.lower())
    words = re.findall(tokenPattern, cleaned_text)
    wordcount = [ (word, 1) for word in words ]
    return wordcount