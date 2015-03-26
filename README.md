#Insight Data Engineering Coding Challenge 
##Scalable Wordcount and Running Median

###Executive Summary

###The Challenge   
####Wordcount
The first part of the coding challenge is to implement your own version of Word Count that counts all the words from the text files contained in a directory named wc_input and outputs the counts (in alphabetical order) to a file named wc_result.txt, which is placed in a directory named wc_output.   

####Running Median
Another common problem is the Running Median - which keeps track of the median for a stream of numbers, updating the median for each new number. The second part of the coding challenge is to implement a running median for the number of words per line of text. Consider each line in a text file as a new stream of words, and find the median number of words per line, up to that point (i.e. the median for that line and all the previous lines).    
We'd like you to implement your own version of this running median that calculates the median number of words per line, for each line of the text files in the wc_input directory. If there are multiple files in that directory, the files should be combined into a single stream and processed by your running median program in alphabetical order, so a file named hello.txt should be processed before a file named world.txt. The resulting running median for each line should then be outputted to a text file named med_result.txt in the wc_output directory.     

###Requirements
####Github Repository
* You may write your solution in any one of the following programming languages: C, C++, Clojure, Java, Python, Ruby, or Scala.
* Submit a link to a Github repo with your source code.    
* In addition to the source code, the top-most directory of your repo must include wc_input and wc_output directories, and a shell script named run.sh that compiles and runs the Word Count and Running Median programs. 
* If your solution requires additional libraries or dependencies, the shell script should load them first so that your programs can be run on any system just by running run.sh. 
* The figure below is for the required structure of the top-most directory in your repo, or simply clone this repo.   
![](https://github.com/InsightDataScience/cc-example/blob/master/images/directory-pic.png)
     
####Scalability
As a data engineer, it’s important that you write clean, well-documented code that scales for large amounts of data.     
For this reason, it’s important to ensure that your solution works well for small and large text files, rather than just the simple examples above.         

------------------------------------------------------------------------------------------------------------------------------------------------------
##The Solution
###Repository Content
####src/ directory 
It contains the source code for the implementation as follows:

#####wordcountSequential.py     

#####wordcountMultiprocessing.py    

#####scaledRunningWordcount.py     

#####tokenizers.py      



#####runningMedianSequential.py     

#####runningMedianMultiprocessing.py     

#####scaledRunningMedian.py      

#####runngingMedianCalculator.py     


#####combiners.py     

#####writers.py     

###Instructions

###Procedures / word abut the implementation

------------------------------------------------------------------------------------------------------------------------------------------------------
##Results
####IDE    
JetBrains' PyCharm 4.0.5.   

####Computing Platform    
The implementation was tested on Intel® Core™2 Duo CPU E7500 @ 2.93GHz (Dual Core), 4 GB RAM, Intel G41 Builtin Display chipset, Ubuntu 14.04 LTS 64-bit.   

####Test Data   
11 text files of a total of 8 MB. They include:
* Adventures of Huckleberry Finn(2 copies)
* Alice in Wonderland (2 copies)
* Count of Mont Cristo (2 copies)
* Pride and Prejudice (2 copies)
* small text files that test special patterns (3 files)

run.sh makes 100 copies of the file Pride and Prejudice.txt which is the largest in the test dataset, 700KB, for expanding the size of the test data. The script 
then deletes these copies when it finishes.

####Perfromance
#####Wordcount    
* The sequential implementation of my wordcount algorithm finished in about 3.15 seconds.    
* The multiprocessing implementation finished in about 1.15 second.     
* This enhancement in the performance is a factor of 2.74.    
       
#####Running medians
* The sequential implementation of my wordcount algorithm finished in about 6.15 seconds.    
* The multiprocessing implementation finished in about 0.36 second.     
* This enhancement in the performance is a factor of 17.  

###Future Work
Good examples of scalability of this classic problem exist. Their implementations are highly performing. 
Some of these implementations will be based on:  MPI4Py, Pycuda,MapReduce, ... If there is enough time before the 
review of my implementation I will implement one of these implementation. I am currently working on an MPI4Py 
implementation.       

###Conclusion
