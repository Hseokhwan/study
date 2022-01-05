from selenium  import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

try:
    driver.get('https://naver.com')

    elem = driver.find_element_by_id('query')
    elem.send_keys('패스트캠퍼스')
    elem.send_keys(Keys.RETURN)

    elem = driver.find_element_by_class_name('_list_base')
    lis = elem.find_elements_by_tag_name('li')

    for i in lis:
        atag = i.find_element_by_class_name('api_txt_lines')
        print(atag.text)
        print(atag.get_attribute('href'))

    print('-'*50)

    elem = driver.find_element_by_class_name('sp_nkin')
    lis = elem.find_elements_by_xpath('./div/ul/li')

    for i in lis:
        print(i.text)

    input()
except Exception as e:
    print(e)
finally:
    driver.quit()
    
