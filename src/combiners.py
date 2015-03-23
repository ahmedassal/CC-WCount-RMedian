__author__ = 'Ahmed Assal'

from collections import defaultdict
from itertools import chain


def SimpleCombiner(intermediates):
    result = defaultdict(int)
    for k,v in chain(*intermediates):
        result[k] += v
    return result

