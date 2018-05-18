// hello.cpp
#include <iostream>

using namespace std;

int main() {

	double Fahrenheit, Celsius;

	cout << "====Fahrenheit To Celsius Converter====\n";
	cout << "\nFahrenheit: ";
	cin >> Fahrenheit;

	Celsius = (Fahrenheit - 32) * (5 / 9.0);

	cout << "\nCelsius = " << Celsius << "\n\n";

	return 0;
}