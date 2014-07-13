#! /usr/bin/python -tt
def prim(G):
  mst=0
  S={'1'}
  l=len(G)
  for i in range(l-1):
    mini=100000000
    t=''
    for v in S:
      for e in G[v]:
        if e[1]<mini and e[0] not in S:
          mini=e[1]
          t=e[0]
    S.add(t)
    mst+=mini
  return mst 
  

if __name__=="__main__":
  sG=[line.strip() for line in open("Prim.txt")]
  Glist=[line.split() for line in sG]
  Glist=Glist[1:]
  G={}
  l=len(Glist)
  for i in range(l):
    Glist[i][2]=int(Glist[i][2])
#  print Glist
  for e in Glist:
    if e[0] not in G:
      G[e[0]]=[(e[1],e[2])]
    else:
      G[e[0]]+=[(e[1],e[2])]
    if e[1] not in G:
      G[e[1]]=[(e[0],e[2])]
    else:
      G[e[1]]+=[(e[0],e[2])]
  print G
  print prim(G)
