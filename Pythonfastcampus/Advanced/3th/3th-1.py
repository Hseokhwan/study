from selenium import webdriver
import datetime
import time
import os


f = open('product.txt', 'r')
products = f.readlines()

output = open('output.csv', 'a')

driver = webdriver.Chrome('./chromedriver')

try:
    header = ['']
    data = [str(datetime.datetime.now())]
    for url in products:
        url = url.strip()
        driver.get(url)

        time.sleep(1)  

        elem = driver.find_element_by_xpath("//div[@class='c_product_info_title']/h1[@class='title']")
        name = elem.text

        elem = driver.find_element_by_xpath("//dd/strong/span[@class='value']")
        price = elem.text.replace('원','')

        header.append(name.replace(',',''))
        data.append(price.replace(',',''))

    if not os.path.exists('output.csv'):
        output.write(','.join(header)+'\n')
    
    output.write(','.join(data)+'\n')

except Exception as e:
    print(e)

finally:
    driver.quit()

