import unittest as ut
from magnitude.temperature import Temperature

class TemperatureTest(ut.TestCase):
  def test_celsius(self):
    temp = Temperature.celsius(34)
    print(temp)
    self.assertEqual(34, temp.celsius())

  def test_fahrenheit(self):
    pass

