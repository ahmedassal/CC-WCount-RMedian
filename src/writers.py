__author__ = 'Ahmed Assal'

################################################
# Various file writers for the wordcount and the
# running medians algorithms
#
################################################

import datetime

def wcWriter(output_path, sortedWords, wordcount, algType, write_in_html = False):
    """
    wordcount wrapper for the different file writers. It invokes the respective writer based on the requested file format

    :rtype :            null
    :param output_path: the path the results file will be written to
    :param sortedWords: the list of alphabetically sorted words that are to be written to the file
    :param wordcount:   the dictionary containing the wordcounts final results. key: word, value: count
    :param algType:     the prefix used for the results file name, seq_ for sequential, and mp_ for multiprocessing
    :param write_in_html: flag that indicates whether the final results is to be written in HTML or TXT file format
    """

    if write_in_html:
        wcWriteHTML(output_path, sortedWords, wordcount, algType)
    else:
        wcWriteTXT(output_path, sortedWords, wordcount, algType)

def medWriter(output_path, medians, algType, write_in_html = False):
    """
    running medians wrapper for the different file writers.s. It invokes the respective writer based on the requested
    file format

    :rtype :            null
    :param output_path: the path the results file will be written to
    :param medians:     the list of medians that are to be written to the file
    :param algType:     the prefix used for the results file name, seq_ for sequential, and mp_ for multiprocessing
    :param write_in_html: flag that indicates whether the final results is to be written in HTML or TXT file format
    """

    if write_in_html:
        medWriteHTML(output_path,medians, algType)
    else:
        medWriteTXT(output_path,medians, algType)


def wcWriteTXT(output_path, sortedWords, wordcount, algType):
    """
    wordcount text file writer for the results.

    :rtype :            null
    :param output_path: the path the results file will be written to
    :param sortedWords: the list of alphabetically sorted words that are to be written to the file
    :param wordcount:   the dictionary containing the wordcounts final results. key: word, value: count
    :param algType:     the prefix used for the results file name, seq_ for sequential, and mp_ for multiprocessing
    """

    wc_output_file = open(output_path + algType +"wc_result.txt", "w")
    wc_output_file.write(str("Created on " + str(datetime.datetime.today())+ "\n"))
    wc_output_file.write("Number of words: " + str(len(sortedWords))+ "\n")

    for word in sortedWords:
        wc_output_file.write(word + "\t" + repr(wordcount[word]) + "\n")
    wc_output_file.close()


def wcWriteHTML(output_path, sortedWords, wordcount, algType):
    """
    wordcount html file writer for the results.

    :rtype :            null
    :param output_path: the path the results file will be written to
    :param sortedWords: the list of alphabetically sorted words that are to be written to the file
    :param wordcount:   the dictionary containing the wordcounts final results. key: word, value: count
    :param algType:     the prefix used for the results file name, seq_ for sequential, and mp_ for multiprocessing
    """

    wc_output_file = open(output_path + algType +"wc_result.html", "w")
    wc_output_file.write("<html><head><title>wordcountSequential.py output</title></head><body><table>")
    for word in sortedWords:
        wc_output_file.write("<tr><td>%s</td><td>%s</td></tr>" % (word,wordcount[word]))
    wc_output_file.write("</table></body></html>")
    wc_output_file.close()



def medWriteTXT(output_path, medians, algType):
    """
    running medians text file writer for the results.

    :rtype :            null
    :param output_path: the path the results file will be written to
    :param medians:     the list of medians that are to be written to the file
    :param algType:     the prefix used for the results file name, seq_ for sequential, and mp_ for multiprocessing
    """

    median_output_file = open(output_path + algType +"med_result.txt", "w")
    median_output_file.write(str("Created on " + str(datetime.datetime.today())+ "\n"))
    median_output_file.write("Number of lines: " +  str(len(medians))+ "\n")
    for median in medians:
        median_output_file.write(str(median) +"\n")
    median_output_file.close()

def medWriteHTML(output_path, medians, algType):
    """
    running medians html file writer for the results.

    :rtype :            null
    :param output_path: the path the results file will be written to
    :param medians:     the list of medians that are to be written to the file
    :param algType:     the prefix used for the results file name, seq_ for sequential, and mp_ for multiprocessing
    """

    median_output_file = open(output_path + algType +"med_result.html", "w")
    median_output_file.write("<html><head><title>running median output</title></head><body><table>")
    for median in medians:
        median_output_file.write("<tr><td>%s</td></tr>" % median)
    median_output_file.write("</table></body></html>")
    median_output_file.close()
