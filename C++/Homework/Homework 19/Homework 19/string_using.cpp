// string_using.cpp
#include <iostream>
#include "mystring.h"

using namespace std;

int main(){
	mystring s1;
	s1 += 'H';
	s1 += 'e';
	s1 += 'l';
	s1 += 'l';
	s1 += 'o';
	s1 += ',';
	s1 += ' ';
	s1 += 'w';
	s1 += 'o';
	s1 += 'r';
	s1 += 'l';
	s1 += 'd';
	s1 += '!';
	
	cout << "String 1: " << s1 << endl;

	cout << "The third letter in the string is " << s1[2];
	cout << ", and the tenth one is " << s1[9] <<" . " << endl;

	cout << "\nLet's see if letter 'o' is present in the word: " << endl;
	int p = s1.find('o');
	if (p == -1) { 
		cout << "No, it is not present in the word." << endl; }
	else {
		cout << "Yes, it is there. It's position is " << p + 1 << endl;
	}

	cout << endl << "reversing the string: ";
	s1.reverse();
	cout << s1 << endl;

	cout << endl << "reversing it back: ";
	s1.reverse();
	cout << s1 << endl;

	mystring s2(s1); //copy constructor testing
	
	cout << "String 2 was built using copy constructor on string 1.\n String 2: " << s2 << endl;

	mystring s3;

	s3 = s1; // assignment operator testing.

	cout << "\nTesting assignment operator, String 3 = String 1.\n String 3: " << s3 << endl;

	mystring s4;
	s4 += 'H';
	s4 += 'o';
	s4 += 'w';
	s4 += ' ';
	s4 += 'a';
	s4 += 'r';
	s4 += 'e';
	s4 += ' ';
	s4 += 'y';
	s4 += 'o';
	s4 += 'u';
	s4 += '?';

	cout << " Testing concatenation of two strings.\n String 1: " << s1;
	cout << "\n String 4: " << s4;
	cout << "String 1 + String 4 = ";
	s1 += s4;
	cout << s1 << endl;

	mystring s5;
	cin >> s5;

	cout << "String 5: " << s5 << endl;

	int i;
	cin >> i;


}
