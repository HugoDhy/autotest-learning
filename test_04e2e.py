import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://jsonplaceholder.typicode.com/users")
    yield driver
    driver.quit()

def test_create_user():
    data = {"name": "Test User", "username": "testuser", "email": "test@example.com"}
    response = requests.post("https://jsonplaceholder.typicode.com/users", json=data)
    user_id = response.json()["id"]
    assert response.status_code == 201
    return user_id

def test_web_check_user(driver):
    driver.get("https://jsonplaceholder.typicode.com/users")
    # 假设页面显示用户列表，检查是否存在 "Test User"
    assert "Test User" in driver.page_source

def test_delete_user(driver, user_id):
    response = requests.delete(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    assert response.status_code == 200