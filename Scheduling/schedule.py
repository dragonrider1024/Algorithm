#! /usr/bin/python -tt
def schedule(jobs):
  l=len(jobs)
  jobs=sorted(jobs,key=wtvslen,reverse=True)
#  print jobs
  wct=0
  ct=0
  for i in range(l):
    ct+=jobs[i][1]
    wct+=ct*jobs[i][0]
  return wct

def wtvslen(jobid):
  return (jobid[0]-jobid[1],jobid[0])    #the non-optimal greedy algorithm

#def wtvslen(jobid):
#  return 1.0*jobid[0]/jobid[1]   #the optimal greedy algorithm


if __name__=="__main__":
  sjobs=[line.strip() for line in open("Scheduling.txt")]
  jobs=[[int(num) for num in line.split()] for line in sjobs]
  jobs=jobs[1:]
#  print jobs
  print schedule(jobs)

