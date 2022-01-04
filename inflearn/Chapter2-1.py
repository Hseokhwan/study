#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# chapter02-01
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지


# In[7]:


car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color':'white'},
    {'horsepower':400},
    {'price':8000}
]

car_company_2 = 'Bmw'
car_detail_2 = [
    {'color':'Black'},
    {'horsepower':270},
    {'price':5000}
]

car_company_3 = 'Audi'
car_detail_3 = [
    {'color':'silver'},
    {'horsepower':300},
    {'price':6000}
]

# 리스트 구조
car_company_list = ['Ferrari', 'Bmw', 'Audi']
car_detail_list = [
    {'color':'white', 'horsepower':400,'price':8000},
    {'color':'Black', 'horsepower':270,'price':5000},
    {'color':'silver','horsepower':300,'price':6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)


# In[9]:


# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등

car_dicts = [
    {'car_company': 'Ferrari', 'car_detail':{'color':'white', 'horsepower':400,'price':8000}},
    {'car_company': 'Bmw', 'car_detail':{'color':'Black', 'horsepower':270,'price':5000}},
    {'car_company': 'Audi', 'car_detail':{'color':'silver','horsepower':300,'price':6000}}
]

del car_dicts[1]
print(car_dicts)


# In[13]:


# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details
    
    # 인스턴스 메소드
    def __str__(self): # 사용자 레벨
        return 'str : {} - {}'.format(self._company, self._details)
    
    def __repr__(self): # 개발자 레벨 어떤걸 사용해도 상관은 없음
        return 'repr : {} - {}'.format(self._company, self._details)
        
car1 = Car('Ferrari', {'color':'white', 'horsepower':400,'price':8000})
car2 = Car('Bmw', {'color':'Black', 'horsepower':270,'price':5000})
car3 = Car('Audi', {'color':'silver','horsepower':300,'price':6000})

print(car1)
print(car2)
print(car3)

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

print(dir(car1))

        


# In[14]:


# 리스트 선언

car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)


# In[ ]:




