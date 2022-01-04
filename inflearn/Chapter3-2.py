#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Special Method(=Magic Method)
# 파이썬의 핵심 4가지 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), class   
# 클래스(스페셜메소드) -> 시퀀스 -> 반복&함수 로 연결
# 스페셜 메소드 = 클래스안에 정의할 수 있는 특별한(Built-in) 메소드 ex. __str__ / __del__ ...
# 이미 만들어져 있는 클래스 메소드를 수정, 변경하는 것


# In[10]:


# 클래스 예제2
# 벡터(x,y) (5,2) = 좌표평면에서 크기와 방향, 속도를 갖는 것
# 좌표평면 상에서 연산

class Vector(object):
    def __init__(self, *arg):
        '''
        
        Create a vector, example : v = Vector(5, 10)
        '''
        # 예외처리
        if len(arg) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = arg
            
    def __repr__(self):
        '''Return the vector informations.'''
        return 'Vector(%r, %r)' % (self._x, self._y)
    
    def __add__(self, other):
        '''Return the vector addtion of self and other'''
        return Vector(self._x + other._x, self._y + other._y)
    
    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)
    
    # (0,0) 인지 확인하는 메소드
    def __bool__(self):
        return bool(max(self._x, self._y))
        
print(Vector.__init__.__doc__)


# In[11]:


# Vector 인스턴스 생성
v1 = Vector(5,7)
v2 = Vector(23,55)
v3 = Vector()


# In[20]:


# 매직메소드 출력
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)

print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(v2 * 10)
print(bool(v1), bool(v2))
print(bool(v3))


# In[ ]:




