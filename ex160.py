#!/usr/bin/env python
# coding: utf-8

# In[4]:


리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    split = i.split(".")
    if (split[1] == "h") or (split[1] == "c"):
        print(i)

# . 을 기준으로 쪼개며 뒤에 h와c가 나올 경우에만 프린트 한다.
#답 intra.h
#   intra.c
#   define.h


# In[ ]:




