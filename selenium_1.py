import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net/")

""" driver.get("https://tinder.com/")
link = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[3]/div[2]/div/div/button[2]')
link.click() """


link = driver.find_element_by_link_text("Python Programming")
link.click()

try: 
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials")))
    element.click()

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sow-button-19310003")))
    element.click()

   
    """ driver.back() #go to previous page
    driver.forward() #go to next page """
    
except:
    driver.quit()

""" driver.find_element_by_link_text("Log in").click() """

""" search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN) # this method is clicking Enter (In selenium enter is RETURN, I dont know why) """


"""
#video 1
print("Now is searching for test")
search.send_keys(Keys.RETURN)
print("Everything is OK")
time.sleep(5)

print("Browser will close in: ")
for i in range(3,0,-1):
    print(i)
    time.sleep(1) """

"""
#video 2
 try: 
    main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "main")))
    print(main.text)

except:
    driver.quit()
 """
time.sleep(5)
driver.quit()

