#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Special Method(=Magic Method)
# 파이썬의 핵심 4가지 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), class   
# 클래스(스페셜메소드) -> 시퀀스 -> 반복&함수 로 연결
# 스페셜 메소드 = 클래스안에 정의할 수 있는 특별한(Built-in) 메소드 ex. __str__ / __del__ ...
# 이미 만들어져 있는 클래스 메소드를 수정, 변경하는 것


# In[3]:


# 객체 -> 파이선의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt( (pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2 )
print(l_leng1)


# In[9]:


# 네임드 튜플 사용
from collections import namedtuple

# 네임드 튜플 선언 (인덱스로도 접근 가능, 키 값으로도 접근 가능)
Point = namedtuple('Point', 'x y')


# In[11]:


pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3)
print(pt4)
print(pt3.x)


# In[13]:


l_leng2 = sqrt( (pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2 )
print(l_leng2)


# In[15]:


# 네임드 튜플 선언 방법(4가지)
Point1 = namedtuple('Point1', ['x', 'y'])
Point2 = namedtuple('Point2', 'x, y') 
Point3 = namedtuple('Point3', 'x y')
Point4 = namedtuple('Point4', 'x y x class', rename=True) # Default = False 키 값이 겹치고 예약어이기 때문

print(Point4)


# In[20]:


print(Point1, Point2, Point3, Point4)


# In[23]:


# Dict to Unpacking
temp_dict = {'x':75, 'y':55}


# In[24]:


# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)

print(p1)
print(p2)
print(p3)
# rename 테스트
print(p4)
# 언패킹
print(p5)


# In[30]:


# 사용
print(p1[0]+p2[1])
print(p1.x+p2.y)

x, y = p3
print(x, y)


# In[34]:


# 네임드 튜플 메소드
temp = [52, 38]

# _make() : 새로운 객체 생성
p4 = Point1._make(temp)
print(p4)

# _fields : 필드 네임 확인
print(p1._fields, p2._fields, p3._fields)

# _asdict() : OrderedDict 반환
print(p1._asdict())
print(p2._asdict())


# In[40]:


# 실사용 실습
# 반 20명, 4개 반(A,B,C,D)

Classes = namedtuple('Classes', 'rank, number')

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

print(numbers)
print(ranks)

# List comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

print(len(students))
print(students)


# In[42]:


# 추천
students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
                 for number in [str(n)
                                for n in range(1, 21)]]

print(len(students2))
print(students2)


# In[43]:


# 출력
for s in students2:
    print(s)


# In[ ]:




