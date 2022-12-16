from __future__ import annotations

import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_leter(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")
        inputbox.send_keys("Buy feather")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = self.browser.find_elements(By.TAG_NAME, "tr")
        self.assertIn("1:Buy feather", [row.text for row in rows])
        self.fail("Test was ended!")


if __name__ == "__main__":
    unittest.main(warnings="ignore")
