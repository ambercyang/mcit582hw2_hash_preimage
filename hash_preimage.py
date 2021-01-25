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


# In[ ]:


def randomString(N):
    return ''.join(random.choice(string.ascii_lowercase + ' ') for i in range(N))
  


# In[4]:


def my_to_bin(string):
    res = ''
    for char in string:
        tmp = (bin(int(char,16))[2:])
        tmp = '%08d' %int(tmp)
        res += tmp
    return res


# In[7]:


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
        x_hex = hashlib.sha256(x_str.encode('utf-8')).hexdigest()
        x_binary = my_to_bin(x_hex)
        last_k_digits = x_binary[-k:]
        
        if str(last_k_digits) == target_string:
            return(x_int)
        
    return( nonce )


# In[8]:


target_string = "101"
hash_preimage(target_string)


# In[18]:


x_tr = str(83)
my_to_bin(hashlib.sha256(x_tr.encode('utf-8')).hexdigest())


# In[ ]:




