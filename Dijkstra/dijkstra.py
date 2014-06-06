import heap
class Solution:
    '''Solution to programming excercise 5'''
#    def dijkstra(self,G):
#	'''naive implementation without heap'''
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
	'''implementation with heap'''
	n=0
	hq=range(1000000) #heap for G-V vertices
	r={} # result hash table
	mapvtoindex={} #map the vertices to hq index for fast search and update
	found={} #boolean to record the vertices whose short pathes are currently found
	hpobj=heap.heap(hq,n)
	for i in xrange(1,201):
	   found[str(i)]=False
	   if i==1:
	      hpobj.heappush(hq,[0,str(i)],mapvtoindex)
	   else:
	      hpobj.heappush(hq,[1000000,str(i)],mapvtoindex)
	while hpobj.length(hq):
	   p=hpobj.heappop(hq,mapvtoindex)
	   v=p[1]
	   r[v]=p[0]
	   found[v]=True
           e_list=G[int(v)-1]
	   for i in xrange(1,len(e_list)):
              w=e_list[i][0]
              if found[w]==False:
	         d=r[v]+e_list[i][1]
	         if d<hq[mapvtoindex[w]][0]:
		    hq[mapvtoindex[w]][0]=d  #relax the path, decrease the key for vertex w
	            hpobj.heapify_up(hq,mapvtoindex[w],mapvtoindex) #heapify vertex w locally
	return r
	
