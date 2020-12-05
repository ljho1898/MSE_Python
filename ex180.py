#!/usr/bin/env python
# coding: utf-8

# In[4]:


low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []
for i in range(len(low_prices)) :
    volatility.append(high_prices[i] - low_prices[i])
print(volatility)

#low와 high의 변동 폭을 구하는 것이기 때문에 high에서 low를 뺴면 된다. 따라서 append의 메소드를 사용하여 위와 같이 코드를 짠다.
#답 [50, 100, 30, 80, 0]


# In[ ]:




