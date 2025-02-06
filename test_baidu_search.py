from selenium import webdriver  
from selenium.webdriver.common.by import By  
import pytest  

@pytest.fixture  
def setup():  
    driver = webdriver.Chrome()  
    driver.get("https://www.baidu.com")  
    yield driver  # 测试执行完成后关闭浏览器  
    driver.quit()  

def test_baidu_search(setup):  
    driver = setup  
    search_box = driver.find_element(By.ID, "kw")  
    search_box.send_keys("软件测试")  
    driver.find_element(By.ID, "su").click()  
    assert "软件测试" in driver.title or "百度一下，你就知道" in driver.title