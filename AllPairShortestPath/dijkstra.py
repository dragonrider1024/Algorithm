#! /usr/bin/python
import heap
def dijkstra(G,n,s):
  '''implementation with heap'''
  l=0
  hq=range(1000000) #heap for G-V vertices
  r={} # result hash table
  mapvtoindex={} #map the vertices to hq index for fast search and update
  found={} #boolean to record the vertices whose short pathes are currently found
  hpobj=heap.heap(hq,l)
  for i in xrange(1,n+1):
    found[i]=False
    if i==s:
      hpobj.heappush(hq,[0,s],mapvtoindex)
    else:
      hpobj.heappush(hq,[1000000,i],mapvtoindex)
  while hpobj.length(hq):
    p=hpobj.heappop(hq,mapvtoindex)
    v=p[1]
    r[v]=p[0]
    found[v]=True
    e_list=G[v]
    for i in xrange(len(e_list)):
      w=e_list[i][0]
      if found[w]==False:
        d=r[v]+e_list[i][1]
        if d<hq[mapvtoindex[w]][0]:
          hq[mapvtoindex[w]][0]=d  #relax the path, decrease the key for vertex w
          hpobj.heapify_up(hq,mapvtoindex[w],mapvtoindex) #heapify vertex w locally
  return r
