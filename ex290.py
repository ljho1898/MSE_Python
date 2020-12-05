#!/usr/bin/env python
# coding: utf-8

# In[1]:


class 부모:
    def __init__(self):
        print("부모생성")

class 자식(부모):
    def __init__(self):
        print("자식생성")
        super().__init__()    # ()안에 self가 알아서 전달이 되기 때문에 쓰지 않아도 된다.

나 = 자식()

# 자식클레스에 객체가 생성될때 생성자가 호출이 될것이고 자식생성을 프린트를 한다. 
# 그다음 부모클래스의 생성자를 super로명시적으로 호출 했기 때문에 부모생성이 프린트 된다.

#답
# 자식생성
# 부모생성


# In[ ]:




