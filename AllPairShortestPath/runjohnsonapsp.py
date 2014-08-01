#! /usr/bin/python
from build_adjacency_list import build_in, build_out
from bellman_ford import bellmanford
from dijkstra import dijkstra
E_list=[[int(num) for num in line.split()] for line in open("g2.txt")]
n=E_list[0][0]
m=E_list[0][1]
E_list=E_list[1:]
#add a source vertex s
for i in range(n):
  E_list+=[[0,i+1,0]]
#build a in degree graph G
G_in=build_in(E_list)
#call bellman-ford
pv=bellmanford(G_in,n+1)
if pv:
  #modify edge cost
  for e in E_list:
    e[2]+=pv[e[0]]-pv[e[1]]
  G_out=build_out(E_list)
  print G_out
  # d[x][y] store the shortest path from x to y
  d=[[0 for x in range(n+1)] for y in range(n+1)]
  # run dijkstra algorithm
  for i in xrange(1,n+1):
    print "...........source vertex",i,"started..............."
    r=dijkstra(G_out,n,i)
    print "...........source vertext", i, "finished......"
    for j in xrange(1,n+1):
      d[i][j]=r[j]-pv[i]+pv[j]
  print d
  dmin=1000000
  for i in xrange(1,n+1):
    for j in xrange(1,n+1):
      dmin=min(dmin,d[i][j])
  print dmin
