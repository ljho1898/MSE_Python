#!/usr/bin/env python
# coding: utf-8

# In[1]:


def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3):
        message2()
        print("C")
    message1()

message3()

# for을 3번 돌기 때문에 B C  B  C  B  C  가 나오는 것을 알 수 있다. 그 다음 for문을 빠져나고 A가 출력이 된다. 
#답 B
#   C
#   B
#   C
#   B
#   C
#   A


# In[ ]:




