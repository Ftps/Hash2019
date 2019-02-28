#!/usr/bin/env python3

from index.py import *
from output.py import *
from math import modf

MAX = 1000000.0

def score(set1, set2):
    s0 = len(set1.intersection(set2))
    s1 = len(set1.union(set2)) - len(set1)
    s2 = len(set1.union(set2]) - len(set2)

    return min(s0, s1, s2)

ParsedPhotos2[0][0] = 1
slides = [0]

for i in range(len(ParsedPhotos2)-1):
    scores = []
    if slides[i] is int:
        p = slides[i]
        for x in ParsedPhotos2[p][2]:
            for y in ParsedTags[x]:
                if p == y or ParsedPhotos2[p][0] == 1:
                    continue
                scores.append(score(ParsedPhotos2[y][2], ParsedPhotos2[p][2]) + y/MAX)
        cur = modf(max(scores))[0]*MAX
        if ParsedPhotos2[cur][0] == 1:
            slides.append([cur, -1])
        else:
            slides.append(cur)
    else:
        if slides[i][1] == -1:
            for x in ParsedPhotosV2:
                if x[0] == 1:
                    continue;
