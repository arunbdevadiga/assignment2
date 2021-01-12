#!/usr/bin/env python
# coding: utf-8

# # Assignment-2
# 

# # Q1  write a python program to remove duplicates from the list
# 

# In[3]:


duplicate=[10,20,30,40,20,10,50,60,30,80,70]
print(list(set(duplicate)))


# In[ ]:





# # Q2 write a python program to get the difference between the two list
# 

# In[9]:


list1 =[10,20,30,40,50,60]
list2 =[15,20,35,40,55,70]
set_difference= set(list1)-set(list2) 
list_difference=list(set_difference)
print(list_difference)


# In[ ]:





# # Q3 write a python program to get the frequency of the elements in a list

# In[27]:


import collections
list1=[10,10,10,20,30,40,10,50,60,60]
print("original list :",list1)
a=int(input("Enter a number to get frequency   "))
frequence=list1.count(a)
print("frequency of the element in the list:",frequence)


# In[ ]:





# # Q4 write a python program to compute the similarity between two list

# In[3]:


from collections import Counter
color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]
counter1 = Counter(color1)
counter2 = Counter(color2)
c12= list(counter1 - counter2)
c21= list(counter2 - counter1)
print("Color1-Color2: ",c12)
print("Color2-Color1: ",c21)


# In[ ]:




