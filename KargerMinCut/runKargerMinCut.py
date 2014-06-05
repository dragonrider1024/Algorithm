#! /usr/bin/python
lines=[line.strip() for line in open('kargerMinCut.txt')]
G=[[int(num) for num in line.split()] for line in lines]
print G
import kargerMinCut
s=kargerMinCut.Solution()
print s.kargerMinCut(G)
