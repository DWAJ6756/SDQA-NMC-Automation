import simulator

simulator = simulator.MicrolinkSimulator(simulator.microlink_host_ip, simulator.microlink_sim_path, simulator.microlink_xml_path)



simulator.UPSSystem_UnSwitchedOutletGroup_Status()
a=60


simulator.UPSStatus_BF()

# while(a):
#     simulator.UPSStatus_BF()
#     print("----------------------------")
#     a=a-1
#
simulator.SerialNumber_STR()

simulator.ManufactureDate()

simulator.UPSModel_STR()

simulator.UPSSKU_STR()

# simulator.Battery_Insatllation_date()

# simulator.Output_Rated_ApparentPower()
# simulator.Output_Rated_RealPower()
#
# simulator.Battery_replace_AlarmNotificationSetting()
#
# simulator.Battery_replace_AlarmReminderInterval()
#
# simulator.UPSBatterySKU()
#
# simulator.BatteryTest_IntervalSetting()
#
# simulator.Battery_LowRuntimeWarningSetting()
#
# simulator.Battery_LifeTimeStatus()
#
# simulator.Battery_Volatge()
#
# simulator.Battery_StateOfCharge()
#
# simulator.Battery_ReplaceTest_Status()
#
# simulator.Battery_RuntimeCalibrationTest_Status()
#
# simulator.Battery_RuntimeRemaining()
#
# simulator.Battery_Temperature()
#
# simulator.OutputSystem_UpperAcceptableVoltageSetting()
#
# simulator.OutputSystem_LowerAcceptableVoltageSetting()
#
#
#
#
# .OutputSystem_UPS_Sensitivity()
#
# simulator.OutputSystem_Energy()
#
# simulator.Output_Rated_ApparentPower()
#
# simulator.Output_Rated_RealPower()
#
# simulator.OutputSystem_VoltageACSetting()
#
# simulator.OutputSystem_VoltageAC()
#
# simulator.OutputSystem_CurrentAC()
#
# simulator.OutputSystem_Frequency()
#
# simulator.OutputSystem_Actual_ApparentPower()
#
# simulator.OutputSystem_Actual_RealPower()

# simulator.UPSSystem_UnswitchedOutletGroup_TurnOnCountdownSetting()
#
# simulator.UPSSystem_UnswitchedOutletGroup_TurnOffCountdownSetting()
#
# simulator.UPSSystem_UnswitchedOutletGroup_StayOffCountdownSetting()
#
# simulator.UPSSystem_UnswitchedOutletGroup_MinimumReturnRuntime()
#
# simulator.UPSSystem_UnSwitchedOutletGroup_LoadShedConfigSetting()
#
# simulator.UPSSystem_UnswitchedOutletGroup_LoadShedTimeOnBattery()
#
# simulator.UPSSystem_UnswitchedOutletGroup_Name()
#
# #simulator.UPSSystem_UnswitchedOutletGroup_TurnOFFCountdown()
#
# simulator.UPSSystem_UserInterfaceSetting()
#
# simulator.UPSSystem_UserInterfaceCommand()
#
# simulator.UPSSystem_UserInterfaceStatus()
#
# simulator.UPSSystem_FileTransferSourceSetting()
#
# simulator.UPSSystem_SmartSlotSKU()
#
# simulator.UPSSystem_SmartSlotHWversion()
#
# simulator.UPSSystem_SmartSlotProbe0Name()
#
# simulator.UPSSystem_Smartslot_Probe0Type()
#
# simulator.UPSSystem_SmartSlotProbe0Temperature()
#

# simulator.UPSSystem_SmartSlotProbe0Humidity()
#
# simulator.UPSSystem_Smartslot_Probe0Status()
#
# simulator.UPSSystem_Smartslot_Probe0UniversalStatus()
#
# simulator.UPSSystem_SmartSlotProbe1Name()
#
# simulator.UPSSystem_Smartslot_Probe1Type()
#
# simulator.UPSSystem_SmartSlotProbe1Temperature()
#
# simulator.UPSSystem_SmartSlotProbe1Humidity()
#
# simulator.UPSSystem_Smartslot_Probe1Status()
#
# simulator.UPSSystem_Smartslot_Probe1UniversalStatus()
#
# simulator.UPSSystem_Name()
#
# simulator.UPSSystem_HighEfficiencyMode()
#
# simulator.UPSSystem_PowerQualitySetting()
#
# simulator.UPSSystem_PowerSystemError()
#
# simulator.UPSSystem_GeneralError()
#
# simulator.UPSSystem_BatterySystemError()
#
# simulator.UPSSystem_Command()
#
# simulator.UPSSystem_OutletCommand()
#
# simulator.UPSSystem_StatusChangeCause()

# simulator.UPSSystem_SwitchedOutletGroup1_Name()
#
# simulator.UPSSystem_SwitchedOutletGroup2_Name()
#
# simulator.UPSSystem_SwitchedOutletGroup3_Name()
#
# simulator.UPSSystem_SwitchedOutletGroup1_LowRuntimeWarningSetting()
#
# simulator.UPSSystem_SwitchedOutletGroup2_LowRuntimeWarningSetting()
#
# simulator.UPSSystem_SwitchedOutletGroup3_LowRuntimeWarningSetting()
#
# simulator.UPSSystem_SwitchedOutletGroup1_TurnOnCountdownSetting()
#
# simulator.UPSSystem_SwitchedOutletGroup2_TurnOnCountdownSetting()
#
# simulator.UPSSystem_SwitchedOutletGroup3_TurnOnCountdownSetting()
#
# simulator.UPSSystem_SwitchedOutletGroup1_TurnOffCountdownSetting()
#
# simulator.UPSSystem_SwitchedOutletGroup2_TurnOffCountdownSetting()
#
# simulator.UPSSystem_SwitchedOutletGroup3_TurnOffCountdownSetting()
#
# simulator.UPSSystem_SwitchedOutletGroup1_StayOffCountdownSetting()
#
# simulator.UPSSystem_SwitchedOutletGroup2_StayOffCountdownSetting()
#
# simulator.UPSSystem_SwitchedOutletGroup2_StayOffCountdownSetting()
#
# simulator.UPSSystem_SwitchedOutletGroup3_StayOffCountdownSetting()
#
# simulator.UPSSystem_SwitchedOutletGroup1_LoadShedConfigSetting()
#
# simulator.UPSSystem_SwitchedOutletGroup2_LoadShedConfigSetting()
#
# simulator.UPSSystem_SwitchedOutletGroup3_LoadShedConfigSetting()
#
# simulator.UPSSystem_SwitchedOutletGroup1_LoadShedRuntimeRemaining()
#
# simulator.UPSSystem_SwitchedOutletGroup2_LoadShedRuntimeRemaining()
#
# simulator.UPSSystem_SwitchedOutletGroup3_LoadShedRuntimeRemaining()
#
# simulator.UPSSystem_SwitchedOutletGroup1_LoadShedTimeOnBattery()
#
# simulator.UPSSystem_SwitchedOutletGroup2_LoadShedTimeOnBattery()
#
# simulator.UPSSystem_SwitchedOutletGroup3_LoadShedTimeOnBattery()
#
# simulator.UPSSystem_SwitchedOutletGroup1_MinimumReturnRuntime()
#
# simulator.UPSSystem_SwitchedOutletGroup2_MinimumReturnRuntime()
#
# simulator.UPSSystem_SwitchedOutletGroup3_MinimumReturnRuntime()
#
#
#
# simulator.UPSSystem_SwitchedOutletGroup3_Status()
#
# simulator.shutdown_microlink_simulator()