#include <iostream>
#include <string>


int main()
{
	int guesses, low, high, middle;
	std::string data;

	guesses = 0;
	low = 1;
	high = 1000;
	middle = 500;

	do
	{
		std::cout << middle << std::endl;

		guesses++;

		std::getline(std::cin, data);
		
		if (data == "lower")
			high = middle - 1;
		else if (data == "higher")
			low = middle + 1;
		else
			break;

		middle = (low + high) / 2;

	} while (guesses < 10);

	return 0;
}