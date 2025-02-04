from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 初始化浏览器驱动
driver = webdriver.Chrome()

# 打开百度首页
driver.get("https://www.baidu.com")

# 定位搜索框并输入关键词
search_box = driver.find_element(By.ID, "kw")
search_box.send_keys("软件测试")

# 定位搜索按钮并点击
search_button = driver.find_element(By.ID, "su")
search_button.click()

# 等待2秒，查看结果
time.sleep(2)

# 打印当前页面标题
print("页面标题：", driver.title)

# 关闭浏览器
driver.quit()
