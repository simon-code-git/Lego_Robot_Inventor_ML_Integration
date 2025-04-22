import asyncio
from contextlib import suppress
from bleak import BleakScanner, BleakClient

PYBRICKS_COMMAND_EVENT_CHAR_UUID = "c5f50002-8280-46da-89f4-6d8051e4aeef" #BLE characteristic.  
HUB_NAME = "Pybricks Hub"

async def connect_to_hub(name):
    device = BleakScanner.find_device_by_name(HUB_NAME)
    if device is None:
        print(f"could not find hub with name: {HUB_NAME}. ")
    return device
    
async def main():
    await connect_to_hub(HUB_NAME)