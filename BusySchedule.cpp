#include <iostream>
#include <string>
#include <regex>
#include <vector>

void PrintHours(std::vector<int> hours, std::string period);

bool CustomSort(int i, int j);

int main()
{
	std::regex expression("^([0-9]{1,2})(?:\:)([0-9]{2}) ([a-z\.]+)");
	std::string line;
	std::smatch match;
	int n;

	std::vector<int> timesAM;
	std::vector<int> timesPM;

	std::getline(std::cin, line);
	n = stoi(line);

	while (n != 0)
	{
		for (int i = 0; i < n; i++)
		{
			std::getline(std::cin, line);
			std::regex_search(line, match, expression);
			if (match[3].str() == "a.m.")
				timesAM.push_back(stoi(match[1].str() + match[2].str()));
			else
				timesPM.push_back(stoi(match[1].str() + match[2].str()));
		}

		std::sort(timesAM.begin(), timesAM.end(), CustomSort);
		std::sort(timesPM.begin(), timesPM.end(), CustomSort);

		PrintHours(timesAM, "a.m.");
		std::cout << std::endl;
		PrintHours(timesPM, "p.m.");

		timesAM.clear();
		timesPM.clear();

		std::getline(std::cin, line);
		n = stoi(line);
	}
	
	return 0;
}

void PrintHours(std::vector<int> hours, std::string period)
{
	std::vector<int>::iterator iter;

	for (iter = hours.begin(); iter != hours.end(); iter++)
	{
		std::string temp = std::to_string(*iter);
		int hoursLength;
		if (temp.length() == 3)
			hoursLength = 1;
		else
			hoursLength = 2;
		std::cout << temp.substr(0, hoursLength) << ":" << temp.substr(hoursLength) << " " + period << std::endl;
	}
}

bool CustomSort(int i, int j)
{
	if ((i >= 1200 && j >= 1200) || (i < 1200 && j < 1200))
		return i < j;
	else if (i >= 1200)
		return true;
	else
		return false;
}