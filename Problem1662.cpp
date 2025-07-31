#include <string>
#include <iostream>
#include <vector>

bool arrayStringsAreEqual(std::vector<std::string>& word1, std::vector<std::string>& word2) {
  std::string full_word1 = "";
  std::string full_word2 = "";

  for (std::string i : word1){
    full_word1 += i;
  }

  for (std::string i: word2){
    full_word2 += i;
  }

  return full_word1 == full_word2;
}

