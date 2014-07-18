#! /usr/bin/python -tt
import sys
sys.setrecursionlimit(10000)
d={}
def knapsack(c,w,p,l):
  if l==0 or c<=0:
    res=0
    d[(c,l)]=res
  else:
    if (c,l) in d:
      res=d[(c,l)]
    else:
      if c<w[l-1]:
        res=knapsack(c,w,p,l-1)
      else:
        res=max(knapsack(c,w,p,l-1),p[l-1]+knapsack(c-w[l-1],w,p,l-1))
      d[(c,l)]=res
  return res

if __name__=="__main__":
  pair=[[int(num) for num in line.split()] for line in open("knapsack_big.txt")]
  c=pair[0][0]
  pair=pair[1:]
  p=[item[0] for item in pair]
  w=[item[1] for item in pair]
  l=len(p)
  print knapsack(c,w,p,l)
