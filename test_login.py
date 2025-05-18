from selenium import webdriver
from selenium.webdriver.common.by import By

def test_example_login():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")
    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "password").send_keys("testpass")
    driver.find_element(By.ID, "loginBtn").click()
    assert "Dashboard" in driver.title
    driver.quit()
