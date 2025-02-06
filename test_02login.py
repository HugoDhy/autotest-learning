from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
import pytest  

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/login")
    yield driver
    driver.quit()

def test_login_success(setup):
    driver = setup
    driver.find_element(By.ID, "userName").send_keys("testuser")
    driver.find_element(By.ID, "password").send_keys("Password123!")
    driver.find_element(By.ID, "login").click()
    
    # 使用显式等待确保页面已经跳转
    WebDriverWait(driver, 10).until(EC.url_contains("profile"))
    assert "profile" in driver.current_url

def test_login_failure(setup):
    driver = setup
    driver.find_element(By.ID, "userName").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login").click()
    
    # 使用显式等待确保错误消息已经显示
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "name")))
    error_message = driver.find_element(By.ID, "name").text
    assert "Invalid username or password" in error_message
