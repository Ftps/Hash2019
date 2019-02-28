#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
	fd = open(sys.argv[1], "r")
	FileLines = fd.read().split('\n')
	print(FileLines)

	FotoAmmount = int(FileLines[0])

	AllSlides = list(map(lambda x: x.split(" "), FileLines[1:(len(FileLines)-1)]))

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
