#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Special Method(=Magic Method)
# 파이썬의 핵심 4가지 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), class   
# 클래스(스페셜메소드) -> 시퀀스 -> 반복&함수 로 연결
# 스페셜 메소드 = 클래스안에 정의할 수 있는 특별한(Built-in) 메소드 ex. __str__ / __del__ ...
# 이미 만들어져 있는 클래스 메소드를 수정, 변경하는 것


# In[2]:


# 기본형
print(int)
print(float)


# In[4]:


#모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))


# In[11]:


n = 10

print(n+100)
print(n.__add__(100))
print(n.__doc__)
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))
# 내부적으로 호출되는 메소드를 직접 호출할 수 있고 직접 수정 가능


# In[25]:


# 클래스 에제1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price
        
    def __str__(self):
        return 'Fruit Class Info : {}, {}'.format(self._name, self._price)

    # 메소드를 불러올때 자동으로 첫번째는 self로 두번째부터는 x로 인식
    def __add__(self, x):
        print('called __add__')
        return self._price + x._price
    
    def __sub__(self, x):
        return self._price - x._price
    
    def __le__(self, x):
        if self._price <= x._price:
            return True
        else:
            return False
        
    def __ge__(self, x):
        if self._price >= x._price:
            return True
        else:
            return False


# In[26]:


# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

print(s1 + s2)
print(s1._price + s2._price)


# In[32]:


# 매직메소드
print(s1 >= s2)
print(s1 <= s2)
print(s1 - s2)
print(s2 - s1)
print(s1)
print(s2)


# In[ ]:




