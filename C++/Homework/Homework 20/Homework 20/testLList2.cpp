#include <iostream>
#include "LList2.h"

using namespace std;

int main()
{
	LList a;

	cout << "Creating a linked list a and adding four numbers to it: 10, 12, 14, and 7\n";
	a.append(10);
	a.append(12);
	a.append(14);
	a.append(7);

	cout << "The size of the linked list is " << a.size() << endl;

	cout << "The second element is " << a[1] << endl;

	cout << "Popping the first element: " << a.pop(0) << endl;

	cout << "Printing the list: " << endl;

	int i;

	cout << a << endl;

	cout << "\nInserting 19 after 14\n";

	a.insert(2, 19);

	cout << "The size of the linked list now " << a.size() << endl;
	cout << "Printing the list: " << endl;

	cout << a << endl;

	cout << "\n Now let's declare a new list b as a copy of the list a.\n";

	LList b(a);

	cout << "The size of the linked list b: " << b.size() << endl;
	cout << "Printing the list b: " << endl;

	cout << b << endl;

	cout << "Appending 28 to the list b." << endl;

	b.append(28);

	cout << "\n Finally, declaring a list c and performing assignment  c = b.\n ";

	LList c;

	c = b;

	cout << "The size of the linked list c: " << c.size() << endl;
	cout << "Printing the list c: " << endl;

	cout << c << endl;

	return 1;
}