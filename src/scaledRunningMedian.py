__author__ = 'Ahmed Assal'

################################################
# Required module for the sequential and
# parallel implementations of the running
# medians calculations
#
################################################

import sys
import os
import multiprocessing as mp
import runningMedianCalculator as medCalc

def seq_MedDataLoader(path, text):
    """
    the running median data loader for the sequential implementation.
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
        for  line in f:
            text.append(line)

        # appends the input file's list to the master text list
        # text.append(txtFile)
        f.close()
    return files

def mp_MedDataLoader(path, text):
    """
    the running median data loader for the parallel implementation using Multiprocessing.
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
        for  line in f:
            txtFile.append(line)

        # appends the input file's list to the master text list
        text.append(txtFile)
        f.close()
    return files

def mp_MedScheduler(text):
    """
    A basic scheduler for the running median implementation using Multiprocessing package.
    It creates a pool of processes based on the number of cores available and then invokes these processes.
    It then collects their outputs which are lists of the running median, and then pack these
    lists into a master list

    :rtype :        list of list of text
    :param path:    the path of the input text files
    :param files:   list of input text file names
    :return:        the master list of the text content of the input files. This is a list of lists where
                    the innermost lists contain the text content for each input file.
    """
    # gets the number of input files
    textPoolLength = len(text)

    # creates a pool of worker processes, leaves the determination of the num of processes to the multiprocessing
    # package to decide depending on the number of processor cores, that is what the processes=None parameter for.
    pool = mp.Pool(processes = None)

    # invokes the different worker processes, the Tokenizers and passes them the arguments
    results = [pool.apply_async(medCalc.MedCalculator, args=(x, text[x])) for x in range(textPoolLength)]

    # collects the output of the worker processes, the lists, into a master list.
    output = [p.get() for p in results]

    pool.close()
    pool.join()
    return output

def mp_MedScheduler2(text):
    """
    A basic scheduler for the running median implementation using Multiprocessing package.
    It creates a pool of processes based on the number of cores available and then invokes these processes.
    It then collects their outputs which are lists of the running median, and then pack these
    lists into a master list

    :rtype :        list of list of text
    :param path:    the path of the input text files
    :param files:   list of input text file names
    :return:        the master list of the text content of the input files. This is a list of lists where
                    the innermost lists contain the text content for each input file.
    """
    # gets the number of input files
    textPoolLength = len(text)

    # creates a pool of worker processes, leaves the determination of the num of processes to the multiprocessing
    # package to decide depending on the number of processor cores, that is what the processes=None parameter for.
    pool = mp.Pool(processes = None)

    # invokes the different worker processes, the Tokenizers and passes them the arguments
    results = [pool.apply_async(medCalc.mp_MedCalculator2, args=(x, text[x])) for x in range(textPoolLength)]

    # collects the output of the worker processes, the lists, into a master list.
    output = [p.get() for p in results]

    pool.close()
    pool.join()
    return output