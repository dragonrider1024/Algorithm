#! /usr/bin/python -tt
def knapsack(c,w,p):
  l=len(p)
  A=[[0 for x in range(c+1)] for y in range(l+1)]
  for i in xrange(1,l+1):
    for j in range(c+1):
      if j<w[i-1]:
        A[i][j]=A[i-1][j]
      else:
        A[i][j]=max(A[i-1][j],A[i-1][j-w[i-1]]+p[i-1])
  return A[l][c]
  

if __name__=="__main__":
  pair=[[int(num) for num in line.split()] for line in open("knapsack1.txt")]
  c=pair[0][0]
  pair=pair[1:]
  p=[item[0] for item in pair]
  w=[item[1] for item in pair]
  print knapsack(c,w,p)
