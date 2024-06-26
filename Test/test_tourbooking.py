# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTourbooking():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tourbooking(self):
    self.driver.get("http://localhost/SE%20Hotel%20Management%20Part/home.php")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3)").click()
    self.driver.find_element(By.LINK_TEXT, "Tour").click()
    self.driver.find_element(By.CSS_SELECTOR, ".navbar > a:nth-child(4)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".box:nth-child(5) .btn").click()
    self.driver.find_element(By.NAME, "name").click()
    self.driver.find_element(By.NAME, "name").send_keys("Vibhansh")
    self.driver.find_element(By.NAME, "phone").click()
    self.driver.find_element(By.NAME, "phone").send_keys("8000443641")
    self.driver.find_element(By.NAME, "location").click()
    self.driver.find_element(By.NAME, "location").send_keys("Rome")
    self.driver.find_element(By.NAME, "arrivals").click()
    self.driver.find_element(By.NAME, "arrivals").click()
    self.driver.find_element(By.NAME, "arrivals").send_keys("2024-05-07")
    self.driver.find_element(By.NAME, "leaving").click()
    self.driver.find_element(By.NAME, "leaving").send_keys("2024-05-09")
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("vibhansh@gmail.com")
    self.driver.find_element(By.NAME, "address").click()
    self.driver.find_element(By.NAME, "address").send_keys("Diu")
    self.driver.find_element(By.NAME, "guests").click()
    self.driver.find_element(By.NAME, "guests").send_keys("3")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
  
