from ..pages.control_ups_page import ControlPage
import time


class UpsControlOperation:

    def turn_on_ups_without_delay(self, driver, simulator_setup, excel_handler, navigate_to_control):

        control_page = ControlPage(driver)
        control_page.turn_on_ups_without_delay()

        simulator_state = simulator_setup.UPSSystem_UnSwitchedOutletGroup_Status()
        print(simulator_state)
        mog_state, sog_state = control_page.get_mogAndsog_status()
        print(mog_state)

        if (mog_state == 'On' and "ON" in simulator_state):

            excel_handler.write_test_data(
                test_name='Turn On Without Delay',
                nmc_value=mog_state,
                simulator_value=simulator_state,
                operation_type='WRITE'
            )

        else:
            assert False, "Turn On UPS without delay Failure"

    def turn_off_ups_with_delay(self, driver, simulator_setup, excel_handler, request):

        delays = request.getfixturevalue('get_delays')
        total_delay = delays['main_power_off'] + delays['sog_power_off'] + 10

        control_page = ControlPage(driver)
        navigate_to_control = request.getfixturevalue('navigate_to_control')

        control_page.turn_off_ups_with_delay()
        time.sleep(total_delay)

        mog_state, sog_state = control_page.get_mogAndsog_status()

        simulator_status = simulator_setup.UPSSystem_UnSwitchedOutletGroup_Status()

        if (mog_state == 'Off' and "OFF" in simulator_status):
            excel_handler.write_test_data(
                test_name='Turn Off With Delay',
                nmc_value=mog_state,
                simulator_value=simulator_status,
                operation_type='WRITE'
            )
        else:
            assert False, "UPS TURN OFF WITH DELAY FAILURE"

    def turn_off_ups_without_delay(self, driver, simulator_setup, excel_handler, request):
        """Test turning off UPS without delay"""
        delays = request.getfixturevalue('get_delays')
        total_delay = delays['main_power_off'] + delays['sog_power_off'] + 10

        control_page = ControlPage(driver)
        navigate_to_control = request.getfixturevalue('navigate_to_control')

        control_page.turn_off_ups_without_delay()
        time.sleep(total_delay)

        mog_state, sog_state = control_page.get_mogAndsog_status()

        simulator_status = simulator_setup.UPSSystem_UnSwitchedOutletGroup_Status()

        if (mog_state == 'Off' and "OFF" in simulator_status):

            excel_handler.write_test_data(
                test_name='Turn Off Without Delay',
                nmc_value=mog_state,
                simulator_value=simulator_status,
                operation_type='WRITE'
            )

        else:
            assert False, "UPS TURN OFF WITH DELAY FAILURE"

    def turn_on_ups_with_delay(self, driver, simulator_setup, excel_handler, request):

        delays = request.getfixturevalue('get_delays')
        total_delay = delays['main_power_on'] + 5

        control_page = ControlPage(driver)
        navigate_to_control = request.getfixturevalue('navigate_to_control')

        control_page.turn_on_ups_with_delay()
        time.sleep(total_delay)

        mog_state, sog_state = control_page.get_mogAndsog_status()

        simulator_value = simulator_setup.UPSSystem_UnSwitchedOutletGroup_Status()

        if (mog_state == 'On' and "ON" in simulator_value):
            excel_handler.write_test_data(
                test_name='Turn On With Delay',
                nmc_value=mog_state,
                simulator_value=simulator_value,
                operation_type='WRITE'
            )

    def reboot_ups_without_delay(self, driver, simulator_setup, excel_handler, request):

        navigate_to_MogSogstatus = request.getfixturevalue('navigate_toFetchMogAndSog')
        mog_state, sog_state = navigate_to_MogSogstatus

        if (mog_state != 'Off' and sog_state != 'Off'):

            delays = request.getfixturevalue('get_delays')

            mainOutletpowerOffDelay = delays['main_power_off']

            mainOutletRebootDuration = delays['reboot_duration']

            mainOutletpowerOnDelay = delays['main_power_on']

            sogOutletPowerOffDelay = delays['sog_power_off']

            sogOutletPowerOnDelay = delays['sog_power_on']

            delay = int(sogOutletPowerOffDelay) + int(mainOutletpowerOffDelay) + 2

            total_delay = int(mainOutletRebootDuration) + int(mainOutletpowerOnDelay) + int(sogOutletPowerOnDelay) + 5

            control_page = ControlPage(driver)
            navigate_to_control = request.getfixturevalue('navigate_to_control')

            control_page.reboot_ups_without_delay()
            time.sleep(2)

            mog_state, sog_state = control_page.get_mogAndsog_status()

            simulator_value = simulator_setup.UPSSystem_UnSwitchedOutletGroup_Status()

            if "Off" in mog_state and "Off" in sog_state and "OFF" in simulator_value:
                time.sleep(total_delay)

                mog_state, sog_state = control_page.get_mogAndsog_status()

                simulator_value1 = simulator_setup.UPSSystem_SwitchedOutletGroup1_Status()

                print(simulator_value1)
                if "On" in mog_state and "ON" in simulator_value1 and "On" in sog_state:
                    excel_handler.write_test_data(
                        test_name='Reboot Without Delay',
                        nmc_value=mog_state,
                        simulator_value=simulator_value,
                        operation_type='WRITE'
                    )

                else:
                    assert False, "Reboot Failed-EITHER MOG/SOG/SIMULATOR Value in Off"

            else:
                assert False, "Reboot Failed-EITHER MOG/SOG/SIMULATOR Value in ON"
        else:
            assert False, "Reboot Failed, MOG AND SOG state if off"

    def reboot_ups_with_delay(self, driver, simulator_setup, excel_handler, request):
        navigate_to_MogSogstatus = request.getfixturevalue('navigate_toFetchMogAndSog')
        mog_state, sog_state = navigate_to_MogSogstatus

        if (mog_state != 'Off' and sog_state != 'Off'):

            delays = request.getfixturevalue('get_delays')

            mainOutletpowerOffDelay = delays['main_power_off']

            mainOutletRebootDuration = delays['reboot_duration']

            mainOutletpowerOnDelay = delays['main_power_on']

            sogOutletPowerOffDelay = delays['sog_power_off']

            sogOutletPowerOnDelay = delays['sog_power_on']

            delay = int(sogOutletPowerOffDelay) + int(mainOutletpowerOffDelay) + 2

            total_delay = int(mainOutletRebootDuration) + int(mainOutletpowerOnDelay) + int(sogOutletPowerOnDelay) + 5

            control_page = ControlPage(driver)
            navigate_to_control = request.getfixturevalue('navigate_to_control')

            control_page.reboot_ups_with_delay()
            time.sleep(delay)

            mog_state, sog_state = control_page.get_mogAndsog_status()

            simulator_value = simulator_setup.UPSSystem_UnSwitchedOutletGroup_Status()

            if "Off" in mog_state and "Off" in sog_state and "OFF" in simulator_value:
                time.sleep(total_delay)

                mog_state, sog_state = control_page.get_mogAndsog_status()

                simulator_value1 = simulator_setup.UPSSystem_SwitchedOutletGroup1_Status()

                print(simulator_value1)
                if "On" in mog_state and "ON" in simulator_value1 and "On" in sog_state:
                    excel_handler.write_test_data(
                        test_name='Reboot Without Delay',
                        nmc_value=mog_state,
                        simulator_value=simulator_value,
                        operation_type='WRITE'
                    )

                else:
                    assert False, "Reboot Failed-EITHER MOG/SOG/SIMULATOR Value in Off"

            else:
                assert False, "Reboot Failed-EITHER MOG/SOG/SIMULATOR Value in ON"
        else:
            assert False, "Reboot Failed, MOG AND SOG state if off"


    def sleep_ups_with_delay(self,driver, simulator_setup, excel_handler, request):

        control_page = ControlPage(driver)
        mog_state, sog_state = control_page.get_mogAndsog_status()

        if (mog_state != 'Off' and sog_state != 'Off'):

            delays = request.getfixturevalue('get_delays')
            power_off_delay = int(delays['main_power_off']) + int(delays['sog_power_off']) + 5

            # Get sleep time from configuration
            navigate_configuration_shutdown = request.getfixturevalue('navigate_configuration_shutdown')
            sleep_time = control_page.get_sleep_time(driver)
            total_delay = (sleep_time * 3600.0) + float(delays['main_power_on']) + float(delays['sog_power_on']) + 5.0

            # Execute sleep operation
            navigate_to_control = request.getfixturevalue('navigate_to_control')
            control_page.put_ups_to_sleep(driver)

            # First check - should be OFF
            time.sleep(power_off_delay)
            mog_state, sog_state = control_page.get_mogAndsog_status()
            simulator_value = simulator_setup.UPSSystem_UnSwitchedOutletGroup_Status()

            if "OFF" in simulator_value and "Off" in mog_state and "Off" in sog_state:

                time.sleep(total_delay)
                simulator_value1 = simulator_setup.UPSSystem_SwitchedOutletGroup1_Status()
                mog_state, sog_state = control_page.get_mogAndsog_status()

                if "ON" in simulator_value1 and "On" in mog_state and "On" in sog_state:
                    excel_handler.write_test_data(test_name='Sleep With Delay', nmc_value=mog_state,simulator_value=simulator_value, operation_type='WRITE')
                else:
                    assert False, "Sleep with Delay Failure, Either mog and sog state is off"
            else:
                assert  False,"Sleep with Delay Failure, Either mog and sog state is On"


        else:
            assert False,"Sleep With Delay Failure,MOGN AND SOG STATE IS OFF"


    def sleep_ups_without_delay(self,driver, simulator_setup, excel_handler, request):

        control_page = ControlPage(driver)
        mog_state, sog_state = control_page.get_mogAndsog_status()

        if (mog_state != 'Off' and sog_state != 'Off'):

            delays = request.getfixturevalue('get_delays')
            navigate_configuration_shutdown = request.getfixturevalue('navigate_configuration_shutdown')
            sleep_time = control_page.get_sleep_time(driver)
            total_delay = (sleep_time * 3600.0) + float(delays['main_power_on']) + float(delays['sog_power_on']) + 5.0

            # Execute sleep operation
            navigate_to_control = request.getfixturevalue('navigate_to_control')
            control_page.put_ups_to_sleep_without_delay(driver)
            # minimum reboot duration is = 4 min
            time.sleep(3)
            mog_state, sog_state = control_page.get_mogAndsog_status()
            simulator_value = simulator_setup.UPSSystem_UnSwitchedOutletGroup_Status()

            if "OFF" in simulator_value and "Off" in mog_state and "Off" in sog_state:

                time.sleep(total_delay)
                simulator_value1 = simulator_setup.UPSSystem_SwitchedOutletGroup1_Status()
                mog_state, sog_state = control_page.get_mogAndsog_status()

                if "ON" in simulator_value1 and "On" in mog_state and "On" in sog_state:
                    excel_handler.write_test_data(test_name='Sleep With Delay', nmc_value=mog_state,simulator_value=simulator_value, operation_type='WRITE')
                else:
                    assert False, "Sleep with Delay Failure, Either mog and sog state is off"
            else:
                assert  False,"Sleep with Delay Failure, Either mog and sog state is On"


        else:
            assert False,"Sleep With Delay Failure,MOGN AND SOG STATE IS OFF"

