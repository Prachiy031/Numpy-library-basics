#!/usr/bin/env python
# coding: utf-8

# # numpy
# its fast
# 

# In[49]:


import numpy as np


# numpy array using list

# In[5]:


a = np.array([8,9,90,67,88],dtype='f') #datatype is defined as a float it can be defined acc to data containing in array 
print(a)              


# numpy array using tuple

# In[6]:


b = np.array((8,9,90,67,88))   #can define in this way also
print(b)              #datatype is optional


# In[7]:


type(a)


# In[8]:


type(b)


# In[9]:


b.dtype


# In[10]:


a.dtype


# multidimentional array

# In[11]:


m = np.array([[7,9,0],[8,6,4]])


# In[12]:


m.ndim


# In[13]:


m[0,1]      #1st array 2nd element


# In[14]:


p = np.array([[7,9,0],[8,6,4],[80,90,70]])   #each array should have same number of elem


# In[15]:


p.ndim


# In[16]:


p[1,2]


# In[17]:


u = np.array([[[7,8,90],[80,5,34],[35,77,12]],[[89,56,34],[-7,-45,-70],[77,55,44]]])


# In[18]:


u[0][1][1]    #3 dimentional array 1st nd array, 2nd array, 1st element


# In[19]:


u[1][2][2]


# In[20]:


u.ndim


# In[21]:


u.shape      #2 2d array 3 lists 3 elements


# In[22]:


type(u)


# In[23]:


u.shape[0]       #2 2d arrays


# In[24]:


u.size #total no. of eleme


# In[25]:


u.nbytes #no of bytes taking in memory


# In[28]:


A = np.arange(80)  #creates 1d array in our mentioned range


# In[29]:


A


# In[32]:


K = np.arange(4,90)    #from 4 to 90


# In[33]:


K


# In[34]:


K = np.arange(4,90,2)  #2 steps
print(K)


# In[40]:


print(list(range(10)))       #list of 10 range


# In[48]:


d = np.random.permutation(np.arange(10)) #shuffle number in random order


# In[49]:


d


# In[52]:


np.random.randint(34,50) #return any random no.between 34 50


# In[55]:


s = np.random.rand(2,3) #2 by 3 matrix 


# In[56]:


s


# In[64]:


d = np.random.rand(2,3,4,2)     #2 arrays of 3dim each 3 dim array has 3 2 dim arrays each 2 dim array has 4 1d arrays and each 1d array has 2ele in it  


# In[70]:


d
#d.ndim


# In[72]:


g = np.arange(60).reshape(4,15)


# In[73]:


g


# In[74]:


g.shape


# In[77]:


np.zeros((2,3),dtype=int)


# slicing

# slicing in numpy uses same memory of given array ..it doesent create copy but creates view...this is big diff in ordinary list or data structure and numpy array

# In[102]:


A = np.random.rand(5)


# In[103]:


A


# In[104]:


B = A[2:5]


# In[105]:


B


# In[106]:


B[0]=  67


# In[107]:


B


# In[109]:


A      #value also added in A also    


# In[114]:


A = np.random.rand(5,4)


# In[115]:


A


# In[ ]:





# In[116]:


D = A[2:4]


# In[117]:


D


# In[118]:


#if we dont want view then create copy b = A[3:10].copy()


# In[5]:


#index of any element
S = np.arange(30)
S


# In[10]:


index = np.argwhere(S==17)  #where is elem 17   #if 2d array is there then add [0][0] in front of(s==17)


# In[11]:


index


# In[22]:


S = np.round(10*np.random.rand(5,6))   #scales values upto 10 and randomly arrange them and rounds values to int


# In[23]:


S


# In[25]:


#access
S[4,1]


# In[26]:


S[1,:]  #all whole row


# In[27]:


S[:,1]    #all whole colm


# In[32]:


S[1:3,3:5]  #consider 1:3 rows(excluded) and 3:5(excluded)colm for submatrix


# In[33]:


S.T   #transpose


# library for linear library

# In[34]:


import numpy.linalg as la


# In[37]:


la.inv(np.random.rand(3,3))    #inverse of matrix


# In[38]:


S.sort(axis=0)   #sorted colm


# In[39]:


S


# In[40]:


S.sort(axis=1) #sorted rows


# In[41]:


S


# numpy more indexing

# In[42]:


S[1,3]


# In[43]:


F = np.arange(20)


# In[44]:


F


# In[51]:


R = F[F>10]


# In[52]:


R


# In[53]:


F


# In[57]:


R = F[(F<20) & (F>10)]


# In[58]:


R


# In[59]:


#  & is used for arrays, and is used for single object  
# | for arrays ,or for single object
# ~ for arrays ,not for single object


# masking

# In[15]:


#broadcasting:  this will match the other elem to match dimension of matrix to add matrix of same dim
Matrix = np.round(10*np.random.rand(2,3))
Matrix


# In[22]:


Matrix+6        #this is mapping as it has created 3 by 2 matrix of 6 ele in it


# In[23]:


Matrix+(np.arange(2).reshape(2,1))


# In[30]:


#universal functions
#conatenate arrays horrizontally
A = np.round(5*np.random.rand(3,4))
A


# In[29]:


B = np.round(5*np.random.rand(3,4))
B


# In[34]:


C = np.hstack((A,B)) #if hosrizontal conact then all  arrays should be in tuple
C


# In[35]:


C = np.vstack((A,B)) 
C


# In[42]:


C.sort(axis=1)
C


# In[44]:


D = np.array([1,2,4,56,7])
D


# In[45]:


np.sort(D)


# how numpy is fast

# In[52]:


V = np.random.rand(100000)
get_ipython().run_line_magic('timeit', 'sum(V)     #under python by default function')
get_ipython().run_line_magic('timeit', 'np.sum(V)   #under numpy    this is faaster than sum function')


# In[ ]:




