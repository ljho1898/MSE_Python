#!/usr/bin/env python
# coding: utf-8

# In[4]:


리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    split = i.split(".")
    if (split[1] == "h") or (split[1] == "c"):
        print(i)


#답 intra.h
#   intra.c
#   define.h


# In[ ]:




