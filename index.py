#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
	fd = open(sys.argv[1], "r")
	FileLines = fd.read().split('\n')
	print(FileLines)

	FotoAmmount = int(FileLines[0])

	AllSlides = list(map(lambda x: x.split(" "), FileLines[1:(len(FileLines)-1)]))

	print(AllSlides)
