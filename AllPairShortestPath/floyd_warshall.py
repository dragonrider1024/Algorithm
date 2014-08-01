#! /usr/bin/python -tt
def floydwarshall(G,n):
  A=[[[0 for x in range(0,n+1)] for y in range(0,n+1)] for z in range(0,n+1)]
  for x in xrange(1,n+1):
    for y in xrange(1,n+1):
      e=(x,y)
      if e not in G:
        A[x][y][1]=1000000
      else:
        A[x][y][1]=G[e]
  for k in xrange(2,n):
    for x in xrange(1,n+1):
      for y in xrange(1,n+1):
        A[x][y][k]=min(A[x][y][k-1],A[x][k][k-1]+A[k][y][k-1])
  d=[[0 for x in range(n+1)] for y in range(n+1)]
  for x in xrange(1,n+1):
    if A[x][x][n-1]<0:
      print "Got Negative Cycle"
      return None
  dmin=1000000
  for x in xrange(1,n+1):
    for y in xrange(1,n+1):
      d[x][y]=A[x][y][n-1]
      dmin=min(dmin,d[x][y])
  return dmin


if __name__=="__main__":
  G_list=[[int(num) for num in line.split()] for line in open("g1.txt")]
  n=G_list[0][0]
  m=G_list[0][1]
  G_list=G_list[1:]
#  print n,m
#  print G
  G={}
  for e in G_list:
    if (e[0],e[1]) not in G:
      G[(e[0],e[1])]=e[2]
  print G
  dmin=floydwarshall(G,n)
  print dmin
