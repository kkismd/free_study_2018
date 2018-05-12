from typing import Union
Numeric = Union[int,float]

class Temperature:
  def __init__(self, celsius: Numeric) -> None:
    self._celsius: Numeric = celsius

  @classmethod
  def from_celsius(cls, num: Numeric) -> 'Temperature':
    return cls(num)

  @classmethod
  def from_fahrenheit(cls, num: Numeric) -> 'Temperature':
    return cls(cls.f2c(num))

  @staticmethod
  def f2c(f: Numeric) -> float:
    return (f - 32) / 1.8

  @staticmethod
  def c2f(c: Numeric) -> float:
    return c * 1.8 + 32

  def celsius(self) -> Numeric:
    return self._celsius

  def fahrenheit(self) -> float:
    return self.c2f(self._celsius)

  def celsius_label(self) -> str:
    return "摂氏%d度" % self.celsius()

  def fahrenheit_label(self) -> str:
    return "華氏%.2f度" % self.fahrenheit()
