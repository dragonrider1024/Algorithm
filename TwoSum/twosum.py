#! /usr/bin/python -tt
class Solution:
  def twosum(self,array):
    numdict={}
    l=len(array)
    for i in range(l):
      if array[i] in numdict:
        numdict[array[i]].append(i)
      else:
        numdict[array[i]]=[i]
    return numdict

if __name__=='__main__':
  import sys
  args=sys.argv[1:]
  if not len(args)==1:
    print 'wrong usage of two sum, correct usage is ./twosum.py filename'
    sys.exit(1)
  f=open(args[0],'r')
  text=f.read()
  array=[int(num) for num in text.split()]
  s=Solution()
  numdict=s.twosum(array)
  for key in numdict.keys():
    print key, '-->', numdict[key]
  count=0
  for t in xrange(-10000,10001):
    found=False
    for key in numdict.keys():
      second = t - key
      if second in numdict:
        if not second == key:
          found=True
          print t,'=',key,'+',second,
          break
        else:
          if len(numdict[key]) > 2:
            print t,'=',key,'+',second,
            found=True
            break
    if found:
      count+=1 
      print '  ',count
  print count
