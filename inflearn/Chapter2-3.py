#!/usr/bin/env python
# coding: utf-8

# In[1]:


# chapter02-03
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리


# In[28]:


class Car():
    """
    
    Car class
    Author : Hwang
    Date:2022.01.01
    Description : Class, Static, Instance method
    """
    
    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0
    
    def __init__(self, company, details):
        self._company = company # 인스턴스 변수
        self._details = details
    
    # 인스턴스 메소드
    def __str__(self): # 사용자 레벨
        return 'str : {} - {}'.format(self._company, self._details)
    
    def __repr__(self): # 개발자 레벨 어떤걸 사용해도 상관은 없음
        return 'repr : {} - {}'.format(self._company, self._details)
    
    # Instance Method
    # self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price'))) 
        
    def get_price(self):
        return 'Before Car price -> company : {}, price : {}'.format(self._company, self._details.get('price'))
    
    def get_price_culc(self):
        return 'After Car price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)
    
    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1: 
            print('Please Enter 1 Or More')
            return
        cls.price_per_raise = per
        print('Succeed! price increased')
        
    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry. This car is not Bmw'
        
car1 = Car('Ferrari', {'color':'white', 'horsepower':400,'price':8000})
car2 = Car('Bmw', {'color':'Black', 'horsepower':270,'price':5000})


# In[29]:


# 전체 정보
car1.detail_info()

# 가격 정보
print(car1._details.get('price'))
print(car1._details['price'])


# In[30]:


# 가격정보(인상전)
print(car1.get_price())

# 가격정보(인상후)
Car.price_per_raise = 1.4

print(car1.get_price_culc())


# In[27]:


# 클래스 메소드 사용
Car.raise_price(1.6)
print(car1.get_price_culc())


# In[35]:


# 스테이틱 메소드
# 인스턴스로 호출
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
# 클래스로 호출
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))


# In[ ]:




