#!/usr/bin/env python3

import index.py import *

def score(photo1, photo2):


currentPic = ParsedPhotos[0]

for i in range(len(ParsedPhotos)):
    for x in range(currentPic[1]):
        tag = currentPic[x+2]
        for y in range(ParsedTags[tag]):
