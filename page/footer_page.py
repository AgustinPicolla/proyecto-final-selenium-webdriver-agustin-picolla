from selenium.webdriver.common.by import By

class FooterPage:

    def __init__(self, driver):
        self.driver = driver
        self.twitter_btn = (By.CLASS_NAME, "social_twitter")   # <a class="social_twitter"></a>

    def click_twitter(self):
        self.driver.find_element(*self.twitter_btn).click()
