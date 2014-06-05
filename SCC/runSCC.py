#! /usr/bin/python
lines=[line.strip() for line in open('SCC.txt')]
E_list=[line.split() for line in lines]
print E_list
V_list=[]
for i in xrange(1,875715):
    V_list+=[str(i)]
print V_list
G={}
Grev={}
for e in E_list:
#   if e[0] not in V_list:
#      V_list+=[e[0]]
#   if e[1] not in V_list:
#      V_list+=[e[1]]
   if G.has_key(e[0]):
      G[e[0]]=G[e[0]]+[e[1]]
   else:
      G[e[0]]=[e[1]]
   if Grev.has_key(e[1]):
      Grev[e[1]]=Grev[e[1]]+[e[0]]
   else:
      Grev[e[1]]=[e[0]]
#print V_list
print G
print Grev
import scc
import sys
sys.setrecursionlimit(100000) #increase the maximum recursion depth
s=scc.Solution()
print s.scc(G,Grev,V_list)
