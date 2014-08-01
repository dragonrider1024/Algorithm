#! /usr/bin/python
def bellmanford(G_in,n):
  d=[[0 for x in range(n)] for y in range(n)]
  d[0][0]=0
  for v in xrange(1,n):
    d[0][v]=1000000
  for i in xrange(1,n):
    for v in range(n):
      d[i][v]=d[i-1][v]
      if v in G_in:
        for u in G_in[v]:
          d[i][v]=min(d[i][v],d[i-1][u[0]]+u[1])
  for v in range(n):
    if v in G_in:
      for u in G_in[v]:
        if d[n-1][u[0]]+u[1]<d[n-1][v]:
          print "Negative Cycle Detected"
          return
  sp=[]
  for i in range(n):
    sp+=[d[n-1][i]]
  return sp
