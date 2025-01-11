
UPS_Status = ['NA', 'Informational Alert', 'High Efficiency', 'NA', 'NA', 'NA', 'Pending Output OFF', 'Pending Output ON', 'Test in Progress', 'Input Bad', 'Fault', 'State Output OFF', 'NA', 'State On Battery', 'State Online', 'Deprecated_StatusChange']
Battery_test_IntervalSetting = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "On Start up and every 14 days since", "On Start ups and every 7 days since", "On Start up plus 14 days", "On Start up plus 7 days", "On Start up only", "Never"]
Battery_LifeTime_Status = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "Life Time Exceeded Acknowledged", "Life Time Near End Acknowledged", "Life Time Exceeded", "Life Time Near End", "Life Time Status OK"]
Battery_ReplaceTest_Status = ["NA", "NA", "NA", "NA", "State Of Charge Not Acceptable", "Internal Fault", "Invalid State", "Internal", "Local User", "Deprecated_Protocol", "Aborted", "Refused", "Failed", "Passed", "In Progress", "Pending"]
Battery_RuntimeCalibrationTest_Status = ["Over Charge In Progress", "Load Too Low", "AC Input Not Acceptable", "Load Change", "State Of Charge", "Internal Fault", "Invalid State", "Internal", "Local User", "Deprecated_Protocol", "Aborted", "Refused", "Failed", "Passed", "In Progress", "Pending"]
UPS_Sensitivity = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "Low", "Reduced", "Normal"]
Output_VoltageSetting = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "VAC 240", "VAC 230", "VAC 220", "NA", "NA", "NA", "NA"]
UnSwitched_OutletGroup_LoadShedConfigSetting = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "UPS Overload", "Runtime Remaining", "Time On Battery", "Manual Restart Required", "Use Off Delay"]
UnSwitched_OutletGroup_Status =  ["NA", "Low Runtime", "NA", "MemberGroupProcess 1", "Pending On Min Runtime", "Pending On AC Presence", "Pending Off Delay", "Pending On Delay", "Pending Load Shed", "NA", "NA", "Process Sleep", "Process Shutdown", "Process Reboot", "State OFF", "State ON"]
UnSwitched_OutletGroup_TurnOFFCountdown = {
    "FFFF": "Not Active, No Countdown in progress",
    "0000": "Countdown ended",
    "0001": "Seconds remaining for countdown"
}
UPS_UserInterfaceSetting = ["NA", "NA", "NA", "Menu Read Only Permanent", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "Menu Hide SOG Items", "Menu Mode Advanced", "Menu Mode Standard", "Audible Disabled", "Audible Enabled"]
UPS_UserInterfaceCommand = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "Acknowledge Battery Alarm", "NA", "Cancel Mute", "Mute all Active Audible Alarm", "Continuous Alarm Test", "Short Test"]
UPS_UserInterfaceStatus = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "Audible Alarm Muted", "Audible Alarm In Progress", "Continuous Test in Progress"]
UPS_FileTransferSourceSetting = ["NA", "NA", "NA", "Smart Slot", "NA", "RJ45 Port", "USB Port", "Local User", "NA", "NA", "NA", "Smart Slot 1 Allowed", "NA", "RJ45 Port Allowed", "USB Port Allowed", "NA"]
UPS_Smartslot_Probe0Type = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "Not Define", "Dry Contact indicate a Dry contact Probe", "Temperature and Humidity indicates the Temperature and Humidity Probe", "Temperature indicate Temperature only Probe", "Unknown the Probe is not defined, it is likely disconnected"]
UPS_Smartslot_Probe0Status = ["NA", "Output 1 Configuration", "Output 1 Event Active", "Input 2 Critical", "Input 2 Warning", "Input 2 Normal", "Input 1 Critical", "Input 1 Warning", "Input 1 Normal", "Humidity Critical", "Humidity Warning", "Humidity Normal", "Temperature Critical", "Temperature Warning", "Temperature Normal", "Not Present"]
UPS_Smartslot_Probe0UniversalStatus = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "Not Defined", "Not Present", "Informational Alarm", "RED Alarm indicate require Attention", "Yellow Alarm indicate Warning", "Normal State indicate Green", "Unknown State"]
UPS_Smartslot_Probe1Type = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "Not Define", "Dry Contact indicate a Dry contact Probe", "Temperature and Humidity indicates the Temperature and Humidity Probe", "Temperature indicate Temperature only Probe", "Unknown the Probe is not defined, it is likely disconnected"]
UPS_Smartslot_Probe1Status = ["NA", "Output 1 Configuration", "Output 1 Event Active", "Input 2 Critical", "Input 2 Warning", "Input 2 Normal", "Input 1 Critical", "Input 1 Warning", "Input 1 Normal", "Humidity Critical", "Humidity Warning", "Humidity Normal", "Temperature Critical", "Temperature Warning", "Temperature Normal", "Not Present"]
UPS_Smartslot_Probe1UniversalStatus = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "Not Defined", "Not Present", "Informational Alarm", "RED Alarm indicate require Attention", "Yellow Alarm indicate Warning", "Normal State indicate Green", "Unknown State"]
UPS_GreenMode =["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "High Efficiency Mode Disable", "High Efficiency Mode Enable"]
UPS_PowerQualitySetting = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "Poor", "Fair", "Good", "Custom"]
UPS_PowerSystemError = ["NA", "NA", "Inverter Fault", "DC Bus Over Voltage", "PFC", "NA", "Bypass Relay", "Output Relay", "PFC Input Relay", "AVR Relay", "Back Feed Relay", "Over Temperature", "NA", "Output Over Voltage", "Output Short Circuit", "Output Overload"]
UPS_GeneralError = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "EPO Active", "NA", "UI Button on the front panel is not working", "Internal Communication Fault", "Logic Power Supply Fault", "A/D Converter", "EEPROM Fault", "Site Wiring"]
UPS_BatterySystemError = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "Bus Soft Start", "Battery Temperature Sensor", "Charger", "Over Temperature", "Need Replacement of battery", "Batery Over Voltage", "Battery Disconnected"]
UPS_Command = ["NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "Restore Factory Setting", "NA", "NA", "NA"]
UPS_OutletCommand = ["SmartSlot", "RJ45 Port", "Local User", "USB Port", "USB Port", "NA", "NA", "NA", "UnSwitched Outlet Group", "Use OFF Delay", "Use ON Delay", "Cold Boot Allowed", "Output Reboot", "Output Shutdown", "Output OFF", "Output ON", "Cancel"]
UPS_StatusChangeCause = [
    "System Initialization indicates that the present state is achieved due to microprocessor reset. value at start-up",
    "High Input Voltage condition caused the transition",
    "Low Input Voltage condition caused the transition",
    "Distorted input A bad input condition caused the transition",
    "Rapid change of input voltage caused the transition",
    "High input Frequency caused the transition",
    "Low Input Frequency caused the transition",
    "Freq and Or Phase difference between the input and the system caused the transition",
    "Acceptable Input caused the transition",
    "Automatic Test indicates that a test has been initiated via automatic timer in the UPS. This can be any test replace battery test or run time calibration",
    "Test Ended Indicates that a test has been either completed (successfully or unsuccessfully) or aborted to cause the transition.",
    "Local UI Command indicates the user pressed the on/off or other button locally to cause the transition. Includes local terminal mode interface if applicable",
    "Protocol command indicates that a command received over the smart interface has caused the state change",
    "LowBatteryVoltage caused this transition. this would be used for low battery shutdown but may be used when transitioning between other states due to a low battery voltage criteria",
    "GeneralError A general error caused the transition GeneralError_BF contains the specific fault if still valid",
    "PowerSystemError A power system error caused the transition. PowerSystemError_BF usage contains the specific fault if still valid",
    "BatterySystemError A battery system error caused the transition. BatterySystemEror_BF contains specific fault if still valid",
    "Error cleared indicates that the system changed states due to an error clearing",
    "Automatic restart indicates that internal conditions have met to allow the turn on, after a battery depletion",
    "Distorted Inverter Output indicate that the system changed states due to a distorted waveform detected on the output",
    "Inverter output acceptable indicate that the system changed state due to no further distortion on the output waveform",
    "EPO interface indicates that an input was received at the UPS through the EPO interface to turn off the output",
    "Input phase Delta out of range indicates input phase delta is out of limit",
    "Input neutral not connected indicates that neutral leg is missing",
    "ATS transfer indicates that state change was caused due to ATS operation",
    "Configuration change indicates that state change was caused by a configuration change",
    "Alert asserted an informational alert has caused the transition",
    "Alert cleared indicates that the system changed state due to an informational alert acknowledge or cleared",
    "Plug rating exceeded indicates transition happened because input current exceeded plug rating. Example: when operating in Boost mode when input current exceeds line cord rating transition to battery",
    "Outlet Group State Change causes indicates the transition occurred due to MOG or SOG state change",
    "Failure bypass expired indicates that the load was turned off due to inability to continue operating in failure bypass",
    "Internal Command indicates that a command from an internal source has caused the status change",
    "USB Command Indicates that a command from the USB port has caused the status change",
    "Internal Network1 command indicates that a command from internal network1 or Smart Connect port has caused the status change",
    "Following system controller indicates that a self-initiated change is the result from the system controller"]
