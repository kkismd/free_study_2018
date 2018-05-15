require "spec"
require "./temperature"

describe Temperature do
  describe "摂氏0度 = 華氏32度" do
    it "摂氏から" do
      zero = Temperature.celsius(0)
      zero.fahrenheit.should eq 32
    end

    it "華氏から" do
      zero = Temperature.fahrenheit(32)
      zero.celsius.should eq 0
    end
  end

  describe "摂氏100度 = 華氏212度" do
    it "摂氏から" do
      handred = Temperature.celsius(100)
      handred.fahrenheit.should eq 212
    end

    it "華氏から" do
      handred = Temperature.fahrenheit(212)
      handred.celsius.should eq 100
    end
  end

  describe "文字列" do
    it "摂氏" do
      zero = Temperature.fahrenheit(32)
      zero.celsius_label.should eq "摂氏0.0度"
    end

    it "華氏" do
      zero = Temperature.celsius(0)
      zero.fahrenheit_label.should eq "華氏32.0度"
    end
  end
end
