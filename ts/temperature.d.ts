export declare class Temperature {
    _celsius: number;
    constructor(celsius: number);
    static fromCelsius(c: number): Temperature;
    static fromFahrenheit(f: number): Temperature;
    static f2c(f: number): number;
    static c2f(c: number): number;
    celsius(): number;
    fahrenheit(): number;
}
