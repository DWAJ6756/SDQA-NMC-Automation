from selenium.webdriver.common.by import By
from .base_page import BasePage

class AboutPage(BasePage):
    # Locators
    UPS_SKU_NUMBER = (By.XPATH, "/html/body/div[5]/div[2]/div/div[2]/div[2]")
    SERIAL_VERSION = (By.CSS_SELECTOR, "body > div:nth-child(7) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2)")
    FIRMWARE_VERSION = (By.CSS_SELECTOR, "body > div:nth-child(7) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2)")
    MANUFACTURE_DATE = (By.CSS_SELECTOR, "body > div:nth-child(7) > div:nth-child(2) > div:nth-child(1) > div:nth-child(5) > div:nth-child(2)")
    APPARENT_POWER = (By.XPATH, "//div[@class='container']//div[6]//div[2]")
    REAL_POWER = (By.XPATH, "//div[@class='container']//div[6]//div[2]")
    BATTERY_SKU = (By.XPATH, "/html/body/div[5]/div[2]/div/div[8]/div[2]")

    def get_ups_sku_number(self):
        return self.get_text(*self.UPS_SKU_NUMBER)

    def get_serial_version(self):
        return self.get_text(*self.SERIAL_VERSION)

    def get_firmware_version(self):
        return self.get_text(*self.FIRMWARE_VERSION)

    def get_manufacture_date(self):
        return self.get_text(*self.MANUFACTURE_DATE)

    def get_apparent_power(self):
        return self.get_text(*self.APPARENT_POWER)

    def get_real_power(self):
        return self.get_text(*self.REAL_POWER)

    def get_battery_sku(self):
        return self.get_text(*self.BATTERY_SKU)