#!/usr/bin/env python
# coding: utf-8

#  1. Partial preimages
# Use a brute-force algorithm to find a partial preimage.
# Using the template “hash_preimage.py” write a function called “hash_preimage” that takes a single input, target_string, where target_string is a string of bits. The function “hash_preimage” should return a single variable x such that the trailing bits of SHA256(x) matches the target string (not the hash of the target string).
# Your algorithm should be randomized, i.e., hash_preimage(target_string) should not always return the same partial preimage
# 
#     Example: If our target string was 101 and the hash(x)=01000101 then this would be a match because the least significant bits (rightmost) completely match the target string.
# 

# In[1]:


import hashlib
import os
import string
import random


# In[2]:


def randomString(N):
    return ''.join(random.choice(string.ascii_lowercase + ' ') for i in range(N))
  


# In[3]:


def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    nonce = b'\x00'
    
    N=1000000
    n=1000
    k=len(target_string)
    
    x_int = random.randint(1, n)
    msg_bytes = target_string.encode('utf-8')
 
    
   # while True:
    for i in range(N):
        x_int = x_int+1
        x_str = str(x_int)
        x_binary = bin(int(hashlib.sha256(x_str.encode('utf-8')).hexdigest(),16))
        last_k_digits = x_binary[-k:]
        
        if str(last_k_digits) == target_string:
            return(x_str)
        
    return( nonce )


# In[4]:


target_string = "1011111"
myx = hash_preimage(target_string)


# In[8]:


bin(int(hashlib.sha256(myx.encode('utf-8')).hexdigest(),16))


# In[ ]:




