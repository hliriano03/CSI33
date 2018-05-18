// mystring.h

/* Comments:

String will be created as an empty string of capacity 20 initially.


*/
#include <iostream>

class mystring{
	
	friend std::ostream& operator<< (std::ostream &os, const mystring &st);
	friend std::istream& operator>> (std::istream &is, mystring &st);
	
public:	
	mystring(unsigned int capacity=20);
	// str is an array of characters, size its size
	mystring(const mystring &str); // copy constructor
	~mystring(); // destructor
	
	mystring& operator+=(char c); // concatenating string with a character

	char& operator[](unsigned int position);
	int find(char c); // finds the first occurence of c in the string, returns its position, -1 if not found
	void reverse(); // reverses the string


	mystring& operator=(const mystring &str);
	void copy(const mystring &str); // used by copy constructor and in assignment operator
	mystring& operator+=(const mystring &str);

	
private:
	void resize(unsigned int newcapacity);
	char *string_;
	unsigned int size_;
	unsigned int capacity_;
	
	
};

std::ostream& operator<<(std::ostream &os, const mystring &st);
std::istream& operator>>(std::istream &is, mystring &st);
