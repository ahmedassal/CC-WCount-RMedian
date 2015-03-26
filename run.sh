#!/usr/bin/env bash

function pause(){
    read -p "$*"
}
#$NUM = 100
function explodeData(){
    for i in $(seq 1 100)
    do
        cp wc_input/pride_and_prejudice.txt wc_input/file_$i
    done
}

function delExplodedData(){
for i in $(seq 1 100)
    do
        rm wc_input/file_$i
    done

}
#sudo pip install sortedcontainers
#sudo pip install line_profiler
#pip install -U pip


#wget -O 'wc_input/count_of_monte_cristo.txt' http://www.gutenberg.org/cache/epub/1184/pg1184.txt
#wget -O 'wc_input/pride_and_prejudice.txt' http://www.gutenberg.org/cache/epub/1342/pg1342.txt
#wget -O 'wc_input/adventures_of_huckleberry_finn.txt' http://www.gutenberg.org/cache/epub/76/pg76.txt
#wget -O 'wc_input/alice_in_wonderland.txt' http://www.gutenberg.org/cache/epub/11/pg11.txt


#explodeData
cd src/
echo -en "\ec"
echo -e "First problem - wordcount.\n"
pause "Let's try the sequential implementation...[Press Enter]"
echo -e "\n"
python3.4 wordcountSequential.py
echo -e "\n"
pause "Then the multiprocessing implementation...[Press Enter]"
echo -e "\n"
python3.4 wordcountMultiprocessing.py
echo -e "\nSecond problem - the running median\n"
pause "Let's try the sequential implementation...[Press Enter]"
echo -e "\n"
python3.4 runningMedianSequential.py
echo -e "\n"
pause "Then the multiprocessing implementation...[Press Enter]"
echo -e "\n"
python3.4 runningMedianMultiprocessing.py
echo -e "\n"

cd ..
cp wc_output/seq_wc_result.txt wc_output/wc_result.txt
cp wc_output/seq_med_result.txt wc_output/med_result.txt

#delExplodedData