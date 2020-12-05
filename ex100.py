#!/usr/bin/env python
# coding: utf-8

# In[1]:


date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price)) 
print(close_table)
# date 와 close_price를 zip으로 묶은뒤 dict함수 안에다 넣는다. 
# 답 {'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}


# In[ ]:




