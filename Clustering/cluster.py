#! /usr/bin/python -tt
import UnionFind
def kcluster(E,k,n):
  u=UnionFind.UnionFind()
  E=sorted(E,key=edgeweight)
  l=len(E)
  for i in range(l):
    w=E[i]
    if u[w[0]]!=u[w[1]]:
      if n==k:
        return w[2]
      u.union(w[0],w[1])
      n=n-1
    else:
      continue
  

def edgeweight(w):
  return w[-1]


if __name__=="__main__":
  E=[line.split() for line in open("clustering.txt")]
  n=int(E[0][0])
  E=E[1:]
  for w in E:
    w[-1]=int(w[-1])
  k=4
  print kcluster(E,k,n)
