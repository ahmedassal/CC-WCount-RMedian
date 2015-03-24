#!/usr/bin/env bash

function pause(){
    read -p "$*"
}
#sudo pip install sortedcontainers
#sudo pip install line_profiler
#pip install -U pip


#wget -O 'wc_input/count_of_monte_cristo.txt' http://www.gutenberg.org/cache/epub/1184/pg1184.txt
#wget -O 'wc_input/pride_and_prejudice.txt' http://www.gutenberg.org/cache/epub/1342/pg1342.txt
#wget -O 'wc_input/adventures_of_huckleberry_finn.txt' http://www.gutenberg.org/cache/epub/76/pg76.txt
#wget -O 'wc_input/alice_in_wonderland.txt' http://www.gutenberg.org/cache/epub/11/pg11.txt

cd src/
echo -en "\ec"


#PYHONPATH="${PYTHONPATH}:/home/administrator/PycharmProjects/CC-WCount-RMedian"
#setenv PYHONPATH="${PYTHONPATH}:/home/administrator/PycharmProjects/CC-WCount-RMedian"
#PYHONPATH="${PYTHONPATH}:/home/administrator/PycharmProjects/CC-WCount-RMedian/src"
#setenv PYHONPATH="${PYTHONPATH}:/home/administrator/PycharmProjects/CC-WCount-RMedian/src"
echo -e "First problem - wordcount.\n"
pause "Let's try the sequential implementation...[Press Enter]"
python3.4 wordcountSequential.py
pause "Then the multiprocessing implementation...[Press Enter]"
python3.4 wordcountMultiprocessing.py
pause "That's an improvement of a factor of 2.74 in the prefromance...[Press Enter]"
echo -e "Second problem - the running median\n"
pause "Let's try the sequential implementation...[Press Enter]"
python3.4 runningMedianSequential.py
pause "Then the multiprocessing implementation...[Press Enter]"
python3.4 runningMedianMultiprocessing.py
pause "That's an improvement of a factor of  in the prefromance."
#python src/menu.py