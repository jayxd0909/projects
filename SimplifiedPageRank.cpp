#include <iostream>
#include <map>
#include <vector>
#include <utility>
#include <iomanip>

// Used template
class AdjacencyList 
{
	private:
	//Think about what member variables you need to initialize
	
		//From Graphs Review
		std::map<std::string, std::vector<std::string>> fromtolist;
		std::map<std::string, std::vector<std::string>> tofromlist;
		std::map<std::string, double> weights;

	public:
	//Think about what helper functions you will need in the algorithm
		void PageRank(int n, std::vector<std::string> from, std::vector<std::string> to);
		void buildLists(std::vector<std::string> from, std::vector<std::string> to);
};

void AdjacencyList::PageRank(int n, std::vector<std::string> from, std::vector<std::string> to)
{
	// Sets up the initial weights map, with all websites having the same ranking
	std::string prev;
	double count = 0;
	for (int i = 0; i < from.size(); i++)
	{
		if (from.at(i) != prev || i == 0)
		{
			weights.insert({ from.at(i), 0 });
			prev = from.at(i);
			count++;
		}
		if (fromtolist.find(to.at(i)) == fromtolist.end() && weights.find(to.at(i)) == weights.end())
		{
			weights.insert({ to.at(i), 0 });
			count++;
		}
	}

	double d = 1 / count;
	for (auto i = weights.begin(); i != weights.end(); i++)
	{
		i->second = d;
	}

	//The algorithm, goes through the tofromlist map website by website, taking advantage of the other created maps in its calculation of the new ranking in each power iteration
	if (n > 1)
	{
		for (int i = 1; i < n; i++)
		{
			std::vector<double> newweights;
			for (auto j = tofromlist.begin(); j != tofromlist.end(); j++)
			{
				double newweight = 0;
				for (int k = 0; k < j->second.size(); k++)
				{
					if (j->second.size() != 0)
					{
						auto it = weights.find(j->second.at(k));
						auto it2 = fromtolist.find(j->second.at(k));
						newweight += it->second / it2->second.size();
					}
				}
				newweights.push_back(newweight);
			}
			int loop = 0;
			for (auto i = weights.begin(); i != weights.end(); i++)
			{
				if (tofromlist.find(i->first) == tofromlist.end())
				{
					i->second = 0;
				}
				else
				{
					i->second = newweights.at(loop);
					loop++;
				}
			}
		}
	}

	for (auto i = weights.begin(); i != weights.end(); i++)
	{
		std::cout << i->first << " " << std::fixed << std::setprecision(2) << i->second << "\n";
	}
} 

// Builds two adjacency lists, one for keeping track of to-from connections, the other for keeping track of from-to connections
void AdjacencyList::buildLists(std::vector<std::string> from, std::vector<std::string> to)
{
	for(int i = 0; i < from.size(); i++)
	{
		tofromlist[to.at(i)].push_back(from.at(i));
		fromtolist[from.at(i)].push_back(to.at(i));
	}
}

// Used template
// prints the PageRank of all pages after p powerIterations in ascending alphabetical order of webpages and rounding rank to two decimal places
// This class and method are optional. To accept the input, you can use this method:
int main()
{
	int no_of_lines, power_iterations;
	std::vector<std::string> fromlist, tolist;
	std::string from, to;
	std::cin >> no_of_lines;
	std::cin >> power_iterations;

	for (int i = 0;i < no_of_lines; i++)
	{
		std::cin >> from;
		std::cin >> to;
		// Do Something
		fromlist.push_back(from);
		tolist.push_back(to);
	}

	//Create a graph object
	AdjacencyList Created_Graph;
	Created_Graph.buildLists(fromlist, tolist);
	Created_Graph.PageRank(power_iterations, fromlist, tolist);
}
