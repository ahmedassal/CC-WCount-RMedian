__author__ = 'Ahmed Assal'

import re, sys

sub_pattern = re.compile(r"['\d-]?")
token_pattern = re.compile(r'([a-zA-Z]+[\d\'-]?[a-zA-Z]*)')

def TokenizerV1(file_num, text):
    """thread worker function"""
    cleaned_text = re.sub(sub_pattern,"",text[file_num])
    words = re.findall(token_pattern, cleaned_text.lower())
    wordcount = {}
    for word in words:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    return wordcount

def TokenizerV2(file_num, text):
    """thread worker function"""
    cleaned_text = re.sub(sub_pattern,"",text)
    words = re.findall(token_pattern, cleaned_text.lower())
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
    cleaned_text = re.sub(sub_pattern,"",text)
    words = re.findall(token_pattern, cleaned_text.lower())
    wordcount = [ (word, 1) for word in words ]
    return wordcount