#!/usr/bin/env python
# coding: utf-8

# In[1]:


def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)

# 여기서  (a,b)  =  (b=100, a= 200)이기 때문에  a=b=100 이 되고 b=a=20이 되어버린다. 
# 따라서 왼쪽이 200이고 오른쪽이 100이 된다.
# 답 왼쪽: 200
#    오른쪽: 100


# In[ ]:




