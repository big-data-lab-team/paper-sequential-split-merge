#!/usr/bin/env python

import math
import matplotlib.pyplot as plt

def cubic_root(x):
  return x**(1.0/3)


# Seek function, typically a step function
def sigma(distance,beta):
  return beta
  if distance > 10**9:
    return beta # 50ms, on HDD
  else:
    return beta/4.0 # 7ms - consistent with fastest seek time in
  # https://en.wikipedia.org/wiki/Hard_disk_drive_performance_characteristics#SEEKTIME

# See notations in paper, section II.A
  
def t_slices(b,R,alpha_r,alpha_w,beta,n):
  read_time = b*R/alpha_r + beta*n
  write_time = +b*R/alpha_w+beta*n
  seek_time = 0
  total_time = read_time + write_time + seek_time
  return (read_time,write_time,seek_time,total_time)

#def t_buff_slices(N,F,alpha_r,alpha_w,beta,m,b):
#  return b*F/alpha_r+b*F/alpha_w+beta*(N+math.ceil(b*F/m))

def t_blocks(b,R,alpha_r,alpha_w,beta,n):
    d = cubic_root(R/n)
    D = cubic_root(R)
    read_time = R*b/alpha_r + beta*n
    write_time = R*b/alpha_w + beta*n
    seek_time_block = n*(sigma(b*R/2,beta))
    seek_time_rows = n*(d*(d-1)*sigma(b*(D-d),beta))
    seek_time_slices = n*(d*sigma(b*(D**2-d**2),beta))
    total_time = read_time + write_time + seek_time_block+seek_time_rows+seek_time_slices
    return (read_time,write_time,seek_time_block,seek_time_rows,seek_time_slices,total_time)
    

def t_sorted_blocks(b,R,alpha_r,alpha_w,beta,n):
    (read,write,seek,total) = t_blocks(b,R,alpha_r,alpha_w,beta,n)
    write_ = write
    seek_ = seek - n*sigma(R,beta)
    total_ = read+write_+seek_
    return (read,write-beta*n,seek_,total_)
  
#def t_multiple_reads(N,F,alpha_r,alpha_w,beta,m,b):
#    return F*b/alpha_r+F*b/alpha_w+beta*math.ceil(F*b/m)*(1+math.ceil(m*N/(F*b)))

#def t_cluster_reads(N,F,alpha_r,alpha_w,beta,m,b):
#    a = m/(b*F)*cubic_root(N)
#    return b*F/alpha_r+b*F/alpha_w+beta*(N+math.ceil(F*b/m)*(cubic_root(F/N)*(math.ceil(a)-math.floor(a))+1))
  
n=125.0
b=2.0
R=76000000000.0/b
alpha_w=109506075.558291 # according to benchmark on May 31st
alpha_r=alpha_w#100000000000000000000000 # caching
beta=1.23*10**(-5)

#2.72**10**(-6) # SSD laptop

#0.045 # on HDD

#4*10**(-4) # on SSD

m=R/125.0 
print "Slices:",t_slices(b,R,alpha_r,alpha_w,beta,n)
#print "Buffered slices",t_buff_slices(N,F,alpha_r,alpha_w,beta,m,b)
print "Blocks:",t_blocks(b,R,alpha_r,alpha_w,beta,n)
#print "Sorted Blocks:",t_sorted_blocks(b,R,alpha_r,alpha_w,beta,n)
#print "Multiple reads",t_multiple_reads(N,F,alpha_r,alpha_w,beta,m,b)
#print "Cluster reads",t_cluster_reads(N,F,alpha_r,alpha_w,beta,m,b)


# mem_values=[b*F/125,b*F/64,b*F/32,b*F/16,b*F/4,b*F/2,b*F]
# cluster_read_values=[]
# multiple_read_values=[]
# slice_values=[]
# buff_slice_values=[]
# block_values=[]
# for mem in mem_values:
#   cluster_read_values.append(t_cluster_reads(N,F,alpha_r,alpha_w,beta,mem,b))
#   multiple_read_values.append(t_multiple_reads(N,F,alpha_r,alpha_w,beta,mem,b))
#   slice_values.append(t_slices(N,F,alpha_r,alpha_w,beta,b))
#   block_values.append(t_blocks(N,F,alpha_r,alpha_w,beta,b))
#   buff_slice_values.append(t_buff_slices(N,F,alpha_r,alpha_w,beta,mem,b))

# fig=plt.figure()
# ax=fig.add_subplot(1,1,1)
# ax.set_xlabel("Available Memory (B)")
# ax.set_ylabel("Time (s)")
# ax.plot(mem_values,cluster_read_values,color='k',label="Cluster reads")
# ax.plot(mem_values,multiple_read_values,color='g',label="Multiple reads")
# ax.plot(mem_values,slice_values,color='r',label="Slices")
# ax.plot(mem_values,block_values,color='b',label="Blocks")
# ax.plot(mem_values,buff_slice_values,color='r',label="Buffered slices")
# ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
#            ncol=2, mode="expand", borderaxespad=0.)
# plt.show()


