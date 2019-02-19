#include <iostream>
#include <string>
#include <regex>

int main()
{
	int T;
	std::string line;
	std::regex expression("^(?:simon says) (.*)");

	std::getline(std::cin, line);
	T = stoi(line);
	std::smatch matches;

	for (int i = 0; i < T; i++)
	{
		std::getline(std::cin, line);
		if (std::regex_search(line, matches, expression))
			std::cout << matches[1].str() << std::endl;
		else
			std::cout << std::endl;
	}
}

