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

class TestAboutus():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_aboutus(self):
    self.driver.get("http://localhost/SE%20Hotel%20Management%20Part/home.php")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.LINK_TEXT, "About Us").click()
    self.driver.find_element(By.CSS_SELECTOR, ".box:nth-child(1) > a:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".navbar > a:nth-child(1)").click()
  