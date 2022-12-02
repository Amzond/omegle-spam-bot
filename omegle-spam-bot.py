from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("https://www.omegle.com/")
time.sleep(2)
cli=driver.find_element("xpath", "/html/body/div[3]/table/tbody/tr[2]/td[2]/img")
cli.click()
time.sleep(5)
while True:
    text_area=driver.find_element("xpath", "/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[2]/div/textarea")
    #Type your text that you want to spam 
    text_area.send_keys('That soo easy to create spam bot LOL')

    send_btn=driver.find_element("xpath","/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[3]/div/button")
    send_btn.click()

    esc_btn=driver.find_element("xpath", "/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[1]/div/button")
    esc_btn.click()
    time.sleep(2)
    esc_btn.click()
    time.sleep(2)
    esc_btn.click()
    time.sleep(10)

