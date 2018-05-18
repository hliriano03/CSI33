#include<iostream>

using namespace std;

int main()
{
	//Problem 5
	int* a = new int(5);
	int* b = new int(6);
	
	cout << a << " = " << *a << endl;
	cout << b << " = " << *b << endl;

	b = a;

	cout << a  << " = " << *a << endl;
	cout << b << " = " << *b << endl;

	delete b;

	//Problem 6

	cout << *b << endl;

}