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

class TestRoombooking():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_roombooking(self):
    self.driver.get("http://localhost/SE%20Hotel%20Management%20Part/home.php")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.LINK_TEXT, "Rooms").click()
    self.driver.find_element(By.CSS_SELECTOR, ".roombox:nth-child(3) .btn").click()
    self.driver.find_element(By.NAME, "Name").click()
    self.driver.find_element(By.NAME, "Name").send_keys("Vibhansh")
    self.driver.find_element(By.NAME, "Email").click()
    self.driver.find_element(By.NAME, "Email").send_keys("vibhansh@gmail.com")
    self.driver.find_element(By.NAME, "Country").click()
    dropdown = self.driver.find_element(By.NAME, "Country")
    dropdown.find_element(By.XPATH, "//option[. = 'India']").click()
    self.driver.find_element(By.NAME, "Phone").click()
    self.driver.find_element(By.NAME, "Phone").send_keys("81515999521")
    self.driver.find_element(By.NAME, "RoomType").click()
    dropdown = self.driver.find_element(By.NAME, "RoomType")
    dropdown.find_element(By.XPATH, "//option[. = 'SUPERIOR ROOM']").click()
    self.driver.find_element(By.NAME, "Bed").click()
    dropdown = self.driver.find_element(By.NAME, "Bed")
    dropdown.find_element(By.XPATH, "//option[. = 'Double']").click()
    self.driver.find_element(By.NAME, "NoofRoom").click()
    dropdown = self.driver.find_element(By.NAME, "NoofRoom")
    dropdown.find_element(By.XPATH, "//option[. = '1']").click()
    self.driver.find_element(By.NAME, "Meal").click()
    dropdown = self.driver.find_element(By.NAME, "Meal")
    dropdown.find_element(By.XPATH, "//option[. = 'Half Board']").click()
    element = self.driver.find_element(By.NAME, "cin")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.NAME, "cin")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.NAME, "cin")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.NAME, "cin").click()
    self.driver.find_element(By.NAME, "cin").click()
    self.driver.find_element(By.NAME, "cin").send_keys("2024-04-26")
    self.driver.find_element(By.NAME, "cout").click()
    self.driver.find_element(By.NAME, "cout").send_keys("2024-05-01")
    self.driver.find_element(By.CSS_SELECTOR, ".reservationinfo").click()
    self.driver.find_element(By.NAME, "guestdetailsubmit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".swal-button").click()
  
