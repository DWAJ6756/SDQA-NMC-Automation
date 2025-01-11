import pytest
from ..pages.about_page import AboutPage


@pytest.mark.system
class TestSystemInformation:
    def test_ups_sku_number(self, driver, simulator_setup, excel_handler, navigate_to_about_ups):
        """Test UPS SKU number information"""
        about_page = AboutPage(driver)

        nmc_sku_number = about_page.get_ups_sku_number()
        simulator_sku_number = simulator_setup.UPSSKU_STR()

        excel_handler.write_test_data(test_name='UPS SKU NUMBER', nmc_value=nmc_sku_number,simulator_value=simulator_sku_number, operation_type="READ")

    def test_ups_serial_version(self, driver, simulator_setup, excel_handler, navigate_to_about_ups):
        """Test UPS serial version information"""
        about_page = AboutPage(driver)

        serial_version = about_page.get_serial_version()
        simulator_serial = simulator_setup.SerialNumber_STR()
        excel_handler.write_test_data(test_name='UPS SERIAL VERSION', nmc_value=serial_version,simulator_value=simulator_serial, operation_type="READ")

    def test_ups_firmware_version(self, driver, simulator_setup, excel_handler, navigate_to_about_ups):
        """Test UPS firmware version information"""

        about_page = AboutPage(driver)

        firmware_version = about_page.get_firmware_version()
        simulator_firmware = simulator_setup.UPSSystem_SmartSlotHWversion()

        excel_handler.write_test_data(test_name='UPS FIRMWARE VERSION', nmc_value=firmware_version,simulator_value=simulator_firmware, operation_type="READ")

    def test_ups_manufacture_date(self, driver, simulator_setup, excel_handler, navigate_to_about_ups):
        """Test UPS manufacture date information"""
        about_page = AboutPage(driver)

        manufacture_date = about_page.get_manufacture_date()
        simulator_date = simulator_setup.ManufactureDate()

        excel_handler.write_test_data(test_name='UPS MANUFACTURE DATE', nmc_value=manufacture_date,simulator_value=simulator_date, operation_type="READ")

    def test_ups_apparent_power_ratings(self, driver, simulator_setup, excel_handler, navigate_to_about_ups):
        """Test UPS power ratings information"""
        about_page = AboutPage(driver)

        # Test apparent power
        apparent_power = about_page.get_apparent_power()

        excel_handler.write_test_data(test_name='UPS APPARENT POWER', nmc_value=apparent_power,simulator_value="simulator_power", operation_type="READ")

        # Test real power rating
        real_power = about_page.get_real_power()
        simulator_real_power = simulator_setup.Output_Rated_RealPower()

        excel_handler.write_test_data(test_name='UPS REAL POWER RATING', nmc_value=real_power,simulator_value=simulator_real_power, operation_type='READ')

    def test_ups_battery_sku(self, driver, simulator_setup, excel_handler, navigate_to_about_ups):
        """Test UPS battery SKU information"""
        about_page = AboutPage(driver)

        battery_sku = about_page.get_battery_sku()
        simulator_battery_sku = simulator_setup.UPSBatterySKU()

        excel_handler.write_test_data(test_name='UPS BATTERY SKU', nmc_value=battery_sku,simulator_value=simulator_battery_sku, operation_type='READ')
