#include <iostream>
#include <vector>
using namespace std;

int main()
{
	vector<int> items;
	int num, sum;
	double average;
	sum = 0;
	
	do {
		cout << "Input a non-negative number to continue: ";
		cin >> num;
		items.push_back(num);

	} while (num > 0);

	for (int a = 0; a < (items.size() - 1); a++) {
		sum += items[a];
	}

	average = sum / (items.size() - 1.0);

	cout << "\nSum: " << sum << endl;
	cout << "Average: " << average << "\n\n";


}