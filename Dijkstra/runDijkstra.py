#! /usr/bin/python
lines=[line.strip() for line in open('dijkstraData.txt')]
#print lines
G=[line.split() for line in lines]
for v in G:
   for i in range(len(v)):
	if i!=0:
	   pair=v[i].split(",")
           v[i]=(pair[0],int(pair[1]))
#print G
import dijkstra
r={}
s=dijkstra.Solution()
r=s.dijkstra(G)
print r['7'],r['37'],r['59'],r['82'],r['99'],r['115'],r['133'],r['165'],r['188'],r['197']
