// CSVtoSQL.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <istream>
#include <string>
#include <vector>
#include <regex>

int main()
{
    std::ifstream myFile;
    myFile.open("Auto Sales data.csv");
    std::ofstream output("ToyCarOrdersAndSales Insert Commands.sql");

    std::string s;
    std::string token;
    std::string q = "INSERT INTO ToyCarOrdersAndSales (";

    std::regex noSpace("^[^ ]");

    getline(myFile, s);
    std::vector<std::string> v;
    std::stringstream ss(s);

    output << "SET DEFINE OFF;\n";

    while (std::getline(ss, token, ','))
    {
        v.push_back(token);
    }
    
    while (v.size() > 0)
    {
        if (v.size() != 13 && v.size() != 11 && v.size() != 10 && v.size() != 8)
        {
            if (v.size() == 1)
            {
                q = q + v.at(0) + ")\nVALUES (";
            }
            else if(v.size() == 14)
            {
                q = q + "DAYSSINCELASTORDER, ";
            }
            else
            {
                q = q + v.at(0) + ", ";
            }
        }
        v.erase(v.begin());
    }
    
    while (getline(myFile, s))
    {
        std::string final = q;
        std::vector<std::string> v;
        std::stringstream ss(s);

        while (std::getline(ss, token, ','))
        {
            v.push_back(token);
        }
        
        while (v.size() > 20)
        {
            if (std::regex_search(v.at(12), noSpace))
            {
                std::string a1 = v.at(13);
                std::string a2 = v.at(14);
                std::string add = a1 + ", " + a2;
                add.erase(std::remove(add.begin(), add.end(), '\"'), add.end());
                v.at(13) = add;
                v.erase(v.begin() + 14);
            }
            else
            {
                std::string a1 = v.at(11);
                std::string a2 = v.at(12);
                std::string add = a1 + ", " + a2;
                add.erase(std::remove(add.begin(), add.end(), '\"'), add.end());
                v.at(11) = add;
                v.erase(v.begin() + 12);
            }
        }

        while (v.size() > 0)
        {
            if (v.size() != 13 && v.size() != 11 && v.size() != 10 && v.size() != 8)
            {
                if (v.size() == 1)
                {
                    final = final + "'" + v.at(0) + "'" + ");\n";
                    output << final;
                }
                else
                {
                    if (v.size() < 16 && v.size() != 14)
                    {
                        if (v.size() == 15) 
                        {
                            std::vector<std::string> v2;
                            std::stringstream ss2(v.at(0));
                            while (std::getline(ss2, token, '/'))
                            {
                                v2.push_back(token);
                            }
                            std::string d = "";
                            while (v2.size() != 0)
                            {
                                if (v2.size() == 1)
                                {
                                    d = d + v2.at(v2.size()-1);
                                }
                                else
                                {
                                    d = d + v2.at(v2.size() - 1) + "-";
                                }
                                v2.erase(v2.begin()+v2.size()-1);
                            }
                            
                            final = final + "TO_DATE('"+ d + "', 'YYYY-MM-DD'), ";
                        }
                        else
                        {
                            size_t found = v.at(0).find("'");
                            if (found != std::string::npos)
                            {
                                v.at(0).insert(found, 1, '\'');
                            }

                            final = final + "'" + v.at(0) + "'" + ", ";
                        }
                    }
                    else
                    {
                        final = final + v.at(0) + ", ";
                    }
                }
            }
            v.erase(v.begin());
        }
    }
}


// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
