
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchWindowException


#from Resources.Locators import Locators
#from Resources.TestData import TestData
# TestData Locatiors BasePage HomePage
# HomePage is child class of BasePage

class TestData():
    #CHROME_EXECUTABLE_PATH="/opt/anaconda3/bin/chromedriver"
    BASE_URL = "https://www.google.com"
    SEARCH_TERM = "Nokia Corporation\n"

    #NO_RESULTS_TEXT = "No results found."

class Locators():
    # --- Home Page Locators ---
    # Goold search box
    SEARCH_TEXTBOX=(By.NAME,'q')
    # Nevigate to Nokia home page (first link)
    NOKIA_HOME = (By.TAG_NAME,"h3")
    # Find About us
    ABOUT_US = (By.XPATH,"/html/body/div[2]/div/header/div/div[1]/nav/div/div[2]/ul/li[4]")
    # Go to dropdown - 'Company'
    COMPANY = (By.XPATH, "/html/body/div[2]/div/header/div/div[1]/nav/div/div[2]/ul/li[4]/div/ul/li/ul/li[1]/a")
    GLANCE_CLASS = 'nc-4'
    GLANCE_KEY_TAG = 'p'
    GLANCE_VALUE_TAG = 'h2'



class Base():
    """This class is the parent class for all the pages"""
    """It contains all actions we need to take"""

    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver=driver

    # Perform click on web element whose locator is passed to it.
    def click(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        except NoSuchWindowException:
            print("Wrong value on Locators!")
        except TimeoutException:
            print("Taking too much time to load! Please retry")
        except ElementNotInteractableException:
            print("Resource not found!)")

    # Perform text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except NoSuchWindowException:
            print("Wrong value on Locators!")
        except TimeoutException:
            print("Taking too much time to load! Please retry")
        except ElementNotInteractableException:
            print("Resource not found!)")


    # Retrieve metric under At a glance and convert to dictionary
    def fetchData(self, by_class, by_tag, by_tag1):
        at_a_glance_key = self.driver.find_elements(By.CLASS_NAME, by_class) and self.driver.find_elements(By.TAG_NAME, by_tag)
        at_a_glance_value = self.driver.find_elements(By.CLASS_NAME, by_class) and self.driver.find_elements(By.TAG_NAME, by_tag1)
        list_key = []
        list_value = []
        i = 7
        while (i < 13):
            list_key.append(at_a_glance_key[i].text)
            i += 1
        j = 3
        while (j < 9):
            list_value.append(at_a_glance_value[j].text)
            j += 1
            metric = {list_key[i]: list_value[i] for i in range(len(list_key))}
            self.metric = metric
     # Serach key and retru value
    def searchData(self):
        while True:
            metric_retrieved = str(input('Please enter the value you want to check or choose from the list: '))
            if metric_retrieved in self.metric:
                print(self.metric[metric_retrieved])
                retry = str(input('Do you want to try another one? Enter Yes or No please: '))
                if retry == 'Yes':
                    True
                else:
                    break
            else:
                retry = str(input('Wrong value. Do you want to try another one? Enter Yes or No please: '))
                if retry == 'Yes':
                    True
                else:
                    break

class Home(Base):
    """Home Page of Amazon India"""
    def __init__(self, driver):
        super().__init__(driver)
        # 1. open webpage
        self.driver.get(TestData.BASE_URL)
        self.metric = {}


    def Nokia_find_data(self):
        # 2. find search box
        self.driver.find_element(*Locators.SEARCH_TEXTBOX).clear()
        # 3. input Nokia Corp and hit Enter button
        self.enter_text(Locators.SEARCH_TEXTBOX, TestData.SEARCH_TERM)
        # 4. open 1st link
        self.click(Locators.NOKIA_HOME)
        # 5. hit About us
        self.click(Locators.ABOUT_US)
        # 6. click company
        self.click(Locators.COMPANY)
        # 7. locate metrics and store to dict
        self.fetchData(Locators.GLANCE_CLASS,Locators.GLANCE_KEY_TAG, Locators.GLANCE_VALUE_TAG)
        self.searchData()
        # return dict
        self.driver.close()


#entry point
def main():
    Home(webdriver.Chrome()).Nokia_find_data()


if __name__ == "__main__":
    main()

