__author__ = 'Ahmed Assal'

import sys, os
import multiprocessing as mp
import tokenizers as toks

def mp_WcDataLoader(path):
    """
    wordcount data loader for the sequential implementation.
    it returns the list of input files only. It does not load the actual data, which is done at a later stage at each
    of the worker functions.

    :rtype :        list of strings
    :param path:    the path of the input text files
    :return:        list of input text file paths
    """
    files = os.listdir(path)
    return files



def seq_WcDataLoader(path, text):
    """
    wordcount data loader for the sequential implementation



    :rtype :        list of strings
    :param path:    the path of the input text files
    :param text:    text buffer, a list of lists, each stores the content of one input file.
    :return:        sorted list of input text file paths
    """
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

def mp_WcScheduler(path, *files):
        """


        :rtype : object
        :param path: 
        :param files: 
        :return: 
        """
        filesLength = len(files)
        pool = mp.Pool(processes=None)
        results = [pool.apply_async(toks.TokenizerV3, args=(x, files, path)) for x in range(filesLength)]
        output = [p.get() for p in results]
        pool.close()
        pool.join()
        return output