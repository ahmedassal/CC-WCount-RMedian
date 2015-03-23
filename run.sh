#!/usr/bin/env bash

pip install -U pip
pip install -U itertools
pip install -U numpy

#wget -O 'wc_input/count_of_monte_cristo.txt' http://www.gutenberg.org/cache/epub/1184/pg1184.txt
#wget -O 'wc_input/pride_and_prejudice.txt' http://www.gutenberg.org/cache/epub/1342/pg1342.txt
#wget -O 'wc_input/adventures_of_huckleberry_finn.txt' http://www.gutenberg.org/cache/epub/76/pg76.txt
#wget -O 'wc_input/alice_in_wonderland.txt' http://www.gutenberg.org/cache/epub/11/pg11.txt


python wordcount.py