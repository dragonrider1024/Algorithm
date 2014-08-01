#! /bin/python -tt
def build_in(E_list):
  G_in={}
#  G_out={}
  for e in E_list:
    v=e[0]
    u=e[1]
    w=e[2]
    if u not in G_in:
      G_in[u]=[(v,w)]
    else:
      G_in[u]+=[(v,w)]
#    if v not in G:
#      G_out[v]=[(u,w)]
#    else:
#      G_out[v]+=[(u,w)]
#  return (G_in,G_out)
  return G_in

def build_out(E_list):
  G_out={}
  for e in E_list:
    v=e[0]
    u=e[1]
    w=e[2]
    if not v==0:
      if v not in G_out:
        G_out[v]=[(u,w)]
      else:
        G_out[v]+=[(u,w)]
  return G_out
