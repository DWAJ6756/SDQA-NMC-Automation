from selenium.webdriver.common.by import By
from .base_page import BasePage
import time
from .navigation_page import NavigationPage
class ControlPage(BasePage):
    # Locators
    TURN_OFF_UPS = (By.XPATH, "//span[@id='langTurnUPSOff']")
    TURN_ON_UPS = (By.XPATH, "//span[@id='langTurnUPSOn']")
    SKIP_OUTLET_OFF_DELAYS = (By.XPATH, "//span[@id='langSkipOutletOffDelays']")
    SKIP_OUTLET_ON_DELAYS = (By.XPATH, "//span[@id='langSkipOutletOnDelays']")
    REBOOT_UPS = (By.XPATH, "//span[@id='langRebootUPS']")
    SLEEP_UPS = (By.XPATH, "//span[@id='langPutUPSToSleep']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@name='submit']")
    APPLY_BUTTON = (By.XPATH, "//input[@value='Apply']")
    NEXT_BUTTON = (By.CSS_SELECTOR, "input[value='Next ››']")
    MOG_STATUS = (By.XPATH, "//tbody/tr[2]/td[2]")
    SOG_STATUS=(By.XPATH,"//tbody/tr[3]/td[2]")
    STATUS=(By.XPATH, "//a[normalize-space()='Status']")
    STATUS_OUTLET_GROUPES=(By.XPATH, "//a[@href='ulstoutg.htm']")
    sleepTimeElement=(By.XPATH, "//input[@name='UpsSleepTime']")





    def turn_on_ups_without_delay(self):
        """Turn on UPS without delay"""
        self.click_element(*self.TURN_ON_UPS)
        self.click_element(*self.SKIP_OUTLET_ON_DELAYS)
        self.click_element(*self.NEXT_BUTTON)
        self.click_element(*self.APPLY_BUTTON)
        time.sleep(5)

    def turn_off_ups_with_delay(self):
        """Turn off UPS with delay"""
        self.click_element(*self.TURN_OFF_UPS)
        self.click_element(*self.SUBMIT_BUTTON)
        self.click_element(*self.APPLY_BUTTON)

    def turn_off_ups_without_delay(self):
        """Turn off UPS without delay"""
        self.click_element(*self.TURN_OFF_UPS)
        self.click_element(*self.SKIP_OUTLET_OFF_DELAYS)
        self.click_element(*self.SUBMIT_BUTTON)
        self.click_element(*self.APPLY_BUTTON)

    def turn_on_ups_with_delay(self):
        """Turn on UPS with delay"""
        self.click_element(*self.TURN_ON_UPS)
        self.click_element(*self.SUBMIT_BUTTON)
        self.click_element(*self.APPLY_BUTTON)

    def reboot_ups_without_delay(self):
        """Reboot UPS without delay"""
        self.click_element(*self.REBOOT_UPS)
        self.click_element(*self.SKIP_OUTLET_OFF_DELAYS)
        self.click_element(*self.SUBMIT_BUTTON)
        self.click_element(*self.APPLY_BUTTON)

    def reboot_ups_with_delay(self):
        """Reboot UPS with delay"""
        self.click_element(*self.REBOOT_UPS)
        self.click_element(*self.SUBMIT_BUTTON)
        self.click_element(*self.APPLY_BUTTON)

    def get_mogAndsog_status(self):
        """Get MOG status"""
        # return self.get_text(*self.MOG_STATUS)

        self.click_element(*self.STATUS)
        self.click_element(*self.STATUS_OUTLET_GROUPES)
        mog_state= self.get_text(*self.MOG_STATUS)
        sog_state=self.get_text(*self.SOG_STATUS)
        return(mog_state,sog_state)


    def get_sleep_time(self,driver):
        navigation=NavigationPage(driver)
        navigation.navigate_to_configuration_shutdown()
        return float(self.get_attribute(*self.sleepTimeElement))

    def put_ups_to_sleep(self,driver):
        navigation = NavigationPage(driver)
        navigation.navigate_to_control()
        self.click_element(*self.SLEEP_UPS)
        self.click_element(*self.SUBMIT_BUTTON)
        self.click_element(*self.APPLY_BUTTON)

    def put_ups_to_sleep_without_delay(self, driver):
        navigation = NavigationPage(driver)
        navigation.navigate_to_control()
        self.click_element(*self.SLEEP_UPS)
        self.click_element(*self.SKIP_OUTLET_OFF_DELAYS)
        self.click_element(*self.SUBMIT_BUTTON)
        self.click_element(*self.APPLY_BUTTON)




