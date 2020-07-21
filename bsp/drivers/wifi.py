from microchip.winc1500 import winc1500 as wifi_driver
from wireless import wifi

def init():
	wifi_driver.auto_init()
    return wifi_driver

def interface():
    return wifi






