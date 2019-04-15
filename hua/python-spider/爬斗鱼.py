from selenium import webdriver
driver=webdriver.Chrome()#driver就是我们的一个操作谷歌浏览器的对象

driver.get('https://www.douyu.com/directory/all')

#driver.quit()

driver.find_element_by_xpath(//*[@id="listAll"]/div[2]/ul/li[1]/div/a[1]/div[1]/div[1]/img)