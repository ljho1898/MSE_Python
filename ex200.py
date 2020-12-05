#!/usr/bin/env python
# coding: utf-8

# In[3]:


ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
profit = 0
for row in ohlc[1:]:
    profit += (row[3] - row[0])
print(profit)

# 각 거래일 수익금= 시가 - 종가     for문으로 시가-종가를 다 더한다.  그다음 for문을 빠져 나간다.
# 답 0


# In[ ]:




