#!/usr/bin/env python

import math
from decimal import Decimal as dec

def cubic_root(x):
  return x**(1.0/3)

# See notations in paper, section II.A
  
def t_slices(b,R,n):
  return 2*n

def t_buff_slices(b,R,n,m):
  return n+math.ceil(b*R/m)

def t_blocks(b,R,n):
    d = cubic_root(R/n)
    return n+n*d**2
    
def t_cluster_reads(b,R,n,m):
    a=(m*n)/(R*b)
    nu = cubic_root(n)
    d = cubic_root(R/n)
    if a < nu: # case 1
      m_prime = (R*b)/(n)*math.floor(a)
     # print "R=",R
    #  print "b=",b
   #   print "n=",n
  #    print "m_prime=",m_prime
 #     print "nu=",nu
      x=math.ceil(R*b)/(nu**2*m_prime)*nu**2
      return n + math.ceil((R*b)/(nu**2*m_prime))*cubic_root(R)**2
    if a < nu**2: # case 2
      m_prime = (R*b)/(nu**2)*math.floor((m*nu**2)/(R*b))
      return n + math.ceil((R*b)/(nu*m_prime))*cubic_root(R)
    if a < n: #case 3
      m_prime = (R*b)/(nu)*math.floor((m*nu)/(R*b))
      return n + math.ceil((R*b)/(m_prime))
    return n + 1 # memory is larger than image size
    
n=125.0
b=2.0
R=76000000000.0/b
mem_values=[10**9,2*10**9,4*10**9,6*10**9,8*10**9,10*10**9,12*10**9,14*10**9,16*10**9]
print "#Memory Slices Blocks Buff Slices Cluster Reads"
for m in mem_values:
  
  print  m, t_slices(b,R,n), t_blocks(b,R,n), t_buff_slices(b,R,n,m), t_cluster_reads(b,R,n,m)



