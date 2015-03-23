__author__ = 'Ahmed Assal'
# import from numpy as np
# import from boost as
import sys, os, re, datetime


# files = []
input_path = "wc_input/"
files = os.listdir(input_path)
# print(len(files))
# print('-' * (len(files)+4))
# print(files)

# if len(sys.argv) >= 2:
#     for file in sys.argv[1:]:
#         files.append("wc_input/"+str(file))
# else:
#     print("usage: wordcountSerial.py file1 file2 file3 ...")

words_to_ignore = []
things_to_strip0 = [".", ",", "?", "(", ")", "\"", ":", ";", "'s"]
things_to_strip = ["\'"]
words_min_size = 1
print_in_html = False


text = ""
for file in files:
    try:
        f = open(input_path+str(file), "rU")
    except:
        print( 'Cannot open file %s for reading' % f)
        sys.exit(0)

    for line in f:
        # pretext = re.match('', line)
        text+=line
    f.close()
sub_pattern = re.compile(r"['\d-]?")
#token_pattern = re.compile(r'([a-zA-Z]+[\d\'-]?[a-zA-Z]*)')
token_pattern = re.compile(r'([a-zA-Z]+[\d\'-]?[a-zA-Z]*)')
cleaned_text = re.sub(sub_pattern,"",text)
words = re.findall(token_pattern, cleaned_text.lower())
#words = re.findall(token_pattern, text.lower())
#words = text.lower().split()
# print(words)
wordcount = {}
for word in words:
#     # print(word)
#     # new_word = re.match(r'', word)
#     # for thing in things_to_strip:
#     #     if thing in word:
#     #         word = word.replace(thing, "")
#     # if word not in words_to_ignore and len(word)>=words_min_size:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
print(wordcount)
#wordcount[word] = [ 1 if word not in wordcount else wordcount[word]+1 for word in words ]

# wordcount2 = { word: 1 if word not in wordcount2 for word in words }
wordcount2 = { word: 1 for word in words }
print(wordcount2)

wordcount3 = { word: words.count(word) for word in words }

print(wordcount3)
#wordcount4 = { word1: [(word2, 1) if word2 == word1 else (word2, 0 )for word2 in words ] for word1 in words}
#print(wordcount4)
def sorting_key(k):
    return (k)


# sortedbyfrequency = sorted(wordcount, key=lambda k: k, reverse=False)


def print_txt(sortedbyfrequency):
    wc_output_file = open("wc_output/wc_result.txt", "w")
    wc_output_file.write(str(datetime.datetime.today())+ "\n")
    wc_output_file.write(str(len(sortedbyfrequency))+ "\n")

    for word in sortedbyfrequency:
        wc_output_file.write(word + "\t" + repr(wordcount[word]) + "\n")
        #print("%s \t%s" %(word, wordcount[word]))
    wc_output_file.close()

    median_output_file = open("wc_output/med_result.txt", "w")
    median_output_file.write(str(datetime.datetime.today())+ "\n")
    median_output_file.close()

def print_html(sortedbyfrequency):
    print("<html><head><title>Wordcount.py Output</title></head><body><table>")
    for word in sortedbyfrequency:
        print("<tr><td>%s</td><td>%s</td></tr>" % (word,wordcount[word]))
        print("</table></body></html>")

# if print_in_html == True:
#     WriteHTML(sortedbyfrequency)
# else:
#     WriteTXT(sortedbyfrequency)