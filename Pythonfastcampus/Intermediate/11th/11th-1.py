from selenium  import webdriver

driver = webdriver.Chrome('./chromedriver') #./ 의미는 현재 있는 폴더

try:
    driver.get('http://news.naver.com')

    elem = driver.find_element_by_id('_rankingList0')

    lis = elem.find_elements_by_tag_name('li')

    for li in lis:
        print(li.text)

    input()
except Exception as e:
    print(e)
finally:
    driver.quit()

