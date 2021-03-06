__author__ = 'Ahmed Assal'

################################################
# Required module for the sequential and
# parallel implementations of wordcount
# calculations
#
################################################

import sys, os
import multiprocessing as mp
import tokenizers as toks

def mp_WcDataLoader(path):
    """
    wordcount data loader for the Multiprocessing package implementation.
    it returns the list of input files only. It does not load the actual data,
    which is done at a later stage at each of the worker functions.

    :rtype :        list of strings
    :param path:    the path of the input text files
    :return:        list of input text file paths
    """

    # gets the files names for the input files at the supplied path argument
    files = os.listdir(path)
    return files



def seq_WcDataLoader(path, text):
    """
    wordcount data loader for the sequential implementation
    it loads the text of every input text file into a list and then adds
    these lists to a master list, text.

    :rtype :        list of strings
    :param path:    the path of the input text files
    :param text:    text buffer, a list of lists, each stores the content of one input file.
    :return:        sorted list of input text file paths
    """
    # gets the files names for the input files at the supplied path argument
    files = os.listdir(path)

    # sorts filenames alphabetically
    files=sorted(files, key = lambda v: v, reverse=False)

    # Iterates over the different input files, attempts to open them, loads their content, line-by-line to a list,
    # txtFile.It then adds the list for each file to the master text list, text.
    for file in files:
        try:
            f = open(path + str(file), "rU")
        except:
            print('Cannot open file %s for reading' % f)
            sys.exit(1)
        txtFile = []

        # adds file lines to the list of the opened file
        for line in f:
            txtFile.append(line)

        # appends the input file's list to the master text list
        text.append(txtFile)
        f.close()
    return files

def mp_WcScheduler(path, *files):
    """
    A basic scheduler for the wordcount implementation using Multiprocessing package.
    It creates a pool of processes based on the number of cores available and then invokes these processes.
    It then collects their outputs which are dictionaries of the words and their counts, and then pack these
    dictionaries into a master list

    :rtype :        list of dictionaries of words and their counts
    :param path:    the path of the input text files
    :param files:   list of input text file names
    :return:        list of dictionaries each containing the words and their counts in the input files.
    """
    # gets the number of input files
    filesLength = len(files)

    # creates a pool of worker processes, leaves the determination of the num of processes to the multiprocessing
    # package to decide depending on the number of processor cores, that is what the processes=None parameter for.
    pool = mp.Pool(processes=None)

    # invokes the different worker processes, the Tokenizers and passes them the arguments
    results = [pool.apply_async(toks.WcTokenizer, args=(x, files, path)) for x in range(filesLength)]

    # collects the output of the worker processes, the tuples list, into a master list.
    output = [p.get() for p in results]

    pool.close()
    pool.join()
    return output