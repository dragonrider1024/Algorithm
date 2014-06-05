class Solution:
    def count_and_sort(self,A,i,j):
	l=j-i
        if l<=1:
	   return 0
	m=self.partition(A,i,j)
	count_l=self.count_and_sort(A,i,m)
	count_r=self.count_and_sort(A,m+1,j)
	count=count_l+count_r+(j-i-1)
	return count


    def partition(self,A,i,j):
	median_index=self.get_median_index(A,i,j)
	(A[i],A[median_index])=(A[median_index],A[i])
#	(A[i],A[j-1])=(A[j-1],A[i])
	k=i+1
	t=i+1
	for k in xrange(i+1,j):
	   if A[k]<A[i]:
	      (A[k],A[t])=(A[t],A[k])
              t=t+1
	(A[i],A[t-1])=(A[t-1],A[i])
	return t-1


    def get_median_index(self,A,i,j):
	middle=(i+j-1)/2
	mini=min(A[i],A[j-1],A[middle])
	maxi=max(A[i],A[j-1],A[middle])
	if A[i]!=mini and A[i]!=maxi:
	   return i
	elif A[j-1]!=mini and A[j-1]!=maxi:
	   return j-1
	else:
	   return middle
