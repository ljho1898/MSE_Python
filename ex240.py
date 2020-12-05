#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)

#함수2(2)를 대입 하면 num=12가 되고 함수1(12)를 넣으면 함수0(14)가 된다. 이렇게 28이 된다.
# 답 28

