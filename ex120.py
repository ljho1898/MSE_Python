#!/usr/bin/env python
# coding: utf-8

# In[ ]:


fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("좋아하는 과일은?")
if user in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")

#fruit에 있는 과일을 말할 때만 정답이고 나머지는 오답이기 때문에 if문으로 만들수 있다.
# 따라서 딸기라고 말하면 정답이 나오고 배 라고 말하면 오답이 나온다.

