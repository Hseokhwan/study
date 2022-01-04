#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 시퀀스 : 번호가 입력되어서 나열된 순서
# 시퀀스형 / 비시퀀스형
# 파이썬은 자료형을 2가지로 나눔
# 컨테이너(container : 서로 다른 자료형[list tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque) 
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급


# In[5]:


# Tuple Advanced
# Unpacking

# b, a = a, b

print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*(divmod(100, 9)))


# In[9]:


x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)


# In[15]:


# Mutable(가변) vs Immutable(불변)

l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2
print(l, id(l))
print(m, id(m))

l *= 2
m *= 2
print(l, id(l))
print(m, id(m))


# In[25]:


# sort vs sorted
# reverse, key=len, key=str.lower, key=func...

# sorted : 정렬 후 새로운 객체 반환 (원본 수정 X)
f_list = ['orange', 'apple', 'mango', 'lemon']
print('sorted -', sorted(f_list))
print('sorted -', sorted(f_list, reverse=True))
print('sorted -', sorted(f_list, key=len))
print('sorted -', sorted(f_list, key=lambda x: x[-1]))
print('sorted -', sorted(f_list, key=lambda x: x[-1], reverse=True))

print(f_list)

# sort : 정렬 후 객체 직접 변경 (원본 수정 O)

print('sort -', f_list.sort(), f_list)
print('sort -', f_list.sort(reverse=True), f_list)
print('sort -', f_list.sort(key=len), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1]), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)

print(f_list)
# list vs array 적합한 사용법
# 리스트 기반 : 융통성, 다양한 자료형, 범용적
# 숫자 기반 : 배열(리스트와 거의 호환)


# In[ ]:




