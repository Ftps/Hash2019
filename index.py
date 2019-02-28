import pickle
import sys
import os
from collections import OrderedDict

if len(sys.argv) == 2:
    Name = sys.argv[1]
else:
    print("Mete como primeiro argumento o nome do ficheiro, sem .txt")
    sys.exit(0)
Parsed_Tags_File = open("Pickles/"+str(Name)+"_ParsedTags",'rb')
ParsedPhotos_File = open("Pickles/"+str(Name)+"_ParsedPhotos",'rb')
ParsedPhotosV_File = open("Pickles/"+str(Name)+"_ParsedPhotosV",'rb')

ParsedTags = pickle.load(Parsed_Tags_File, encoding='bytes')
ParsedPhotos = pickle.load(ParsedPhotos_File, encoding='bytes')
ParsedPhotosV = pickle.load(ParsedPhotosV_File, encoding='bytes')

print(ParsedPhotos)
print(ParsedPhotosV)
print(ParsedTags)
