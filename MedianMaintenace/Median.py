#! /usr/bin/python -tt
import heapq
import sys
class Median:
  def CalMedian(self,array):
    l=len(array)
    hql=[]
    hqr=[]
    ll=0
    lr=0
    summedian=0
    for i in range(l):
      if ll==lr:
        if ll==0:
          self.heappush_max(hql,array[i])
        else:
          if array[i]<hqr[0]:
            self.heappush_max(hql,array[i])
          else:
            self.heappush_min(hqr,array[i])
            item=heapq.heappop(hqr)
            self.heappush_max(hql,item) 
        ll+=1
      else:
        if array[i]>hql[0]:
          self.heappush_min(hqr,array[i])
        else:
          temp=array[i]
          item=heapq._heappushpop_max(hql,temp)
          self.heappush_min(hqr,item)
        lr+=1
#      print hql[0]
      summedian=summedian + hql[0]
#    print summedian  
    return summedian%l  

  def heappush_min(self,hqr,item):
    hqr.append(item)
    heapq._siftdown(hqr,0,len(hqr)-1)
    return
  
  def heappush_max(self,hql,item):
    hql.append(item)
    heapq._siftdown_max(hql,0,len(hql)-1)
    return

if __name__=='__main__':
  filename='Median.txt'
  f=open(filename,'r')
  text=f.read()
  array=[int(num) for num in text.split()]
  s=Median()
  print s.CalMedian(array)

