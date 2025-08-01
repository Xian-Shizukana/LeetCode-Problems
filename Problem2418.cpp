#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <limits>
#include <numeric>

// using namespace std;
using std::string;
using std::vector;

class Solution {
public:
  vector<string> sortPeople(vector<string>& names, vector<int>&heights) {

    vector<std::pair<int, string>> person_height = {};
    vector<string> sorted_height = {};   

    int names_size = names.size();

    for (int i = 0; i < names_size; i++){
      person_height.push_back(std::make_pair(heights[i], names[i]));
    }

    sort(person_height.rbegin(), person_height.rend());

    for (auto i : person_height) {
      sorted_height.push_back(i.second);
    }

    return sorted_height;
  }
};

int main() {
    Solution sol;

    // (variable) result = sol.func();
    // std::cout << result << std::endl;

    return 0;
}

