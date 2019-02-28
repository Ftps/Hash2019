#!/usr/bin/env python3

from index import *
from output import *
from math import modf

MAX = 1000000.0

def score(set1, set2):
    s0 = len(set1.intersection(set2))
    s1 = len(set1.union(set2)) - len(set1)
    s2 = len(set1.union(set2)) - len(set2)

    return min(s0, s1, s2)

for p in range(len(ParsedPhotos2)):
    if ParsedPhotos2[p][1] == 0:
        slides = [p]
        break;

k = 0
for i in range(len(ParsedPhotos2)-1):
    scores = []
    if type(slides[i-k]) == type(1):
        p = slides[i-k]
        for x in ParsedPhotos2[p][2]:
            for y in ParsedTags[x]:
                if p == y or ParsedPhotos2[p][0] == 1:
                    continue
                scores.append(score(ParsedPhotos2[y][2], ParsedPhotos2[p][2]) + y/MAX)
        cur = int(modf(max(scores))[0]*MAX)
        if ParsedPhotos2[cur][1] == 1:
            slides.append([cur, -1])
            for a in ParsedPhotosV2:
                if a[1] == cur:
                    a[0] = 1
                    print("a " + str(a[1]))
                    break
        else:
            slides.append(cur)
        ParsedPhotos2[cur][0] = 1
    else:
        if slides[i-k][1] == -1:
            for x in ParsedPhotosV2:
                if x[0] == 1:
                    continue;
                if type(slides[i-k-1]) == type(1):
                    scores.append(score(ParsedPhotos2[slides[i-k-1]][2], x[2].union( ParsedPhotos2[slides[i-k][0]][2] ) ) + x[1]/MAX)
                else:
                    scores.append(score(ParsedPhotos2[slides[i-k-1][0]][2].union(ParsedPhotos2[slides[i-k-1][1]][2]), x[2].union(ParsedPhotos2[slides[i-k][0]][2])) + x[1]/MAX)

            cur = int(modf(max(scores))[0]*MAX)
            ParsedPhotos2[cur][0] = 1
            slides[i-k][1] = cur
            k+=1
            for a in ParsedPhotosV2:
                if a[1] == cur:
                    a[0] = 1
                    print("b " + str(a[1]))
                    break
            print(slides[i-k+1])
        else:
            penis = slides[i-k]
            set = ParsedPhotos2[slides[i-k][0]][2].union(ParsedPhotos2[slides[i-k][1]][2])
            for x in set:
                for y in ParsedTags[x]:
                    if y == penis[0] or y == penis[1] or ParsedPhotos2[p][0] == 1:
                        continue
                    scores.append(score(ParsedPhotos2[y][2], set) + y/MAX)
        cur = int(modf(max(scores))[0]*MAX)
        if ParsedPhotos2[cur][1] == 1:
            slides.append([cur, -1])
            for a in ParsedPhotosV2:
                if a[1] == cur:
                    a[0] = 1
                    print("a " + str(a[1]))
                    break
        else:
            slides.append(cur)
        ParsedPhotos2[cur][0] = 1

output(slides, "out.txt")
