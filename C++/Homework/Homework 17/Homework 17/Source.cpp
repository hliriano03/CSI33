#include <iostream>
#include "Rational.h"

using namespace std;

int main()
{
	Rational r1(1,2), r2(1,2);


	cout << r1 << " + " << r2 << " = " << r1 + r2 << endl;
	cout << r1 << " - " << r2 << " = " << r1 - r2 << endl;
	cout << r1 << " * " << r2 << " = " << r1 * r2 << endl;
	cout << r1 << " / " << r2 << " = " << r1 / r2 << endl;
	cout << endl;
	cout << r1 << " < " << r2 << " = " << (r1 < r2) << endl;
	cout << r1 << " <= " << r2 << " = " << (r1 <= r2) << endl;
	cout << r1 << " > " << r2 << " = " << (r1 > r2) << endl;
	cout << r1 << " >= " << r2 << " = " << (r1 >= r2) << endl;
	cout << r1 << " == " << r2 << " = " << (r1 == r2) << endl;
	cout << r1 << " != " << r2 << " = " << (r1 != r2) << endl;

}