#! /usr/bin/python -tt
import UnionFind
from itertools import combinations
def kcluster(E,n,nbit):
  u=UnionFind.UnionFind()
  pos1=list(combinations(range(nbit),1))
  print pos1
  pos2=list(combinations(range(nbit),2))
  print pos2
  l=len(E)
  s=set()
  for i in range(l):
    s.add(E[i])
  n=len(s)
  for i in range(l):
    for pos in pos1:
      c=ord('1')^ord(E[i][pos[0]])
      etemp=E[i][:pos[0]]+str(c)+E[i][pos[0]+1:]
      if etemp in s and u[E[i]]!=u[etemp]:
        u.union(etemp,E[i])
        n=n-1
    for pos in pos2:
      c0=ord('1')^ord(E[i][pos[0]])
      c1=ord('1')^ord(E[i][pos[1]])
      etemp=E[i][:pos[0]]+str(c0)+E[i][pos[0]+1:pos[1]]+str(c1)+E[i][pos[1]+1:]
      if etemp in s and u[E[i]]!=u[etemp]:
        u.union(etemp,E[i])
        n=n-1
  return n

if __name__=="__main__":
  E=[line.split() for line in open("clustering_big.txt")]
  n=int(E[0][0])
  nbit=int(E[0][1])
  E=E[1:]
  E=[''.join(line) for line in E]
  print kcluster(E,n,nbit)
