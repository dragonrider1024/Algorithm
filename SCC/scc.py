class Solution:
    '''solution to programming excercie 4'''
    n=1
    def scc(self,G,Grev,V_list):
	'''compute the size of the five largest strongly
		connected components,input is a graph dictionary'''
	# run dfs on Grev to get finishing time
	nscc=[]
	ftime=self.dfs(Grev,V_list,nscc) # finish time of dfs on reverse graph of G
#	print ftime
	V_list=sorted(ftime,key=ftime.get)
	V_list.reverse()
	self.n=1
	nscc=[]
	self.dfs(G,V_list,nscc)
#	print nscc
	nscc.sort(reverse=True)
	return nscc

    def dfs(self,G,V_list,nscc):
	f={}
	visited={}
	i=0
	for v in V_list:
	    if not visited.has_key(v):
	      n=len(visited)
              self.dfs_visit(G,v,visited,f)           
	      nscc+=[len(visited)-n]
	return f

    def dfs_visit(self,G,v,visited,f):
	visited[v]=True
	if v not in G:
	    f[v]=self.n
	    self.n=self.n+1
	    return 
	for w in G[v]:
	   if not visited.has_key(w):
	      self.dfs_visit(G,w,visited,f)
	f[v]=self.n
	self.n=self.n+1
