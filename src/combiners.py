__author__ = 'Ahmed Assal'

from collections import defaultdict
from itertools import chain
import random


def SimpleCombiner(intermediates):
    # print(*intermediates)
    result = defaultdict(int)
    for k,v in chain(*intermediates):
        result[k] += v
    # print(result)
    return result

