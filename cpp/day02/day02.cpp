#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>


bool isSafe(std::vector<int> report) {

    std::vector<int> difference;

    for (int i = 0; i < report.size() - 1; i++) {
        difference.push_back(report[i + 1] - report[i]);
    }

    std::vector<int>::iterator min_it = std::min_element(difference.begin(), difference.end());
    std::vector<int>::iterator max_it = std::max_element(difference.begin(), difference.end());

    int min = *min_it;
    int max = *max_it;

    if (((0 < min && min < 4) && (0 < max && max < 4)) || ((-4 < min && min < 0) && (-4 < max && max < 0))) {
        return true;
    }

    return false;
}


int main()
{
    std::ifstream file("../../input/day02.txt");

    int number_of_safe_reports = 0;
    int number_of_safe_dampened_reports = 0;

    // Read input lines
    std::string line;
    while (std::getline(file, line)) {
        
        std::istringstream stream(line);
        std::vector<int> report;
        int level;

        while (stream >> level) {
            report.push_back(level);
        }

        if (isSafe(report)) {
            number_of_safe_reports++;
        }

        for (int i = 0; i < report.size(); i++) {
            
            std::vector<int> dampened_report;
            for (int j = 0; j < report.size(); j++) {
                if (i != j) {
                    dampened_report.push_back(report[j]);
                }
            }

            if (isSafe(dampened_report)) {
                number_of_safe_dampened_reports++;
                break;
            }

        }
    }

    file.close();

    std::cout << "Number of safe reports: " << number_of_safe_reports << std::endl;
    std::cout << "Number of safe dampened reports: " << number_of_safe_dampened_reports << std::endl;

    return 0;
}