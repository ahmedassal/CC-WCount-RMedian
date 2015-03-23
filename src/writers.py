__author__ = 'Ahmed Assal'

import datetime

def wcWriter(output_path, sortedWords, wordcount, write_in_html = False, partial=False, file_no=0):
    if write_in_html == True:
        wcWriteHTML(output_path, sortedWords, wordcount, partial, file_no)
    else:
        wcWriteTXT(output_path, sortedWords, wordcount, partial, file_no)

def medWriter(output_path, medians, write_in_html = False, partial=False, file_no=0):
    if write_in_html == True:
        medWriteHTML(output_path,medians, partial, file_no)
    else:
        medWriteTXT(output_path,medians, partial, file_no)

def wcWriteTXT(output_path, sortedWords, wordcount, partial=False, file_no=0):
    if (not partial):
        wc_output_file = open(output_path + "wc_result.txt", "w")
        wc_output_file.write(str("Created on " + str(datetime.datetime.today())+ "\n"))
        wc_output_file.write("Number of words: " + str(len(sortedWords))+ "\n")
    else:
        wc_output_file = open(output_path + "partial/"+"wc_result"+str(file_no)+".txt", "w")
        wc_output_file.write(str("File number: "+ str(file_no) + " Created on " + str(datetime.datetime.today())+ "\n"))
        wc_output_file.write("Number of words: " +  str(len(sortedWords))+ "\n")

    for word in sortedWords:
        wc_output_file.write(word + "\t" + repr(wordcount[word]) + "\n")
    wc_output_file.close()

    median_output_file = open(output_path +"med_result.txt", "w")
    median_output_file.write(str("Created on " + str(datetime.datetime.today())+ "\n"))
    median_output_file.close()

def wcWriteHTML(output_path, sortedWords, wordcount, partial=False, file_no=0):
    if (not partial):
        wc_output_file = open(output_path + "wc_result.html", "w")
        wc_output_file.write("<html><head><title>wordcountSequential.py output</title></head><body><table>")
    for word in sortedWords:
        wc_output_file.write("<tr><td>%s</td><td>%s</td></tr>" % (word,wordcount[word]))
    wc_output_file.write("</table></body></html>")
    wc_output_file.close()

    median_output_file = open(output_path +"med_result.html", "w")
    median_output_file.write("<html><head><title>running median output</title></head><body><table>")
    median_output_file.close()


def medWriteTXT(output_path, medians, partial=False, file_no=0):
    median_output_file = open(output_path +"med_result.txt", "w")
    median_output_file.write(str("Created on " + str(datetime.datetime.today())+ "\n"))
    median_output_file.write("Number of lines: " +  str(len(medians))+ "\n")
    for median in medians:
        median_output_file.write(str(median) +"\n")
    median_output_file.close()

def medWriteHTML(output_path, medians, partial=False, file_no=0):
    median_output_file = open(output_path +"med_result.html", "w")
    median_output_file.write("<html><head><title>running median output</title></head><body><table>")
    for median in medians:
        median_output_file.write("<tr><td>%s</td></tr>" % median)
    median_output_file.write("</table></body></html>")
    median_output_file.close()
