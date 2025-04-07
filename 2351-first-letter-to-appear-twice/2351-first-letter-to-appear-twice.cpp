class Solution {
public:
    char repeatedCharacter(string s) {
        unordered_map<char, int> twice;
        for (auto num : s) {
            twice[num]++;
            if (twice[num] == 2) return num;
        }
        return ' ';
    }
};

