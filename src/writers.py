__author__ = 'Ahmed Assal'

import datetime

def Writer(output_path, sortedWords, wordcount, write_in_html = False, partial=False, file_no=0):
    if write_in_html == True:
        WriteHTML(output_path, sortedWords, wordcount, partial, file_no)
    else:
        WriteTXT(output_path, sortedWords, wordcount, partial, file_no)

def WriteTXT(output_path, sortedWords, wordcount, partial=False, file_no=0):
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

def WriteHTML(output_path, sortedWords, wordcount, partial=False, file_no=0):
    if (not partial):
        wc_output_file = open(output_path + "wc_result.html", "w")
        wc_output_file.write("<html><head><title>wordcountSerial.py output</title></head><body><table>")
    for word in sortedWords:
        wc_output_file.write("<tr><td>%s</td><td>%s</td></tr>" % (word,wordcount[word]))
    wc_output_file.write("</table></body></html>")
    wc_output_file.close()

    median_output_file = open(output_path +"med_result.html", "w")
    median_output_file.write("<html><head><title>running median output</title></head><body><table>")
    median_output_file.close()
