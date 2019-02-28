#!/usr/bin/env python3
import pickle
import sys
import os
from collections import OrderedDict

if not os.path.isdir("Pickles"):
    os.mkdir("Pickles")

for Files in os.scandir('Inputs'):
    #print(ParsedPhotos)
    #print(ParsedTags)
    if Files.name != "a_example.txt":
        continue
    print(Files.name[:-4])
    Parsed_Tags_File = open("Pickles/"+Files.name[:-4]+"_ParsedTags",'wb')
    ParsedPhotos_File = open("Pickles/"+Files.name[:-4]+"_ParsedPhotos",'wb')
    ParsedPhotosV_File = open("Pickles/"+Files.name[:-4]+"_ParsedPhotosV",'wb')

    fd = open("Inputs/"+Files.name, "r")

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
    ParsedPhotosV = list()

    for Photo in AllPhotos:
        #print([Slide[x+1] for x in range(int(Slide[1])-1)])
        templ = list()
        # H == 0  V == 1
        templ.append(0)
        templ.append(1 if Photo[0] == "V" else 0)
        if Photo[0] == "V":
            ParsedPhotosV.append(templ+[AddToTag(Photo[x+2]) for x in range(int(Photo[1]))])
        #templ.append(int(Photo[1]))
        ParsedPhotos.append(templ+[AddToTag(Photo[x+2]) for x in range(int(Photo[1]))])

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


    print(AllPhotos)
    print(AllTags)#Dictionary

    pickle.dump(ParsedTags,Parsed_Tags_File)
    Parsed_Tags_File.close()
    pickle.dump(ParsedPhotos,ParsedPhotos_File)
    ParsedPhotos_File.close()
    pickle.dump(ParsedPhotosV,ParsedPhotosV_File)
    ParsedPhotosV_File.close()

    Parsed_Tags_File = open("Pickles/"+Files.name[:-4]+"_ParsedTags",'rb')
    ParsedPhotos_File = open("Pickles/"+Files.name[:-4]+"_ParsedPhotos",'rb')
    ParsedPhotosV_File = open("Pickles/"+Files.name[:-4]+"_ParsedPhotosV",'rb')

    ParsedTags = pickle.load(Parsed_Tags_File, encoding='bytes')
    ParsedPhotos = pickle.load(ParsedPhotos_File, encoding='bytes')
    ParsedPhotosV = pickle.load(ParsedPhotosV_File, encoding='bytes')
    print(ParsedPhotos)
    print(ParsedPhotosV)
    print(ParsedTags)


    sys.exit(0)
