class Temperature
  # @implements Temperature

  # private_class_method :new

  def self.celsius(num)
    Temperature.new(num)
  end

  def self.fahrenheit(num)
    Temperature.new(f2c(num))
  end

  def self.f2c(f)
    (f - 32) / 1.8
  end

  def self.c2f(c)
    c * 1.8 + 32
  end

  def initialize(num)
    @celsius = num
  end

  def celsius
    @celsius
  end

  def celsius_label
    "摂氏#{@celsius}度"
  end

  def fahrenheit
    # @type const Temperature: Temperature.module
    Temperature.c2f(celsius)
  end

  def fahrenheit_label
    "華氏#{fahrenheit}度"
  end
end
