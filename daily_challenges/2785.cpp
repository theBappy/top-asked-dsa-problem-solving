// A->Z = 65-90
// a->z = 97 - 122

// Tc = O(n.logn)
// Sc = O(n)

class Solution {
public:
    bool isVowel(char ch) {
        ch = tolower(ch);
        return (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u');
    }
    string sortVowels(string s) {
        string temp;
        for (char& ch : s) {
            if (isVowel(ch)) {
                temp.push_back(ch);
            }
        }
        sort(begin(temp), end(temp));
        int j = 0;
        for (int i = 0; i < s.length(); i++) {
            if (isVowel(s[i])) {
                s[i] = temp[j];
                j++;
            }
        }
        return s;
    }
};



class Solution {
public:
    bool isVowel(char ch) {
        ch = tolower(ch);
        return (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u');
    }

    string sortVowels(string s) {
        unordered_map<char, int> mp;

        for (char& ch : s) {
            if (isVowel(ch)) {
                mp[ch]++;
            }
        }

        string temp = "AEIOUaeiou";

        int j = 0;

        for (int i = 0; i < s.length(); i++) {

            if (isVowel(s[i])) {
                while (mp[temp[j]] == 0) {
                    j++;
                }

                s[i] = temp[j];
                mp[temp[j]]--;
            }
        }

        return s;
    }
};