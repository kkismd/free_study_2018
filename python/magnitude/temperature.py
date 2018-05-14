from typing import Union
numeric = Union[int,float]

class Temperature:
  def __init__(self, celsius: numeric) -> None:
    self._celsius: numeric = celsius

  @classmethod
  def from_celsius(cls, num: numeric) -> 'Temperature':
    return cls(num)

  @classmethod
  def from_fahrenheit(cls, num: numeric) -> 'Temperature':
    return cls(cls.f2c(num))

  @staticmethod
  def f2c(f: numeric) -> float:
    return (f - 32) / 1.8

  @staticmethod
  def c2f(c: numeric) -> float:
    return c * 1.8 + 32

  def celsius(self) -> numeric:
    return self._celsius

  def fahrenheit(self) -> float:
    return self.c2f(self._celsius)

  def celsius_label(self) -> str:
    return "摂氏%d度" % self.celsius()

  def fahrenheit_label(self) -> str:
    return "華氏%.2f度" % self.fahrenheit()
