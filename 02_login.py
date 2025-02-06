from selenium import webdriver  
from selenium.webdriver.common.by import By  
import time  

def test_02login():  
    driver = webdriver.Chrome()  
    driver.get("https://demoqa.com/login")  

    # 输入用户名和密码  
    driver.find_element(By.ID, "userName").send_keys("testuser")  
    driver.find_element(By.ID, "password").send_keys("Password123!")  

    # 点击登录按钮  
    driver.find_element(By.ID, "login").click()  

    # 验证登录结果（此处需根据实际页面调整断言逻辑）  
    time.sleep(2)  
    assert "profile" in driver.current_url  

    driver.quit()  