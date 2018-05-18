#include <iostream>
#include <cmath>

using namespace std;

double CalculateInvestment(double investment, double interestrate, double years)
{
	double InterestRateValue, total;

	total = investment;

	for (int i = 0; i < years; i++)
	{
		InterestRateValue = total * (interestrate / 100);
		total += investment + InterestRateValue;
	}
	return total;

}

int main()
{
	double investment, interestrate, years, totalinvestment;

	cout << "Input annual investment: ";
	cin >> investment;
	cout << "Input interrest rate: ";
	cin >> interestrate;
	cout << "Input how many years: ";
	cin >> years;

	totalinvestment = CalculateInvestment(investment, interestrate, years);

	cout << "\nTotal investment in " << years << " years with " << interestrate << "% interest: $" << totalinvestment << endl;

}