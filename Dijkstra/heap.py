class heap:
    '''heap data structure and its operation'''

    def __init__(self,hq,n):
        self.hq=hq
        self.n=n

    def heappush(self,hq,item,mapvtoindex):
	hq[self.n]=item
	mapvtoindex[item[1]]=self.n
	self.heapify_up(hq,self.n,mapvtoindex)
	self.n=self.n+1
	return

    def length(self,hq):
	return self.n

    def heapify_up(self,hq,pos,mapvtoindex):
	item=hq[pos]
	while pos>=0:
	   parentpos=(pos-1)>>1
	   parent=hq[parentpos]
	   if item<parent:
	      hq[pos]=parent
	      mapvtoindex[parent[1]]=pos
	      pos=parentpos
	      continue
	   break
	hq[pos]=item
	mapvtoindex[item[1]]=pos
	return
	
    def heappop(self,hq,mapvtoindex):
	item=hq[0]
	hq[0]=hq[self.n-1]	
	mapvtoindex[hq[self.n-1][1]]=0
	self.n=self.n-1
	self.heapify_down(hq,0,mapvtoindex)
	return item

    def heapify_down(self,hq,pos,mapvtoindex):
	item=hq[pos]
	while 2*pos+2<self.n:
	   lchild=2*pos+1
	   rchild=2*pos+2
	   if item>hq[lchild] or item>hq[rchild]:
	      if hq[lchild]<hq[rchild]:
	         hq[pos]=hq[lchild]
	         mapvtoindex[hq[lchild][1]]=pos
	         pos=lchild
	      else:
	         hq[pos]=hq[rchild]
	         hq[pos]=hq[rchild]
	         mapvtoindex[hq[rchild][1]]=pos
	         pos=rchild
	      continue
           break 
	hq[pos]=item
	mapvtoindex[item[1]]=pos
	return	
