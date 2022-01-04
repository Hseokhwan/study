#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 시퀀스 : 번호가 입력되어서 나열된 순서
# 시퀀스형 / 비시퀀스형
# 파이썬은 자료형을 2가지로 나눔
# 컨테이너(container : 서로 다른 자료형[list tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque) 
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급


# In[5]:


# 지능형 리스트(comprehending lists)
chars = '+_)(&*(^@#$'
code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))
    
print(code_list1)

# 지능형 리스트(comprehending lists)
code_list2 = [ord(s) for s in chars]
print(code_list2) 


# In[ ]:


# Comprehending lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
print(code_list3)

code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))
print(code_list4)


# In[11]:


# 전체 출력
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])


# In[18]:


# Generator 생성 / dir에 __iter__가 들어가있으면 for문 순회 가능
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지 X)
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))

print(tuple_g)
print(type(tuple_g))
print(next(tuple_g))
print(next(tuple_g))

print(array_g)
print(type(array_g))
print(array_g.tolist())


# In[22]:


# 제네레이터 예제
print(('%s' % c + str(n) for c in ['A','B','C','D'] for n in range(1,21)))

#for s in ('%s' % c + str(n) for c in ['A','B','C','D'] for n in range(1,21)):
#    print(s)


# In[34]:


# 리스트 주의
mark1 = [['~'] * 3 for n in range(4)]
mark2 = [['~'] * 3] * 4 

print(mark1)
print(mark2)

# 수정
mark1[0][1] = 'X'
mark2[0][1] = 'X'

print(mark1)
print(mark2)

print([id(mark1) for n in mark1])
print([id(mark2) for n in mark2])


# In[ ]:




