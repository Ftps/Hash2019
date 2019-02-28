#!/usr/bin/env python3

fd  = open("Input", "r")
FileLines = fd.read().split('\n')
print(FileLines)

FotoAmmount = int(FileLines[0])

AllSlides = list(map(lambda x: x.split(" "), FileLines[1:(len(FileLines)-1)]))

print(AllSlides)
