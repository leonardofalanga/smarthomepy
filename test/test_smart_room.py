import unittest
import mock.GPIO as GPIO
from unittest.mock import patch, PropertyMock
from unittest.mock import Mock

from mock.adafruit_bmp280 import Adafruit_BMP280_I2C
from src.smart_room import SmartRoom
from mock.senseair_s8 import SenseairS8


class TestSmartRoom(unittest.TestCase):

    @patch.object(GPIO, "input")
    def SmartRoom.check_room_occupancy(self, mock_infrared_sensor: Mock):
        mock_infrared_sensor.return_value = True
        system = SmartRoom()
        occupied = system.check_room_occupancy(system.INFRARED_PIN)
        self.assertTrue(occupied)

    @patch.object(Adafruit_BMP280_I2C, "__init__")
    def SmartRoom.check_enough_light(self, mock_bmp280: Mock):
        mock_bmp280.return_value = True
        system = SmartRoom()
        light = system.check_enough_light()
        self.assertTrue(light)

    @patch.object(Senseair, "__init__")
    def SmartRoom.manage_light_level(self, mock_sensair: Mock):
        mock_sensair.return_value = True
        system = SmartRoom()
        system.manage_light_level()
        self.assertTrue(system.light_on)
        self.assertTrue(system.window_open)
        self.assertTrue(system.fan_on)