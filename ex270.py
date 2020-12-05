#!/usr/bin/env python
# coding: utf-8

# In[45]:


class stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per  = per
        self.pbr  = pbr
        self.배당수익률 = 배당수익률
        
종목 = []

삼성 = stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
    print(i.code, i.per) 

#  종목을 만들고 종목 리스트에 추가를 하고 루프를 통해서 각각의 종목을 하나씩 가져와서 프린트 하는것을 알 수 있다.   
#답     
# 005930 15.79
# 005380 8.7
# 066570 317.34


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




