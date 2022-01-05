from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

driver = webdriver.Chrome('./chromedriver')

try:
    driver.get('https://cafe.naver.com/joonggonara')

    elem = driver.find_element_by_id('topLayerQueryInput')
    elem.send_keys('맥북')
    elem.send_keys(Keys.RETURN)

    time.sleep(1)
    
    iframe = driver.find_element_by_xpath("//iframe[@name='cafe_main']")
    driver.switch_to.frame(iframe)

    scope = [
        'https://www.googleapis.com/auth/drive',
        'https://spreadsheets.google.com/feeds'
        ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name('cred.json', scope)
    gs = gspread.authorize(credentials)
    doc = gs.create('중고나라 검색결과')
    ws = doc.get_worksheet(0)

    curr_page = 1
    while True:
        elem = driver.find_element_by_xpath("//div[@id='main-area']")
        trs = elem.find_elements_by_xpath("./div/table/tbody/tr/td/div[@class='board-list']//a")

        for tr in trs:
            ws.append_row([tr.text])

        if curr_page == 1:
            break
        
        curr_page = curr_page + 1
        page = driver.find_element_by_link_text(str(curr_page))
        page.click()

    doc.share('tjrghks3663@gmail.com', perm_type='user', role = 'owner')
    input()
except Exception as e:
    print(e)
finally:
    driver.quit()


