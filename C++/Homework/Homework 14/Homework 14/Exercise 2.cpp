#include <iostream>
using namespace std;

int main()
{
	int cents, quarters, dimes, nickels, pennies;
	quarters = dimes = nickels = pennies = 0;
	
	do {
		cout << "Input number of cents: ";
		cin >> cents;

		if (cents < 0 || cents > 99) {
			cout << "Only numbers from 0-99\n\n";
		}
	} while (cents < 0 || cents > 99);
	
	while (cents != 0)
	{
		if (cents >= 25) {
			quarters++;
			cents -= 25;

		}
		else if (cents >= 10) {
			dimes++;
			cents -= 10;
		}
		else if (cents >= 5) {
			nickels++;
			cents -= 5;
		}
		else if (cents >= 1) {
			pennies++;
			cents -= 1;
		}
	}
	cout << "\nQuarters: " << quarters << endl;
	cout << "Dimes: " << dimes << endl;
	cout << "Nickels: " << nickels << endl;
	cout << "Pennies: " << pennies << endl;
}