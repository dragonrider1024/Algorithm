#! /usr/bin/python -tt
from itertools import combinations
from math import sqrt
class Solution:
  ''' Dynamic programming for Traveling Salesman Probblem'''
  def tsp(self,G):
    n=len(G)
    locations=range(1,n+1)
    A={}
    #initialization
    A[((1,),1)]=0
    for m in range(1,n):
      for item in combinations(locations[1:],m):
        tempitem=(1,)+item
        A[(tempitem,1)]=100000000 # 100000000 is infinity
    for m in range(1,n):
      for item in combinations(locations[1:],m):
        tempitem=(1,)+item
        for j in item:
          A[(tempitem,j)]=100000000
          templist=list(tempitem)
          templist.remove(j)
          temptuple=tuple(templist)
          for k in tempitem:
            if k!=j:
              C_kj=sqrt((G[k-1][0]-G[j-1][0])**2+(G[k-1][1]-G[j-1][1])**2)
              A[(tempitem,j)]=min(A[(tempitem,j)],A[(temptuple,k)]+C_kj)
          print 'A[',tempitem,',',j,']',A[(tempitem,j)]
    res=100000000
    S=tuple(locations)
    for j in range(2,n+1):
      C_j1=sqrt((G[j-1][0]-G[0][0])**2+(G[j-1][1]-G[0][1])**2)
      res=min(res,A[(S,j)]+C_j1)
    return res


if __name__=="__main__":
  G=[line.split() for line in open("tsp.txt")]
  G=G[1:]
  G=[[float(num) for num in item] for item in G]
  s=Solution()
  #print s.tsp(G[:9])
  #print s.tsp(G[9:])
  #C_812=sqrt((G[8-1][0]-G[12-1][0])**2+(G[8-1][1]-G[12-1][1])**2)
  #C_89=sqrt((G[8-1][0]-G[9-1][0])**2+(G[8-1][1]-G[9-1][1])**2)
  C_1213=sqrt((G[12-1][0]-G[13-1][0])**2+(G[12-1][1]-G[13-1][1])**2)
  #C_913=sqrt((G[9-1][0]-G[13-1][0])**2+(G[9-1][1]-G[13-1][1])**2)
  #print s.tsp(G[:9])+s.tsp(G[9:])-C_89-C_1213+C_812+C_913
  #print s.tsp(G)
  print s.tsp(G[:13])+s.tsp(G[11:])-2*C_1213
