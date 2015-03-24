__author__ = 'Ahmed Assal'

import sys
import os
import multiprocessing as mp

import tokenizers as toks
import runningMedianCalculator as medCalc


def schedulerV2(path, *files):
        filesLength = len(files)
        pool = mp.Pool(processes=None)
        results = [pool.apply_async(toks.TokenizerV3, args=(x, files, path)) for x in range(filesLength)]
        output = [p.get() for p in results]
        pool.close()
        pool.join()
        return output

def schedulerV3(text):
        textPoolLength = len(text)
        pool = mp.Pool(processes = None)
        results = [pool.apply_async(medCalc.MedianCalculator, args=(x, text[x])) for x in range(textPoolLength)]
        output = [p.get() for p in results]
        # print(output)
        pool.close()
        pool.join()
        return output

def dataLoaderV2(path):
    files = os.listdir(path)
    return files

def dataLoaderV3(path, text):
    files = os.listdir(path)
    files=sorted(files, key = lambda v: v, reverse=False)
    for file in files:
        try:
            f = open(path + str(file), "rU")
        except:
            print('Cannot open file %s for reading' % f)
            sys.exit(1)
        txtFile = []

        for  line in f:
            txtFile.append(line)
        text.append(txtFile)
        f.close()
    return files