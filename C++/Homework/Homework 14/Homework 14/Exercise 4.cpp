#include <iostream>
#include <cmath>
using namespace std;

bool quadraticFormula(double a, double b, double c, double totalResults[])
{

	double numerator1 = ((-b + sqrt((b * b) - (4.0 * a * c))));
	double numerator2 = ((-b - sqrt((b * b) - (4.0 * a * c))));
	double denominator = 2 * a;

	if (((b*b) - (4 * a*c)) < 0)
	{
		cout << "\nError cant square root a negative.\n";
		return false;
	}

	else if (denominator == 0)
	{
		cout << "\nCant compute, Denominator is 0";
		return false;
	}

	totalResults[0] = numerator1 / denominator;
	totalResults[1] = numerator2 / denominator;

	return true;
}

int main()
{
	double a, b, c;
	double x[2];       //store results of x

	cout << "Please Enter a, b, and c to get Results of x:\n";

	cout << "a: ";
	cin >> a;

	cout << "b: ";
	cin >> b;

	cout << "c: ";
	cin >> c;

	if (quadraticFormula(a, b, c, x))
	{
		cout << "\nYour Results are:" << endl;

		if (x[0] == x[1])
		{
			cout << "x = " << x[0] << endl;
		}
		else
		{
			cout << "x1 = " << x[0] << endl;
			cout << "x2 = " << x[1] << endl;
		}
	}

	return 0;
}