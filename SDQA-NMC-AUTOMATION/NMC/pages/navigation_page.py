from selenium.webdriver.common.by import By
from .base_page import BasePage
import time


class NavigationPage(BasePage):
    # Navigation Menu Locators
    HOME_LINK = (By.XPATH, "//a[normalize-space()='Home']")
    ABOUT_LINK = (By.XPATH, "//a[normalize-space()='About']")
    STATUS_LINK = (By.XPATH, "//a[normalize-space()='Status']")
    CONTROL_LINK = (By.XPATH, "//a[normalize-space()='Control']")
    CONFIGURATION_LINK = (By.XPATH, "//a[@class='dropdown-toggle'][normalize-space()='Configuration']")

    # Sub-menu Locators
    ABOUT_UPS_LINK = (By.XPATH, "//a[@href='ulabout.htm']")
    UPS_STATUS_LINK = (By.XPATH, "//a[@href='ulstat.htm']")
    OUTLET_GROUPS_STATUS_LINK = (By.XPATH, "//a[@href='ulstoutg.htm']")
    UNIVERSAL_IO_STATUS_LINK = (By.XPATH, "//a[@href='uiostatus.htm']")
    OUTLET_GROUPS_CONTROL_LINK = (By.XPATH, "//a[@href='ulsogctl.htm']")
    UPS_CONTROL_LINK = (By.XPATH, "//a[@href='ulctrl.htm']")
    OUTLET_GROUPS_CONFIG_LINK = (By.XPATH, "//a[@href='uloutgrp.htm']")
    SHUTDOWN_CONFIG_LINK = (By.XPATH, "//a[normalize-space()='Shutdown']")

    def navigate_to_home(self):
        """Navigate to Home page"""
        self.click_element(*self.HOME_LINK)
        time.sleep(2)

    def navigate_to_about(self):
        """Navigate to About -> UPS page"""
        self.click_element(*self.ABOUT_LINK)
        self.click_element(*self.ABOUT_UPS_LINK)
        time.sleep(2)

    def navigate_to_status(self):
        """Navigate to Status -> UPS page"""
        self.click_element(*self.STATUS_LINK)
        self.click_element(*self.UPS_STATUS_LINK)
        time.sleep(2)

    def navigate_to_status_outlet_groups(self):
        """Navigate to Status -> Outlet Groups page"""
        self.click_element(*self.STATUS_LINK)
        self.click_element(*self.OUTLET_GROUPS_STATUS_LINK)
        time.sleep(2)

    def navigate_to_status_universalio(self):
        """Navigate to Status -> Universal IO page"""
        self.click_element(*self.STATUS_LINK)
        self.click_element(*self.UNIVERSAL_IO_STATUS_LINK)
        time.sleep(2)

    def navigate_to_control(self):
        """Navigate to Control -> UPS page"""
        self.click_element(*self.CONTROL_LINK)
        self.click_element(*self.UPS_CONTROL_LINK)
        time.sleep(2)

    def navigate_to_control_outlet_groups(self):
        """Navigate to Control -> Outlet Groups page"""
        self.click_element(*self.CONTROL_LINK)
        self.click_element(*self.OUTLET_GROUPS_CONTROL_LINK)
        time.sleep(2)

    def navigate_to_configuration(self):
        """Navigate to Configuration -> Outlet Groups page"""
        self.click_element(*self.CONFIGURATION_LINK)
        self.click_element(*self.OUTLET_GROUPS_CONFIG_LINK)
        time.sleep(2)

    def navigate_to_configuration_shutdown(self):
        """Navigate to Configuration -> Shutdown page"""
        self.click_element(*self.CONFIGURATION_LINK)
        self.click_element(*self.SHUTDOWN_CONFIG_LINK)
        time.sleep(2)

