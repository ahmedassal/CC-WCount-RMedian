__author__ = 'Ahmed Assal'

################################################
# Calculating the wordcounts sequentially
#
################################################
import datetime

def wcWriter(output_path, sortedWords, wordcount, algType, write_in_html = False):
    if write_in_html:
        wcWriteHTML(output_path, sortedWords, wordcount, algType)
    else:
        wcWriteTXT(output_path, sortedWords, wordcount, algType)

def medWriter(output_path, medians, algType, write_in_html = False):
    if write_in_html:
        medWriteHTML(output_path,medians, algType)
    else:
        medWriteTXT(output_path,medians, algType)

def wcWriteTXT(output_path, sortedWords, wordcount, algType):
    wc_output_file = open(output_path + algType +"wc_result.txt", "w")
    wc_output_file.write(str("Created on " + str(datetime.datetime.today())+ "\n"))
    wc_output_file.write("Number of words: " + str(len(sortedWords))+ "\n")

    for word in sortedWords:
        wc_output_file.write(word + "\t" + repr(wordcount[word]) + "\n")
    wc_output_file.close()


def wcWriteHTML(output_path, sortedWords, wordcount, algType):
    wc_output_file = open(output_path + algType +"wc_result.html", "w")
    wc_output_file.write("<html><head><title>wordcountSequential.py output</title></head><body><table>")
    for word in sortedWords:
        wc_output_file.write("<tr><td>%s</td><td>%s</td></tr>" % (word,wordcount[word]))
    wc_output_file.write("</table></body></html>")
    wc_output_file.close()



def medWriteTXT(output_path, medians, algType):
    median_output_file = open(output_path + algType +"med_result.txt", "w")
    median_output_file.write(str("Created on " + str(datetime.datetime.today())+ "\n"))
    median_output_file.write("Number of lines: " +  str(len(medians))+ "\n")
    for median in medians:
        median_output_file.write(str(median) +"\n")
    median_output_file.close()

def medWriteHTML(output_path, medians, algType):
    median_output_file = open(output_path + algType +"med_result.html", "w")
    median_output_file.write("<html><head><title>running median output</title></head><body><table>")
    for median in medians:
        median_output_file.write("<tr><td>%s</td></tr>" % median)
    median_output_file.write("</table></body></html>")
    median_output_file.close()
