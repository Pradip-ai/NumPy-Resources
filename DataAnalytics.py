#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
arr1 = np.array([1, 2, 3])

print(arr1)


# In[6]:


print(type(arr1))


# In[7]:


print(arr1.shape)


# In[8]:


print(arr1[2])


# In[10]:


arr1[2] =  5
arr1


# In[12]:


arr2 = np.array([[1, 2, 3], [3, 4, 5]])
arr2


# In[13]:


arr2[1][2]


# In[15]:


print(arr2.shape)


# In[17]:


arr2[1, 2]


# In[18]:


arr2[1][-1]


# In[20]:


arrS = np.array(['china', 'India', 'USA', 'Mexixo'])
arrS


# In[21]:


arrR = np.arange(0, 20, 2)
arrR


# In[22]:


arrL = np.linspace(0,10, 20)
arrL


# In[23]:


arr = np.random.rand(10)
arr


# In[28]:


print(np.zeros(10))
print('/n')
print(np.zeros((2,3)))


# In[33]:


arr = np.array([1,2,3,4,5])
print(arr)


# In[35]:


import numpy as np

print(np.__version__)


# In[39]:


arr = np.array([1,2,3,4,5])    # Creating a numpy ndarray object
print(arr)
print(type(arr))


# In[38]:





# In[40]:


#creating  a 0-D array with 42
arr = np.array(42)
print(arr)


# In[43]:


#Creating a 1-D  array containg 1,2,3,4,5
arr = np.array([1,2,3,4,5])
print(arr)


# In[45]:


#creaeting a 2-D arrrays
arr = np.array([[1,2,3,4], [4,5,6,7]])
print(arr)


# In[46]:


#creating a 3-D arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)


# In[50]:


#cecking Dimernsion of the array
a = np.array(42)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3,4], [4,5,6,7]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# In[55]:


#creating the higher dimension arrays
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)


# In[59]:


#Getting the first element from the following elements 
arr = np.array([1,2,3,4])
print(arr[2] + arr[3])


# In[70]:


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])


# In[72]:


arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])


# In[73]:


# Slicing 2-D arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])


# In[77]:





# In[82]:


arr = np.array([1,2,3,4])
print(arr.dtype)


# In[83]:


arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)


# In[87]:


arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)


# In[90]:


arr = np.array([1,2,3,4])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)


# In[91]:


arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)


# In[92]:


arr = np.array([1,2,3,4,5])
print(arr.shape)


# In[101]:


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2,3,2)

print(newarr)


# In[108]:


a = np.array[(2,3,4)]
x = np.sum


# In[110]:


arr = np.array(['cow', 'rat'])
print(arr.dtype)


# In[113]:


arr = np.array([1, 2, 3, 4])

x = arr.view()
x[1] = 21
print(arr)
print(x)


# In[119]:


arr = np.array([[1,2,3,4], [2,3,4,5]])
for x in arr:
    for y in x:
        
        print(y)
    


# In[120]:


arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)


# In[121]:


arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)


# In[123]:


a = [1,2,3]
sum = 0
for i in a:
    sum += i
print(sum)


# In[ ]:




