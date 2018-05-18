#include <iostream>

using namespace std;

int linear_search(int target, int array[], int arraysize)
{
	for (int i = 0; i < arraysize; i++)
	{
		if (target == array[i])
		{
			return i;
		}
	}
	return -1;
}

int binary_search(int target, int array[], int arraysize)
{
	int min = 0;
	int max = arraysize - 1;

	while (true)
	{
		if (max < min)
		{
			return -1;
		}

		int middle = (min + max) / 2;

		if (array[middle] < target)
		{
			min = middle + 1;
		}
		else if (array[middle] > target)
		{
			max = middle - 1;
		}
		else
		{
			return middle;
		}
	}
}

int main()
{
	int arr[10] = { 1,2,4,5,6,8,13,20,29,40 };
	int num;
	int target;

	do
	{
		cout << "Choose a number to find it's the position in the array: ";
		cin >> target;

		//Linear Search
		/*if (linear_search(target, arr, 10) == -1)
		{
			cout << "The number is not in the array, please try again.\r" << endl;
		}
		else 
		{
			cout << "The number's position is: " << linear_search(target, arr, 10) << endl << endl;
			break;
			
		}*/

		//Binary Search
		if (binary_search(target, arr, 10) == -1)
		{
			cout << "The number is not in the array, please try again.\r" << endl;
		}
		else
		{
			cout << "The number's position is: " << binary_search(target, arr, 10) << endl << endl;
			break;

		}

	} while (true);

	return 0;
}