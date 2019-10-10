import unittest
from appium import webdriver
import base64
import os
import time
from appium.webdriver.common.touch_action import TouchAction


class AddContactTest(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            "platformName": "Android",
            "deviceName": "Android Emulator",
            "appPackage": "com.android.contacts",
            "appActivity": "com.android.contacts.activities.PeopleActivity",
            "newcommandTimeout": 600
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(20)
        self.driver.start_recording_screen()

    def testAddContact(self):
        driver = self.driver
        user_action = TouchAction(driver)

        user_action.tap(x=960, y=1676).perform()

        driver.find_element_by_id("com.android.contacts:id/left_button").click()
        time.sleep(3)

        #driver.find_element_by_xpath("//android.widget.TextView[@text = 'More fields']").click()
        #driver.implicitly_wait(20)

        driver.implicitly_wait(20)
        firstname = driver.find_element_by_xpath("//android.widget.EditText[@text = 'First name']")
        firstname.send_keys("Olka")
        time.sleep(3)
        user_action.long_press(firstname, duration=3000).perform()
        driver.hide_keyboard()
        driver.find_element_by_xpath("//android.widget.EditText[@text ='Last name']").click()
        driver.find_element_by_xpath("//android.widget.EditText[@text ='Last name']").send_keys("Ko")
        driver.hide_keyboard()
        driver.implicitly_wait(200)

        for i in range(3):
            time.sleep(10)
            user_action.press(x=521, y=1521).move_to(x=517, y=752).release().perform()
            time.sleep(10)

        driver.find_element_by_xpath("//android.widget.EditText[@text = 'Phone']").click()
        driver.find_element_by_xpath("//android.widget.EditText[@text = 'Phone']").send_keys("6475210000")
        driver.hide_keyboard()
        driver.implicitly_wait(100)

        driver.find_element_by_xpath("//android.widget.TextView[@text = 'Mobile']").click()
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("//android.widget.CheckedTextView[@text = 'Mobile']").click()
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("//android.widget.EditText[@text = 'Email']").click()
        driver.find_element_by_xpath("//android.widget.EditText[@text = 'Email']").send_keys("butafor@gmail.com")
        driver.implicitly_wait(100)

        driver.find_element_by_id("com.android.contacts:id/editor_menu_save_button").click()

    def tearDown(self):
        video_rawdata = self.driver.stop_recording_screen()
        video_name = self.driver.current_activity + time.strftime("%y_%m_%d_%H%M%S")
        filepath = os.path.join("D:/Olga/PycharmProjects/Appium1/venv/NewFunc/Video/", video_name + ".mp4")
        with open(filepath, "wb") as vd:
            vd.write(base64.b64decode(video_rawdata))
        # self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

