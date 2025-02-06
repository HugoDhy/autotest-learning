import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException  # 确保正确导入NoSuchElementException

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/login")
    yield driver
    driver.quit()

@pytest.mark.parametrize("username, password, expected_url, expected_message", [
    ("testuser", "Password123!", "https://demoqa.com/profile", ""),
    ("wrong_user", "wrong_password", "https://demoqa.com/login", "Invalid username or password"),
    ("testuser", "", "https://demoqa.com/login", ""),
    ("", "Password123!", "https://demoqa.com/login", "")
])
def test_login(setup, username, password, expected_url, expected_message):
    driver = setup
    driver.find_element(By.ID, "userName").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login").click()
    
    # 使用显式等待确保页面已经跳转
    WebDriverWait(driver, 10).until(EC.url_contains(expected_url.split("://")[-1]))
    
    assert "profile" in driver.current_url if "profile" in expected_url else not "profile" in driver.current_url, \
        f"Expected URL to contain 'profile' is {expected_url}, but got {driver.current_url}"

    if expected_message:
        error_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "name"))
        )
        error_message = error_element.text
        assert expected_message in error_message
    else:
        # 如果期望结果中没有错误消息，则验证页面上没有错误消息显示
        try:
            error_element = driver.find_element(By.ID, "name")
            assert not error_element.is_displayed(), "Error message is displayed unexpectedly"
        except NoSuchElementException:
            pass  # 如果找不到错误消息元素，说明没有显示错误消息，符合预期
