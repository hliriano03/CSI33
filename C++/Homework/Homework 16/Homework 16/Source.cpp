#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

//Sorts array
int sort(vector<int> arr, ofstream& output)
{


	for (int i = 1; i < arr.size(); ++i) {
		for (int j = 0; j < arr.size() - 1; ++j) {
			if (arr[j] > arr[i]) swap(arr[j], arr[i]);
		}
	}

	output << endl << "Sorted Array: ";

	for (int i = 0; i < arr.size(); i++)
	{
		if (i + 1 != arr.size())
		{
			output << arr[i] << ", ";
		}
		else
		{
			output << arr[i];
		}
	}

	output << endl;
	return 1;
}

//Gets the minimum of the array of numbers
int min(vector<int> arr, ofstream& output)
{
	int min = 0;
	int count = 0;

	for each(int i in arr)
	{
		if (count == 0)
		{
			min = i;
		}

		if (min > i)
		{
			min = i;
		}
		count += 1;
	}
	
	output << "Min: " << min << endl;
	return min;
}

//Gets the  maximum of the array of numbers
int max(vector<int> arr, ofstream& output)
{
	int max = 0;
	int count = 0;

	for each(int i in arr)
	{
		if (count == 0)
		{
			max = i;
		}

		if (max < i)
		{
			max = i;
		}
		count += 1;
	}
	output << "Max: " << max << endl;
	return max;
}

//Gets the average of the array of numbers

double average(vector<int> arr, ofstream& output)
{
	int average = 0;

	for each(int i in arr)
	{
		average += i;
	}
	output << "Total Average: " << average / (arr.size() * 1.0) << endl;
	return average/(arr.size() * 1.0);
}

//Gets the average of all positive numbers in the array

double posAverage(vector<int> arr, ofstream& output)
{
	int posAverage = 0;

	for each(int i in arr)
	{
		posAverage += i;
	}
	output << "Positive Number Average: " << posAverage / (arr.size() * 1.0) << endl;
	return posAverage / (arr.size() * 1.0);
}

//Gets the average of all negative numbers in the array

double negAverage(vector<int> arr, ofstream& output)
{
	int negAverage = 0;

	for each(int i in arr)
	{
		negAverage += i;
	}
	output << "Negative Number Average: " << negAverage / (arr.size() * 1.0) << endl;
	return negAverage / (arr.size() * 1.0);
}

//Gets all the zeroes in the array

//Gets all the positives numbers in the array

//Gets all the negatives numbers in the array

int main()
{
	ifstream ifs;
	ofstream ofs;
	
	int x, zeroCount = 0;
	vector<int> arr = {};
	vector<int> posarr = {};
	vector<int> negarr = {};

	ifs.open("in.txt");

	while (!ifs.eof())
	{
		ifs >> x;
		arr.push_back(x);

		if (x > 0)
		{
			posarr.push_back(x);
		}
		else if (x < 0)
		{
			negarr.push_back(x);
		}
		else
		{
			zeroCount++;
		}
	}

	ifs.close();
	ofs.open("out.txt");

	cout << "Min: " << min(arr, ofs) << endl;
	cout << "Max: " << max(arr, ofs) << endl;
	cout << "Total Average: " << average(arr, ofs) << endl;
	cout << "Positive Number Average: " << posAverage(posarr, ofs) << endl;
	cout << "Negative Number Average: " << negAverage(negarr, ofs) << endl;
	cout << "Zero Numbers Count: " << zeroCount << endl;
	cout << "Positive Numbers Count: " << posarr.size() << endl;
	cout << "Negative Number Count: " << negarr.size() << endl << endl;

	ofs << "Zero Numbers Count: " << zeroCount << endl;
	ofs << "Positive Numbers Numbers Count: " << posarr.size() << endl;
	ofs << "Negative Numbers Count: " << negarr.size() << endl;
	
	sort(arr, ofs);
}
