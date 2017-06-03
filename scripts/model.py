import math
import matplotlib.pyplot as plt

def cubic_root(x):
  return x**(1.0/3)

# returns (t2-t1)/t1, where t1 is the sequential time ("read slices, write slices")
# and t2 is the "random time" (read blocks, write blocks)
#
# F: file size in bytes. Also file size in voxels. Typical value: 10**9 bytes (1 GB).
# N: number of blocks and number of slices. Must be lower than F**(1/3). Typical value: 100.
# alpha_r: data read rate. Typical value: 100 MB/s
# alpha_w: data write rate. Typical value: 100 MB/s (?)
# beta: disk access time. Typical value: 5 ms
# m: amount of available memory, in bytes
# b: number of bytes per voxel

def t_slices(N,F,alpha_r,alpha_w,beta,b):
  return b*F/alpha_r+b*F/alpha_w+2*beta*N

def t_buff_slices(N,F,alpha_r,alpha_w,beta,m,b):
  return b*F/alpha_r+b*F/alpha_w+beta*(N+math.ceil(b*F/m))

def t_blocks(N,F,alpha_r,alpha_w,beta,b):
    return F*b/alpha_r+F*b/alpha_w+beta*N*(1+cubic_root(F/N))

def t_multiple_reads(N,F,alpha_r,alpha_w,beta,m,b):
    return F*b/alpha_r+F*b/alpha_w+beta*math.ceil(F*b/m)*(1+math.ceil(m*N/(F*b)))

def t_cluster_reads(N,F,alpha_r,alpha_w,beta,m,b):
    a = m/(b*F)*cubic_root(N)
    return b*F/alpha_r+b*F/alpha_w+beta*(N+math.ceil(F*b/m)*(cubic_root(F/N)*(math.ceil(a)-math.floor(a))+1))
  
N=125.0
b=2.0
F=76000000000.0/b
alpha_w=68*1024*1024 #109506075.558291 # according to benchmark on May 31st
alpha_r=alpha_w
alpha_w=1000000000000000000000000000000000000
beta=15*10**(-3)
m=F/125.0 
print "Slices",t_slices(N,F,alpha_r,alpha_w,beta,b)
print "Buffered slices",t_buff_slices(N,F,alpha_r,alpha_w,beta,m,b)
print "Blocks",t_blocks(N,F,alpha_r,alpha_w,beta,b)
print "Multiple reads",t_multiple_reads(N,F,alpha_r,alpha_w,beta,m,b)
print "Cluster reads",t_cluster_reads(N,F,alpha_r,alpha_w,beta,m,b)

mem_values=[b*F/125,b*F/64,b*F/32,b*F/16,b*F/4,b*F/2,b*F]
cluster_read_values=[]
multiple_read_values=[]
slice_values=[]
buff_slice_values=[]
block_values=[]
for mem in mem_values:
  cluster_read_values.append(t_cluster_reads(N,F,alpha_r,alpha_w,beta,mem,b))
  multiple_read_values.append(t_multiple_reads(N,F,alpha_r,alpha_w,beta,mem,b))
  slice_values.append(t_slices(N,F,alpha_r,alpha_w,beta,b))
  block_values.append(t_blocks(N,F,alpha_r,alpha_w,beta,b))
  buff_slice_values.append(t_buff_slices(N,F,alpha_r,alpha_w,beta,mem,b))

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.set_xlabel("Available Memory (B)")
ax.set_ylabel("Time (s)")
ax.plot(mem_values,cluster_read_values,color='k',label="Cluster reads")
ax.plot(mem_values,multiple_read_values,color='g',label="Multiple reads")
ax.plot(mem_values,slice_values,color='r',label="Slices")
ax.plot(mem_values,block_values,color='b',label="Blocks")
ax.plot(mem_values,buff_slice_values,color='r',label="Buffered slices")
ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
plt.show()


