import unittest as ut
from magnitude.temperature import Temperature

class TemperatureTest(ut.TestCase):
  def test_celsius(self):
    temp = Temperature.from_celsius(34)
    self.assertEqual(34, temp.celsius())

  def test_fahrenheit(self):
    temp = Temperature.from_fahrenheit(12)
    self.assertEqual(12, temp.fahrenheit())

  def test_zero_c(self):
    temp = Temperature.from_celsius(0)
    self.assertEqual(32, temp.fahrenheit())

  def test_zero_f(self):
    temp = Temperature.from_fahrenheit(32)
    self.assertEqual(0, temp.celsius())

  def test_handred_c(self):
    temp = Temperature.from_celsius(100)
    self.assertEqual(212, temp.fahrenheit())

  def test_handred_f(self):
    temp = Temperature.from_fahrenheit(212)
    self.assertEqual(100, temp.celsius())

  def test_celsius_label(self):
    temp = Temperature.from_celsius(34)
    self.assertEqual("摂氏34度", temp.celsius_label())

  def test_fahrenheit_label(self):
    temp = Temperature.from_fahrenheit(12)
    self.assertEqual("華氏12.00度", temp.fahrenheit_label())

  def test_fail(self):
    with self.assertRaises(Exception):
      err = Temperature.from_celsius("abc")
      err.fahrenheit()

