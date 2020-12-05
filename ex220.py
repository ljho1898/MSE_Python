#!/usr/bin/env python
# coding: utf-8

# In[4]:


def print_max(a, b, c) :
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)
    
print_max(9,5,6)

# if를 사용하여 a가 b,c보다 클 때 elif를 이용하여 b가 a,c보다 클 때 그다음 둘다 아닐때 else로 c를 출력하도록 한다.
# 답 9


# In[ ]:




