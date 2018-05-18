using namespace std;
#include "Rational.h"

bool Rational::set(const int n, const int d)
{
	if (d != 0) {
		num_ = n;
		den_ = d;
		return true;
	}
	else
		return false;
}

Rational operator+(const Rational &r1, const Rational &r2)
{
	int num, den;

	num = r1.num() * r2.den() + r2.num() * r1.den();
	den = r1.den() * r2.den();
	return Rational(num, den);
}

Rational operator-(const Rational &r1, const Rational &r2)
{
	int num, den;

	num = r1.num() * r2.den() - r2.num() * r1.den();
	den = r1.den() * r2.den();
	return Rational(num, den);
}

Rational operator*(const Rational &r1, const Rational &r2)
{
	int num, den;

	num = r1.num() * r2.num();
	den = r1.den() * r2.den();
	return Rational(num, den);
}

Rational operator/(const Rational &r1, const Rational &r2)
{
	int num, den;

	num = r1.num() * r2.den();
	den = r1.den() * r2.num();
	return Rational(num, den);
}

Rational operator<(const Rational &r1, const Rational &r2)
{
	int num, den;

	if (r1.num() / r1.den() < r2.num() / r2.den())
	{
		return true;
	}
	else
	{
		return false;
	}
}

Rational operator<=(const Rational &r1, const Rational &r2)
{
	int num, den;

	if (r1.num() / r1.den() <= r2.num() / r2.den())
	{
		return true;
	}
	else
	{
		return false;
	}
}

Rational operator>(const Rational &r1, const Rational &r2)
{
	int num, den;

	if (r1.num() / r1.den() > r2.num() / r2.den())
	{
		return true;
	}
	else
	{
		return false;
	}
}

Rational operator>=(const Rational &r1, const Rational &r2)
{
	int num, den;

	if (r1.num() / r1.den() >= r2.num() / r2.den())
	{
		return true;
	}
	else
	{
		return false;
	}
}

Rational operator==(const Rational &r1, const Rational &r2)
{
	int num, den;

	if (r1.num() / r1.den() == r2.num() / r2.den())
	{
		return true;
	}
	else
	{
		return false;
	}
}

Rational operator!=(const Rational &r1, const Rational &r2)
{
	int num, den;

	if (r1.num() / r1.den() != r2.num() / r2.den())
	{
		return true;
	}
	else
	{
		return false;
	}
}


std::istream& operator >> (std::istream &is, Rational &r)
{
	char c;

	is >> r.num_ >> c >> r.den_;
	return is;
}

std::ostream& operator<<(std::ostream &os, const Rational &r)
{
	os << r.num() << "/" << r.den();
	return os;
}