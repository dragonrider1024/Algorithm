import heapq
class Solution:
    '''Solution to programming excercise 5'''
#    def dijkstra(self,G):
#	'''naive implementation'''
#	q=[]
#	r={}
#	found={}
#        for i in xrange(1,201):
#	   if i==1:
#	      q+=[[0,str(1)]]
#	   else:
#	      q+=[[1000000,str(i)]]
#	   found[str(i)]=False
#	print q
#	while q:
#	   minindex=q.index(min(q))
#	   print minindex
#	   mapvtoi={}
#	   for i in range(len(q)):
#              mapvtoi[q[i][1]]=i
#	   print mapvtoi
#	   sl=q[minindex][0]
#           v=q[minindex][1]
#	   print v
#	   found[v]=True
#	   r[v]=sl
#           e_list=G[int(v)-1]
#	   for i in xrange(1,len(e_list)):
#	      w=e_list[i][0]
#              if found[w]==False:
#		 d=sl+e_list[i][1]
#	         if d<q[mapvtoi[w]][0]:
#	            q[mapvtoi[w]][0]=d
#	   del q[minindex] 
#	return r


    def dijkstra(self,G):

