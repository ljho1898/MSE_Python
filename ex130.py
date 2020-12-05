#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")
    
# 시가+변동폭이 최고가보다 크면 상승장이 나오고 작으면 하락장이 나온다.
# 따라서 답은 상승장이다.


# In[ ]:




