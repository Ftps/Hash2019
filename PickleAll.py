#!/usr/bin/env python3
import pickle
import sys
import os
from collections import OrderedDict

if not os.path.isdir("Pickles2"):
    os.mkdir("Pickles2")

for Files in os.scandir('Inputs'):
    #print(ParsedPhotos)
    #print(ParsedTags)
    if Files.name[:-4] != "a_example":
        continue
    print(Files.name[:-4])
    Parsed_Tags_File = open("Pickles2/"+Files.name[:-4]+"_ParsedTags",'wb')
    ParsedPhotos_File = open("Pickles2/"+Files.name[:-4]+"_ParsedPhotos",'wb')
    ParsedPhotosV_File = open("Pickles2/"+Files.name[:-4]+"_ParsedPhotosV",'wb')
    ParsedPhotos2_File = open("Pickles2/"+Files.name[:-4]+"_ParsedPhotos2",'wb')
    ParsedPhotosV2_File = open("Pickles2/"+Files.name[:-4]+"_ParsedPhotosV2",'wb')

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
    ParsedPhotos2 = list()
    ParsedPhotosV = list()
    ParsedPhotosV2 = list()

    for Photo in AllPhotos:
        #print([Slide[x+1] for x in range(int(Slide[1])-1)])
        templ = list()
        templv = list()
        # H == 0  V == 1
        templ.append(0)
        templ.append(1 if Photo[0] == "V" else 0)
        templv.append(0)
        templv.append(len(ParsedPhotos))

        if Photo[0] == "V":
            ParsedPhotosV.append(templv+[AddToTag(Photo[x+2]) for x in range(int(Photo[1]))])

            ParsedPhotosV2.append(templv+[{AddToTag(Photo[x+2]) for x in range(int(Photo[1]))}])
        #templ.append(int(Photo[1]))
        ParsedPhotos.append(templ+[AddToTag(Photo[x+2]) for x in range(int(Photo[1]))])

        ParsedPhotos2.append(templ+[{AddToTag(Photo[x+2]) for x in range(int(Photo[1]))}])

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


    pickle.dump(ParsedTags,Parsed_Tags_File)
    Parsed_Tags_File.close()
    pickle.dump(ParsedPhotos,ParsedPhotos_File)
    ParsedPhotos_File.close()
    pickle.dump(ParsedPhotosV,ParsedPhotosV_File)
    ParsedPhotosV_File.close()
    pickle.dump(ParsedPhotos2,ParsedPhotos2_File)
    ParsedPhotos_File.close()
    pickle.dump(ParsedPhotosV2,ParsedPhotosV2_File)
    ParsedPhotosV_File.close()
#    """
    print("All Photos")
    print(AllPhotos)
    print("All Tags")#Dictionary
    print(AllTags)#Dictionary

    Parsed_Tags_File = open("Pickles2/"+Files.name[:-4]+"_ParsedTags",'rb')
    ParsedPhotos_File = open("Pickles2/"+Files.name[:-4]+"_ParsedPhotos",'rb')
    ParsedPhotosV_File = open("Pickles2/"+Files.name[:-4]+"_ParsedPhotosV",'rb')
    ParsedPhotos2_File = open("Pickles2/"+Files.name[:-4]+"_ParsedPhotos2",'rb')
    ParsedPhotosV2_File = open("Pickles2/"+Files.name[:-4]+"_ParsedPhotosV2",'rb')

    ParsedTags = pickle.load(Parsed_Tags_File, encoding='bytes')
    ParsedPhotos = pickle.load(ParsedPhotos_File, encoding='bytes')
    ParsedPhotosV = pickle.load(ParsedPhotosV_File, encoding='bytes')
    ParsedPhotos2 = pickle.load(ParsedPhotos2_File, encoding='bytes')
    ParsedPhotosV2 = pickle.load(ParsedPhotosV2_File, encoding='bytes')

    print("Parsed Photos")
    print(ParsedPhotos)
    print("Parsed Photos 2")
    print(ParsedPhotos2)
    print("Parsed Photos V")
    print(ParsedPhotosV)
    print("Parsed Photos V2")
    print(ParsedPhotosV2)
    print("Parsed Tags")
    print(ParsedTags)

#"""
