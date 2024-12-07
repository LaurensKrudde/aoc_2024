#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <chrono>
#include <map>


std::map<long long, std::vector<long long>> parseInput() {

    std::map<long long, std::vector<long long>> input_map;

    std::ifstream file("../../input/day07.txt");

    // Read input lines
    std::string line;
    while ((std::getline(file, line))) {

        // Colon ':' position
        size_t colon_pos = line.find(":");
        
        // Test value
        long long test_value = std::stoll(line.substr(0, colon_pos));
        
        // Values after colon
        std::istringstream stream(line.substr(colon_pos + 1));
        long long number;
        std::vector<long long> numbers;
        while (stream >> number) {
            numbers.push_back(number);
        }

        input_map[test_value] = numbers;
    }

    file.close();

    return input_map;

};


long long apply_operator(long long current_value, long long next_value, char op) {
    
    if (op == '+') {
        return current_value + next_value;
    } else if (op == '*') {
        return current_value * next_value;
    } else if (op == '|') {
        return std::stoll(std::to_string(current_value) + std::to_string(next_value));
    } else {
        return current_value;
    }
}


bool check(long long test_value, long long current_value, int i, std::vector<long long> numbers) {

    if (i == numbers.size()) {
        if (current_value == test_value) {
            return true;
        } else {
            return false;
        }
    } else if (current_value > test_value) {
        return false;
    } else {
        long long cur_value1 = apply_operator(current_value, numbers[i], '+');
        long long cur_value2 = apply_operator(current_value, numbers[i], '*');
        long long cur_value3 = apply_operator(current_value, numbers[i], '|');
        
        bool check1 = check(test_value, cur_value1, i+1, numbers);
        bool check2 = check(test_value, cur_value2, i+1, numbers);
        bool check3 = check(test_value, cur_value3, i+1, numbers);
        return check1 || check2 || check3;
    }

}


long long solve(std::map<long long, std::vector<long long>> input_map) {

    long long calibration_result = 0;

    for (const auto& pair : input_map) {

        // Check if test value can be obtained
        long long test_value = pair.first;
        std::vector<long long> numbers = pair.second;
        bool equation_true = check(test_value, numbers[0], 1, numbers);
        if (equation_true) {
            calibration_result += test_value;
        }
    }

    return calibration_result;
}


int main()
{

    // Parse input
    auto parse_start = std::chrono::high_resolution_clock::now();

    std::map<long long, std::vector<long long>> input_map = parseInput();

    auto parse_end = std::chrono::high_resolution_clock::now();

    double parse_time = std::chrono::duration<double, std::milli>(parse_end - parse_start).count();

    std::cout << "Parsing time: " << parse_time << " ms" << std::endl;


    // Solve
    auto t_start = std::chrono::high_resolution_clock::now();

    long long result = solve(input_map);

    auto t_end = std::chrono::high_resolution_clock::now();

    double execution_time = std::chrono::duration<double, std::milli>(t_end - t_start).count();

    std::cout << "Calibration result: " << result << std::endl;
    std::cout << "Execution time: " << execution_time << " ms" << std::endl;

    return 0;
}
