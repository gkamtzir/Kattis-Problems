#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

int main()
{
	std::string line;
	std::string::iterator iter;
	std::map<char, int> mapper;
	std::map<char, int>::iterator mapperIter;
	bool found;

	std::getline(std::cin, line);

	for (iter = line.begin(); iter != line.end(); iter++)
	{
		found = false;
		for (mapperIter = mapper.begin(); mapperIter != mapper.end(); mapperIter++)
		{
			if (mapperIter->first == *iter)
			{
				mapperIter->second++;
				found = true;
			}
		}

		if (!found)
			mapper[*iter] = 1;
	}

	std::vector<int> letters;
	std::vector<int>::iterator vectorIter;

	for (mapperIter = mapper.begin(); mapperIter != mapper.end(); mapperIter++)
	{
		letters.push_back(mapperIter->second);
	}

	std::sort(letters.begin(), letters.end());

	int answer = 0;
	int removed = 0;

	for (vectorIter = letters.begin(); vectorIter != letters.end(); vectorIter++)
	{
		if (letters.size() - removed <= 2)
			break;

		answer += *vectorIter;
		removed++;

	}

	std::cout << answer << std::endl;

	return 0;
}