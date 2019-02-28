#!/usr/bin/env python3

from index.py import *
from output.py import *
from math import modf

MAX = 1000000.0

def score(photo1, photo2):
    s0 = 0
    s1 = len(photo1)-2
    s2 = len(photo2)-2
    for x in range(len(photo1)-2):
        for y in range(len(photo2)-2):
            if photo1[x+2] == photo2[y+2]:
                s0+=1
                s1-=1
                s2-=1

    return min(s0, s1, s2)

cur = 0
ParsedPhotos[0][0] = 1
slides = [0]

for i in range(len(ParsedPhotos)-1):
    scores = []
    if ParsedPhotos[cur][1] == 1:
        oldcur = cur
        pass
    else:
        for x in range(len(ParsedPhotos[cur])-2):
            tag = ParsedPhotos[cur][x+2]
            for y in ParsedTags[tag]):
                if ParsedPhotos[y][0]:
                    continue
                scores.append(score(ParsedPhotos[y], ParsedPhotos[cur])+y/MAX)

        cur = modf(max(scores))[0]*MAX
        if ParsedPhotos[cur][1] == 0:
            slides.append(cur)
        else:
            oldcur = 1
        ParsedPhotos[cur][0] = 1
