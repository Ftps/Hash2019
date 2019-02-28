#!/usr/bin/env python3

import sys
from collections import OrderedDict

if len(sys.argv) == 2:
    fd = open(sys.argv[1], "r")
else:
    fd  = open("Input", "r")

FileLines = fd.read().split('\n')
#print(FileLines)
AllTags = OrderedDict()

def AddToTag(Tag):
    if Tag in list(AllTags.keys()):
        return AllTags[Tag]
    else:
        if len(list(AllTags.keys())):
            AllTags[Tag] = AllTags[list(AllTags.keys())[-1]]+1
            return AllTags[Tag]
        else:
            AllTags[Tag] = 0
            return 0

FotoAmmount = int(FileLines[0])

AllPhotos = list(map(lambda x: x.split(" "), FileLines[1:(len(FileLines)-1)]))

#print(AllSlides)

ParsedPhotos = list()

for Photo in AllPhotos:
    #print([Slide[x+1] for x in range(int(Slide[1])-1)])
    templ = list()
    # H == 0  V == 1
    templ.append(0)
    templ.append(1 if Photo[0] == "V" else 0)
    #templ.append(int(Photo[1]))
    ParsedPhotos.append(templ+[AddToTag(Photo[x+2]) for x in range(int(Photo[1]))])

print(AllPhotos)
print(AllTags)#Dictionary


print(list(range(len(AllTags))))
ParsedTags = [list() for x in range(len(AllTags))]

for Tag in AllTags:
    #Search all tags
    x = 0
    for Photo in AllPhotos:
        #Search all photos
        if Tag in Photo[2:]:
            #Tag is inside photo
            #AllTags[Tag] is the tag id, in which we want to add
            ParsedTags[AllTags[Tag]].append(x)
        x+=1

print(ParsedPhotos)
print(ParsedTags)
