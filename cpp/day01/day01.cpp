#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

int main()
{
    std::ifstream file("../../input/day01.txt");

    std::vector<int> left, right;

    // Read input into two vectors
    int a, b;
    while (file >> a >> b) {
        left.push_back(a);
        right.push_back(b);
    }

    file.close();

    // Sort the vectors
    std::sort(left.begin(), left.end());
    std::sort(right.begin(), right.end());

    // Calculate the total distance
    int total_distance = 0;
    for (int i = 0; i < left.size(); i++) {
        total_distance += abs(left[i] - right[i]);
    }

    std::cout << "Total distance: " << total_distance << std::endl;

    // Calculate the similarity score
    int similarity_score = 0;
    for (int i = 0; i < left.size(); i++) {
        int n_occurences = std::count(right.begin(), right.end(), left[i]);
        similarity_score += left[i] * n_occurences;
    }

    std::cout << "Similarity score: " << similarity_score << std::endl;

    return 0;
}
