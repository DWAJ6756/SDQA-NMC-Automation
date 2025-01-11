import pytest
from ...pages.control_ups_page import ControlPage
import time
from ...library.control_ups_operation import UpsControlOperation



@pytest.mark.control
class TestUPSControlOperations:

    def test_turn_off_ups_with_delay(self, driver, simulator_setup, excel_handler, request):
        control_operation = UpsControlOperation()
        control_operation.turn_off_ups_with_delay(driver, simulator_setup, excel_handler, request)

    def test_turn_on_ups_without_delay(self, driver, simulator_setup, excel_handler, navigate_to_control):
        """Test turning on UPS without delay"""
        control_operation=UpsControlOperation()
        control_operation.turn_on_ups_without_delay(driver, simulator_setup, excel_handler, navigate_to_control)



    def test_turn_off_ups_without_delay(self, driver, simulator_setup, excel_handler, request):
        control_operation = UpsControlOperation()
        control_operation.turn_off_ups_without_delay(driver, simulator_setup, excel_handler, request)



    def test_turn_on_ups_with_delay(self, driver, simulator_setup, excel_handler, request):
        """Test turning on UPS with delay"""

        control_operation = UpsControlOperation()
        control_operation.turn_on_ups_with_delay(driver, simulator_setup, excel_handler, request)



    def test_reboot_ups_without_delay(self, driver, simulator_setup, excel_handler, request):
        control_operation = UpsControlOperation()
        control_operation.reboot_ups_without_delay(driver, simulator_setup, excel_handler, request)



    def test_reboot_ups_with_delay(self, driver, simulator_setup, excel_handler, request):
        """Test rebooting UPS with delay"""
        control_operation = UpsControlOperation()
        control_operation.reboot_ups_with_delay(driver, simulator_setup, excel_handler, request)


    def test_ups_sleep_with_delay(self, driver, simulator_setup, excel_handler, request):
        control_operation = UpsControlOperation()
        control_operation.sleep_ups_with_delay(driver, simulator_setup, excel_handler, request)


    def test_ups_sleep_without_delay(self, driver, simulator_setup, excel_handler, request):
        control_operation = UpsControlOperation()
        control_operation.sleep_ups_without_delay(driver, simulator_setup, excel_handler, request)


