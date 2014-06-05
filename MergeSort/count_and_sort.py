class Solution:
   """ Count number of inversions in a given array
   using divide and conqur"""
   def count_and_sort(self,array):
       infinity=10000000
       l=len(array)
       if l==1:
          return 0
       a_l=array[0:l/2]
       a_r=array[l/2:l]
       count_l=self.count_and_sort(a_l)
       count_r=self.count_and_sort(a_r)
       count=count_l+count_r
       a_l=a_l+[infinity]
       a_r=a_r+[infinity]
       i=0
       j=0
       for k in range(l):
          if a_l[i]<a_r[j]:
             array[k]=a_l[i]
             i=i+1
          else:
             array[k]=a_r[j]
             j=j+1
             count=count+(l/2-i)
       return count
