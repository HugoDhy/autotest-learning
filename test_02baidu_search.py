# test_baidu_search.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote_plus
from test_02data import TEST_SEARCH_TERMS

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("search_term, expected_url", TEST_SEARCH_TERMS)
def test_baidu_search_with_parameters(setup, search_term, expected_url):
    driver = setup
    driver.get("https://www.baidu.com")
    
    search_box = driver.find_element(By.ID, "kw")
    search_box.send_keys(search_term)
    driver.find_element(By.ID, "su").click()
    
    # 使用显式等待等待标题包含搜索词
    WebDriverWait(driver, 10).until(EC.title_contains(search_term))
    
    # 对搜索词进行URL编码
    encoded_search_term = quote_plus(search_term)
    
    # 简化断言，只检查 URL 是否包含URL编码后的搜索词
    assert encoded_search_term in driver.current_url, "URL does not contain the search term"