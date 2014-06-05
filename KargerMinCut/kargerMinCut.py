import random
import math
import copy
class Solution:
   def kargerMinCut(self,G):
       Gp=copy.deepcopy(G)
       V=len(G)
       N=V*V*math.log(V)
       Emin=1000000
       i=0
       while i<N:
          Gp=copy.deepcopy(G)
          E=self.kargerMinCut_trial(Gp)
          Emin=min(Emin,E)
	  print i, Emin
	  i=i+1
       return Emin

   def kargerMinCut_trial(self,G):
       V=len(G)
       while V>2:
	  (V,E)=self.contraction(G)
#	  print (V,E)
       return E
       

   def contraction(self,G):
       V=len(G)
       E=0
       for i in range(V):
          E=E+len(G[i])-1
       E=E/2
# pick a edge at random
       t=random.randint(1,2*E)
       i=0
       while t>(len(G[i])-1):
	   t=t-len(G[i])+1
           i=i+1
# endpoints of the edge
       Vi=G[i][0]
       Vj=G[i][t]
# merge the two end points
       for x in range(V):
	   for j in xrange(1,len(G[x])):
	       if G[x][0]!=Vi and G[x][0]!=Vj:
                  if G[x][j]==Vj:
		      G[x][j]=Vi
# remove that edge and any loops
       while Vj in G[i]:
           G[i].remove(Vj)
       for k in range(V):
           if G[k][0]==Vj:
	       break
       while Vi in G[k]:
           G[k].remove(Vi)
       del G[k][0]
       G[i]=G[i]+G[k]
       del G[k]
       V=len(G)
       E=0
       for i in range(V):
          E=E+len(G[i])-1
       E=E/2
       return (V,E)
       
