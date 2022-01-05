from selenium import webdriver
import datetime
import time
import os
import telepot

def write_log(msg):
    base_dir = os.path.dirname(os.path.realpath(__file__))
    f = open(os.path.join(base_dir, 'auto.log'), 'a')
    f.write('[%s] %s\n' % (str(datetime.datetime.now()), msg))
    f.close()

base_dir = os.path.dirname(os.path.realpath(__file__))

write_log('제품 리스트를 가져옵니다.')

f = open(os.path.join(base_dir, 'product.txt'), 'r')
products = f.readlines()
f.close()

output_filename = os.path.join(base_dir, 'output.csv')
prices = None
if os.path.exists(output_filename):
    f = open(output_filename, 'r')
    prices = f.readlines().pop().strip().split(',') # pop 리스트 중 가장 마지막을 꺼내주는 함수
    f.close()

output = open(output_filename, 'a')

write_log('제품 리스트를 가져옵니다.')
opts = webdriver.ChromeOptions()
opts.headless=True
driver = webdriver.Chrome(os.path.join(base_dir, 'chromedriver'), options=opts)

try:
    idx = 1
    header = ['']
    data = [str(datetime.datetime.now())]
    diff = []
    write_log('상품 정보를 조회합니다.')
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
        write_log('텔레그램으로 알림을 보냅니다.')
        bot = telepot.Bot('1913272827:AAEDSjf8fqNwuJvw8ZXHw5WR41P_re6ti8Q')
        msg = ''
        for info in diff:
            msg += '- %s\n%s => %s\n' % info
        bot.sendMessage('1824238459',msg)
        


    if not os.path.exists(output_filename):
        output.write(','.join(header)+'\n')
    
    output.write(','.join(data)+'\n')

except Exception as e:
    write_log(e)

finally:
    driver.quit()

