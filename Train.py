#!/usr/bin/env python3

fd  = open("Input", "r")
FileLines = fd.read().split('\n')
print(FileLines)

GeneralInfo = FileLines[0].split(" ")
print(GeneralInfo)

Rows,Columns,Minimum,Maximum = list(map(lambda x: int(x),GeneralInfo))
print([Rows,Columns,Minimum,Maximum])

Pizza = list(map(lambda x: list(x), FileLines[1:(len(FileLines)-1)]))
print(Pizza)
