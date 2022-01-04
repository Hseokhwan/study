#!/usr/bin/env python
# coding: utf-8

# In[9]:


# chapter02-01
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리


# In[16]:


class Car():
    """
    
    Car class
    Author : Hwang
    Date:2022.01.01
    """
    
    # 클래스 변수(모든 인스턴스가 공유)
    car_count = 0
    
    def __init__(self, company, details):
        self._company = company # 인스턴스 변수
        self._details = details
        Car.car_count += 1
    
    # 인스턴스 메소드
    def __str__(self): # 사용자 레벨
        return 'str : {} - {}'.format(self._company, self._details)
    
    def __repr__(self): # 개발자 레벨 어떤걸 사용해도 상관은 없음
        return 'repr : {} - {}'.format(self._company, self._details)

    def __del__(self):
        Car.car_count -= 1
    
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price'))) 
        
car1 = Car('Ferrari', {'color':'white', 'horsepower':400,'price':8000})
car2 = Car('Bmw', {'color':'Black', 'horsepower':270,'price':5000})
car3 = Car('Audi', {'color':'silver','horsepower':300,'price':6000})

# ID 확인 - 각각 고유 id 가 있다 -> self의 의미!
print(id(car1))
print(id(car2))
print(id(car3))


# In[17]:


print(car1._company == car2._company)
print(car1 is car2)

# dir & __dict__ 확인

print(dir(car1))
print(dir(car2))

print(car1.__dict__)

# Doctring

print(Car.__doc__)


# In[18]:


car1.detail_info()

print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__))


# In[19]:


car1.detail_info()
Car.detail_info(car1)


# In[20]:


print(car1.car_count)
print(car1.__dict__)
print(dir(car1))


# In[21]:


del car2
print(car1.car_count)
print(Car.car_count)


# In[ ]:


# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후, 상위 클래스 변수 찾음) init --> 클래스 변수


# In[ ]:




