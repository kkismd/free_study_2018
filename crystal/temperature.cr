class Temperature
  @celsius : Float64

  def initialize(@celsius)
  end

  def self.celsius(c : Number) : self
    new(c.to_f)
  end

  def self.fahrenheit(f : Number) : self
    new(f2c(f))
  end

  def self.c2f(c : Number)
    c * 1.8 + 32
  end

  def self.f2c(f : Number)
    (f - 32) / 1.8
  end

  def celsius
    @celsius
  end

  def fahrenheit
    self.class.c2f(celsius)
  end

  def celsius_label
    "摂氏#{celsius}度"
  end

  def fahrenheit_label
    "華氏#{fahrenheit}度"
  end
end
