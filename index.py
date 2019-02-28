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
    if Tag in Dic.keys():
        return Dic[Tag]
    else:
        if len(Dic.keys()):
            Dic[Tag] = Dic[Dic.keys()[-1]]+1
        else:
            Dic[Tag] = 0

FotoAmmount = int(FileLines[0])

AllSlides = list(map(lambda x: x.split(" "), FileLines[1:(len(FileLines)-1)]))

print(AllSlides)

ParsedSlides = list()
for Slide in AllSlides:
    #print([Slide[x+1] for x in range(int(Slide[1])-1)])
    templ = list(Slide[0])
    templ.append(Slide[1])
    ParsedSlides.append(templ+[(Slide[x+2]) for x in range(int(Slide[1]))])
    print(AllSlides)

slides = [1, 2, [3,4], 5, [6,7]]

f = open("sadsd", "w")

f.write('{}\n'.format(len(slides)))

for i in slides:
	try:
		f.write('{} {}\n'.format(i[0], i[1]))
	except:
		#Int
		f.write('{}\n'.format(i))
print(ParsedSlides)
