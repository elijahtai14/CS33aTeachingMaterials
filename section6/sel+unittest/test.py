import unittest
from selenium import webdriver

browser = webdriver.Firefox()
path = "Users/apple/Desktop/CSE33A/CS33aTeachingMaterials/section6/sel+unittest/"
browser.get("file:///" +  path + "index.html")

class SwitchTest(unittest.TestCase):
    def test1(self):  
        """Title"""
        self.assertTrue("Some page" in browser.title)

    def test2(self):
        """Initializes to Off"""
        self.assertEqual(browser.find_element_by_id("label").text, "Off")

    def test2(self):
        """One click to On"""
        browser.find_element_by_id("switch").click()
        self.assertEqual(browser.find_element_by_id("label").text, "On")

    def test3(self):
        """Second click to Off """
        browser.find_element_by_id("switch").click()
        self.assertEqual(browser.find_element_by_id("label").text, "Off")
    
unittest.main()
        
