class Temperature:

  @classmethod
  def celsius(cls, num):
    return Temperature(num)

  @classmethod
  def fahrenheit(cls, num):
    return Temperature(f2c(num))

  @classmethod
  def f2c(cls, f):
    return (f - 32) / 1.8

  def __init__(self, celsius):
    self._celsius = celsius

  def celsius(self):
    return self._celsius

  def fahrenheit(self):
    pass
