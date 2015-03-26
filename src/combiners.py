__author__ = 'Ahmed Assal'

################################################
# Different reducers for the different
# implementations of the wordcount and running
# median algorithms.
#
################################################

from collections import defaultdict
from itertools import chain



def WcCombiner(intermediates):
    """
    Wordcount Reducer
    merges the intermediate dictionaries that are packed inside the list, intermediates, into one master dictionary.

    :rtype :                master dictionary for the final results
    :param intermediates:   list of tuples lists representing single occurrences of words for each input text file
    :return:                the final results
    """

    # the use of the defaultdict data structures simplifies the summation of values (counts) of the intermediate
    # dictionaries. It only requires one statement, instead of 2, for creating a new key, value pair or
    # updating its values.
    result = defaultdict(int)

    # the following loop iterates over the first dictionary key and value pairs and then iterates over the next dictionary's
    # pairs. It continues until it iterates over all dictionaries that are members of the intermediates. While iterating,
    # a new dictionary is created, result, to hold all the pairs of the intermediate dictionaries, thus effectively
    # merging all of them.
    for k,v in chain(*intermediates):
        result[k] += v
    return result

def MedCombiner(intermediates):
    """
    The Running Medians Reducer
    merges the intermediate lists that are packed inside the outer list, intermediates, into one master flat list.

    :rtype : object         master list of the final results
    :param intermediates:   list of lists of the running medians of each input text file
    :return:                the final results
    """
    # master list of the final results
    result = []

    # iterating over the sub lists for each input file to concatenate them into a master list
    for v in intermediates:
        result+=v
    return result
