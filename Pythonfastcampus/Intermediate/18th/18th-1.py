from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from myid import ID, PW
from time import time

driver = webdriver.Chrome('./chromedriver')

try:
    driver.get('http://instagram.com')

    driver.implicitly_wait(time_to_wait=5)

    elem = driver.find_element_by_name('username')
    elem.send_keys(ID)
    elem = driver.find_element_by_name('password')
    elem.send_keys(PW)
    elem.send_keys(Keys.RETURN)

    driver.implicitly_wait(time_to_wait=5)

    elem = driver.find_element_by_class_name('cmbtv')
    elem.click()

    driver.implicitly_wait(time_to_wait=5)

    elem = driver.find_element_by_xpath("//span[text()='검색']/..")
    ac = ActionChains(driver)
    ac.move_to_element(elem)
    ac.click()
    ac.send_keys('#패스트캠퍼스')
    ac.perform()   

    time.sleep(1)
 
    ac.reset_actions()
    ac.move_by_offset(0, 50)
    ac.click()
    ac.perform()

    input()

    divs = elem.find_elements_by_xpath("//*[text()='인기 게시물']/../..//a[contains(@href, '/p')]")
    ac = ActionChains(driver)

    for div in divs:
        ac.reset_actions()
        ac.move_to_element(div)
        ac.click()
        ac.perform()

        time.sleep(1)
        
        try:
            ac.reset_actions()
            elem = driver.find_element_by_xpath("//*[@aria-label='좋아요' and @height='24']")
            ac.move_to_element(elem)
            ac.click()
            ac.perform
        except:
            print('이미 좋아요를 누른 게시물')

        ac.reset_actions()
        ac.send_keys(Keys.ESCAPE)
        ac.perform()

        time.sleep(1)

    input()
except Exception as e:
    print(e)
finally:
    driver.quit()