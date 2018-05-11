require 'minitest/autorun'
require './temperature'

class TestTemperature < Minitest::Test
  def test_celsius
    subject = Temperature.celsius(34)
    assert_equal subject.celsius, 34
  end

  def test_zero
    zero = Temperature.celsius(0)
    assert_equal zero.fahrenheit, 32
  end

  def test_zero2
    zero = Temperature.fahrenheit(32)
    assert_equal zero.celsius, 0
  end

  def test_handred
    handred = Temperature.celsius(100)
    assert_equal handred.fahrenheit, 212
  end

  def test_handred2
    handred = Temperature.fahrenheit(212)
    assert_equal handred.celsius, 100
  end

  def test_fahrenheit
    subject = Temperature.fahrenheit(12)
    assert_equal subject.fahrenheit, 12
  end

  def test_celsius_label
    zero = Temperature.celsius(0)
    assert_equal zero.celsius_label, "摂氏0度"
  end

  def test_celsius_label
    zero = Temperature.celsius(0)
    assert_equal zero.fahrenheit_label, "華氏32.0度"
  end
end
