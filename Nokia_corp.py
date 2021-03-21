import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

    # locate 1st link to go to Nokia Corp

    # locate About for click

    # locate
    # No need to hit submit search button, bucase '\n' at end of SEARCH_TERM meaning hit ENTER button
#    SEARCH_SUBMIT_BUTTON=(By.XPATH, "//*[@id='tsf']/div[1]/div[1]/div[2]/button/div/span/svg")

    # First result link from google
    FIRSTR_RESULT_LINK = (By.XPATH, "//div[@id='search']")
    # --- Search Results Page Locators ---
    SEARCH_RESULT_LINK=(By.XPATH, "(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[2]")

    # --- Product Details Page Locators ---
    ADD_TO_CART_BUTTON=(By.ID, "add-to-cart-button")

    # --- Sub Cart Page Locators ---
    SUB_CART_DIV=(By.ID,"hlb-subcart")
    PROCEED_TO_BUY_BUTTON=(By.ID,"hlb-ptc-btn-native")
    CART_COUNT=(By.ID,"nav-cart-count")
    CART_LINK=(By.ID,"nav-cart")

    # --- Cart Page Locators ---
    DELETE_ITEM_LINK=(By.XPATH,"//div[contains(@class,'a-row sc-action-links')]//span[contains(@class,'sc-action-delete')]")
    CART_COUNT=(By.ID,'nav-cart-count')
    PROCEED_TO_CHECKOUT_BUTTON=(By.NAME,"proceedToCheckout")
    # --- Signin Page Locators ---
    USER_EMAIL_OR_MOBIL_NO_TEXTBOX=(By.ID,"ap_email")


class BasePage():
    """This class is the parent class for all the pages in our application."""
    """It contains all common elements and functionalities available to all pages."""

    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver=driver

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        web_element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self,by_locator):
        element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

class HomePage(BasePage):
    """Home Page of Amazon India"""
    def __init__(self, driver):
        super().__init__(driver)
        # 1. open webpage
        self.driver.get(TestData.BASE_URL)
        self.metric = {}


    def fetchData(self):
        ####
        self.driver.find_element()
        #At COmpany page, retrieve metrics
        #at_a_glance_key = self.driver.find_elements(By.CLASS_NAME, 'nc-4') and self.driver.find_elements(By.TAG_NAME, 'p')
        #at_a_glance_value = self.driver.find_elements(By.CLASS_NAME, 'nc-4') and self.driver.find_elements(By.TAG_NAME, 'h2')

        #Create list and dictionary for search
        #key =[]
        #value = []
        #i = 7

        #while (i < 13):
        #    key.append(at_a_glance_key[i].text)
        #    i+=1


        #j = 3
        #while (j<9):
        #    value.append(at_a_glance_value[j].text)
        #    j+=1


        #metric = {key[i]: value[i] for i in range(len(key))}
        #self.metric = metric

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

    def Nokia_find_data(self):
        # 2. find search box
        self.driver.find_element(*Locators.SEARCH_TEXTBOX).clear()
        # 3. input Nokia Corp and hit Enter button
        self.enter_text(Locators.SEARCH_TEXTBOX, TestData.SEARCH_TERM)
        # 4. open 1st link
        self.click(Locators.FIRSTR_RESULT_LINK)
        # 5. hit About us
        # 6. click company
        # 7. locate metrics and store to dict
        self.fetchData()
        self.searchData()
        # return dict

#entry point
def main():
    HomePage(webdriver.Chrome()).Nokia_find_data()
    time.sleep(5)

if __name__ == "__main__":
    main()





#class SearchResultsPage(BasePage):
#    """Search Results Page of Amazon India"""
#    def __init__(self, driver):
#        super().__init__(driver)
#
#    def click_search_result(self):
#        self.click(Locators.SEARCH_RESULT_LINK)
#
#class ProductDetailsPage(BasePage):
#    """Product Details Page for the clicked product on Amazon India"""
#    def __init__(self,driver):
#        super().__init__(driver)
#
#    def click_add_to_cart_button(self):
#        self.click(Locators.ADD_TO_CART_BUTTON)
#
#class SubCartPage(BasePage):
#    """Sub Cart Page on Amazon India"""
#    def __init__(self,driver):
#        super().__init__(driver)
#
#    def click_cart_link(self):
#        self.click(Locators.CART_LINK)
#
#class CartPage(BasePage):
#    """Cart Page on Amazon India"""
#    def __init__(self,driver):
#        super().__init__(driver)
#
#    def delete_item(self):
#        cartCount=int(self.driver.find_element(*Locators.CART_COUNT).text)
#        # print ("Cart Count is"+ str(cartCount))
#        if(cartCount<1):
#            print("Cart is empty")
#            exit()
#        if(self.driver.title.startswith("Amazon.in Shopping Cart")):
#            #to delete an item from the Cart
#            self.click(Locators.DELETE_ITEM_LINK)
#            time.sleep(2)
#
#    def click_proceed_to_checkout_button(self):
#        self.click(Locators.PROCEED_TO_CHECKOUT_BUTTON)
#
#class SignInPage(BasePage):
#    """SignIn Page on Amazon India"""
#    def __init__(self,driver):
#        super().__init__(driver)
#

