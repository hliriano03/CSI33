// Rational.h
#ifndef _RATIONAL_H
#define _RATIONAL_H

// needed for definition of ostream and istream classes
#include <iostream>

class Rational {

	// declare input and output operators functions as friends
	// to the class so they can directly access the private data
	friend std::istream& operator >> (std::istream& is, Rational &r);
	friend std::ostream& operator<<(std::ostream& os, const Rational &r);

public:
	// constructor
	Rational(const int n = 0, const int d = 1) { set(n, d); }

	// sets to n / d
	bool set(const int n, const int d);

	// access functions
	int num() const { return num_; }
	int den() const { return den_; }

	// returns decimal equivalent
	double decimal() const;

private:
	int num_, den_; // numerator and denominator
};

// prototypes for operator overloading
Rational operator+(const Rational &r1, const Rational &r2);
Rational operator-(const Rational &r1, const Rational &r2);
Rational operator*(const Rational &r1, const Rational &r2);
Rational operator/(const Rational &r1, const Rational &r2);

// prototype for comparision operators
Rational operator<(const Rational &r1, const Rational &r2);
Rational operator<=(const Rational &r1, const Rational &r2);
Rational operator>(const Rational &r1, const Rational &r2);
Rational operator>=(const Rational &r1, const Rational &r2);
Rational operator==(const Rational &r1, const Rational &r2);
Rational operator!=(const Rational &r1, const Rational &r2);


// declare the non-member input output operator functions
std::istream& operator >> (std::istream &is, Rational &r);
std::ostream& operator<<(std::ostream &os, const Rational &r);

#endif