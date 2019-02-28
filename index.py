#!/usr/bin/env python3

import sys
from collections import OrderedDict

if len(sys.argv) == 2:
    fd = open(sys.argv[1], "r")
else:
    fd  = open("Input", "r")

FileLines = fd.read().split('\n')
print(FileLines)
Dic = OrderedDict()

def AddToDict(Tag):
    if Tag in list(Dic.keys()):
        return Dic[Tag]
    else:
        if len(list(Dic.keys())):
            Dic[Tag] = Dic[list(Dic.keys())[-1]]+1
            return Dic[Tag]
        else:
            Dic[Tag] = 0
            return 0

FotoAmmount = int(FileLines[0])

AllPhotos = list(map(lambda x: x.split(" "), FileLines[1:(len(FileLines)-1)]))

#print(AllSlides)

ParsedPhotos = list()

ParsedTags = list()

for Photo in AllPhotos:
    #print([Slide[x+1] for x in range(int(Slide[1])-1)])
    templ = list()
    # H == 0  V == 1
    templ.append(1 if Photo[0] == "V" else 0)
    templ.append(int(Photo[1]))
    ParsedPhotos.append(templ+[AddToDict(Photo[x+2]) for x in range(int(Photo[1]))])
#print(Dic)
print(ParsedPhotos)
