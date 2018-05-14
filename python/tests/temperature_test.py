import unittest as ut
from magnitude.temperature import Temperature

class TemperatureTest(ut.TestCase):
  def test_celsius(self) -> None:
    temp = Temperature.from_celsius(34)
    self.assertEqual(34, temp.celsius())

  def test_fahrenheit(self) -> None:
    temp = Temperature.from_fahrenheit(12)
    self.assertEqual(12, temp.fahrenheit())

  def test_zero_c(self) -> None:
    temp = Temperature.from_celsius(0)
    self.assertEqual(32, temp.fahrenheit())

  def test_zero_f(self) -> None:
    temp = Temperature.from_fahrenheit(32)
    self.assertEqual(0, temp.celsius())

  def test_handred_c(self) -> None:
    temp = Temperature.from_celsius(100)
    self.assertEqual(212, temp.fahrenheit())

  def test_handred_f(self) -> None:
    temp = Temperature.from_fahrenheit(212)
    self.assertEqual(100, temp.celsius())

  def test_celsius_label(self) -> None:
    temp = Temperature.from_celsius(34)
    self.assertEqual("摂氏34度", temp.celsius_label())

  def test_fahrenheit_label(self) -> None:
    temp = Temperature.from_fahrenheit(12)
    self.assertEqual("華氏12.00度", temp.fahrenheit_label())

  def test_fail(self) -> None:
    with self.assertRaises(Exception):
      err = Temperature.from_celsius("abc")
      err.fahrenheit()

