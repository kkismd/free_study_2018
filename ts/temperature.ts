export class Temperature {
  private _celsius: number;
  constructor(celsius: number) {
    this._celsius = celsius;
  }

  static fromCelsius(c: number): Temperature {
    return new Temperature(c);
  }

  static fromFahrenheit(f: number): Temperature {
    return new Temperature(Temperature.f2c(f));
  }

  static f2c(f: number): number {
    return (f - 32) / 1.8;
  }

  static c2f(c: number): number {
    return c * 1.8 + 32;
  }

  celsius(): number {
    return this._celsius;
  }

  fahrenheit(): number {
    return Temperature.c2f(this._celsius);
  }

  celsiusLabel(): string {
    return `摂氏${this.celsius()}度`;
  }

  fahrenheitLabel(): string {
    return `華氏${Temperature.c2f(this.celsius())}度`;
  }
}

/** Testing */

function is(a: number|string, b: number|string): void {
  if (a !== b) {
    console.log("%s is not %s", a.toString(), b.toString());
  }
}

const zero_c: Temperature = Temperature.fromCelsius(0);
is(zero_c.celsius(), 0);
is(zero_c.fahrenheit(), 32);

const zero_f: Temperature = Temperature.fromFahrenheit(32);
is(zero_f.celsius(), 0);
is(zero_f.fahrenheit(), 32);

const handred_c: Temperature = Temperature.fromCelsius(100);
is(handred_c.celsius(), 100);
is(handred_c.fahrenheit(), 212);

const handred_f: Temperature = Temperature.fromFahrenheit(212);
is(handred_f.celsius(), 100);
is(handred_f.fahrenheit(), 212);

is(zero_c.celsiusLabel(), "摂氏0度");
is(zero_f.fahrenheitLabel(), "華氏32度");

const error_t: Temperature = Temperature.fromCelsius("foo");
is(error_t.celsius(), 0);
