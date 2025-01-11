import math
import re
from datetime import datetime, timedelta
import os

output = ""


def hex_to_binary(hex_value):
    decimal_value = int(hex_value, 16)
    binary_value = bin(decimal_value)[2:]
    binary_value_16 = binary_value.zfill(16)
    return binary_value_16

def hex_to_binary_32(hex_value):
    decimal_value = int(hex_value, 32)
    binary_value = bin(decimal_value)[2:]
    binary_value_32 = binary_value.zfill(32)
    return binary_value_32

def hex_to_decimal(hex_value):
    decimal_value = int(hex_value, 16)
    return decimal_value

def hex_to_ascii(hex_value):
    bytes_value = bytes.fromhex(hex_value)
    ascii_value = bytes_value.decode('utf-8', errors='replace')
    return ascii_value

def extract_and_print_values(file_path):
    global output
    global days
    global Hex_values
    global Binary_values
    global Ascii_values
    global Decimal_values
    global String_values


    with open(file_path, 'r') as file:
        content = file.read()

    hex_values = re.findall(r'usageHexValue :\s*([^\n]+)', content)
    str_values = re.findall(r'usageStrValue :\s*([^\n]+)', content)


    Hex_values = hex_values

    for value in hex_values:

        Binary_values_32 = hex_to_binary_32(value)

        Binary_values = hex_to_binary(value)

        Ascii_values = hex_to_ascii(value)

        Decimal_values = hex_to_decimal(value)
        days = hex_to_decimal(value)



    for value in str_values:

        String_values = value

current_directory = os.getcwd()
output_filename = "microlink_output.txt"
file_path = os.path.join(current_directory, output_filename)


def empty_file(file_path):
    with open(file_path, 'w') as file:
        pass

def calculate_manufacture_date(days):
    global Manufacture_date

    days = int(days)
    start_date = datetime(2000, 1, 1)
    manufacture_date = start_date + timedelta(days=days)
    Manufacture_date = manufacture_date.strftime('%Y-%m-%d')
    return manufacture_date


def convert_decimal_to_custom_value(decimal_value):
    # Divide by 512 to get the desired value
    custom_value = decimal_value / 512

    return custom_value


def convert_decimal_to_custom_value_temp(decimal_value):
    # Divide by 128.7 to get the desired value
    custom_value = decimal_value / 128.7
    custom_value=round(custom_value)

    return custom_value






