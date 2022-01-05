from selenium import webdriver
import datetime
import time
import os
import telepot


f = open('product.txt', 'r')
products = f.readlines()
f.close()

prices = None
if os.path.exists('output.csv'):
    f = open('output.csv', 'r')
    prices = f.readlines().pop().strip().split(',') # 리스트 중 가장 마지막을 꺼내주는 함수
    f.close()

output = open('output.csv', 'a')

driver = webdriver.Chrome('./chromedriver')

try:
    idx = 1
    header = ['']
    data = [str(datetime.datetime.now())]
    diff = []
    for url in products:
        url = url.strip()
        driver.get(url)

        time.sleep(1)  

        elem = driver.find_element_by_xpath("//div[@class='c_product_info_title']/h1[@class='title']")
        name = elem.text

        elem = driver.find_element_by_xpath("//dd/strong/span[@class='value']")
        price = elem.text.replace(',','').replace('원','')

        if prices and price != prices[idx]:
            diff.append((name, prices[idx], price))

        header.append(name.replace(',',''))
        data.append(price.replace(',',''))

        idx += 1
        
    if diff:
        bot = telepot.Bot('1913272827:AAEDSjf8fqNwuJvw8ZXHw5WR41P_re6ti8Q')
        msg = ''
        for info in diff:
            msg += '- %s\n%s => %s\n' % info
        bot.sendMessage('1824238459',msg)
        


    if not os.path.exists('output.csv'):
        output.write(','.join(header)+'\n')
    
    output.write(','.join(data)+'\n')

except Exception as e:
    print(e)

finally:
    driver.quit()

