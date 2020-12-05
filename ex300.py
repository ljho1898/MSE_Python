#!/usr/bin/env python
# coding: utf-8

# In[1]:


per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")
# 10.31은 잘 실행이 되고 예외가 없기 때문에 clean data가 프린트 될 것이고 변환 완료가 된다.
# 공백은 예외가 발생하기 때문에 0이 출력이 되고 변환 완료가 뜬다.
# 8.00은 잘 실행이 되고 예외가 없기 때문에 clean data가 프린트 될 것이고 변환 완료가 된다.

#답
# 10.31
# clean data
# 변환 완료
# 0
# 변환 완료
# 8.0
# cl3ean data
# 변환 완료


# In[ ]:




