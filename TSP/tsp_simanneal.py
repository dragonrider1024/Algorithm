#! /usr/bin/python
from math import sqrt, exp
from random import randint, random
class Solution:
  def tsp_simanneal(self,G):
    n=len(G)
    T0=1000000 #initial temperature
    T=T0
    ncycle=2000000
    i=0
    while i<ncycle:
      index1=randint(0,n-1)
      index2=randint(0,n-1)
  #    print index1,index2
  #    print G
      cost1=self.path_length(G)
      #swap G[index1] and G[index2]
      temp=G[index1][:]
      G[index1]=G[index2][:]
      G[index2]=temp
      cost2=self.path_length(G)
  #    print G
      if cost2<cost1:
        print cost2, T
      else:
        r=random()
        if r<exp(-(cost2-cost1)/T):
          print cost2, T
        else:
          temp=G[index1][:]
          G[index1]=G[index2][:]
          G[index2]=temp
      T=T*0.99999
      i=i+1
    return cost1
    

  def path_length(self,G):
    n=len(G)
    l=0
    for i in range(1,n):
      l+=sqrt((G[i][0]-G[i-1][0])**2+(G[i][1]-G[i-1][1])**2)
    l+=sqrt((G[0][0]-G[n-1][0])**2+(G[0][1]-G[n-1][1])**2)
    return l

if __name__=="__main__":
  G=[line.split() for line in open("tsp.txt")]
  G=G[1:]
  G=[[float(num) for num in item] for item in G]
  s=Solution()
  print s.tsp_simanneal(G)
