from lib2to3.pgen2 import driver
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

try:
    driver.get('https://fastcampus.co.kr/category_online_programming')
    elem = driver.find_element_by_class_name('infinity-course')
    strongs = elem.find_elements_by_tag_name('strong')

    for strong in strongs:
        print(strong.text.replace('.', ''))
        print('-'*40)

    input()
except Exception as e:
    print(e)
finally:
    driver.quit()
