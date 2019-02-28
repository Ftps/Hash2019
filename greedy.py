#!/usr/bin/env python3

from index.py import *
from output.py import *

MAX = 100000

def score(photo1, photo2):
    s0 = 0
    s1 = len(photo1)-2
    s2 = len(photo2)-2
    for x in range(len(photo1)-2):
        for y in range(len(photo2)-2):
            if photo1[x+2] == photo2[y+2]:
                s0++
                s1--
                s2--

    return min(s0, s1, s2);

cur = 0
ParsedPhotos[0][0] = 1
slides = [1]

for i in range(len(ParsedPhotos-1)):
    scores = []
    photo = []
    if ParsedPhotos[cur][0]:
        pass
    else:
        for x in range(len(ParsedPhotos[cur])-2):
            tag = ParsedPhotos[cur][x+2]
            for y in ParsedTags[tag]):
                if ParsedPhotos[y][0]:
                    continue
                scores.append(score(ParsedPhotos[y], ParsedPhotos[cur]))
                photo.append(y)
