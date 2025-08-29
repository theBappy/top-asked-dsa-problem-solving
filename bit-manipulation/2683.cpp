// Approach-1
class Solution {
public:
    bool doesValidArrayExist(vector<int>& derived) {
        int n = derived.size();

        vector<int> original(n);
        original[0] = 0;
        for (int i = 0; i < n - 1; i++) {
            original[i + 1] = original[i] ^ derived[i];
        }
        if (original[n - 1] ^ original[0] == derived[n - 1]) {
            return true;
        }

        original[0] = 1;
        for (int i = 0; i < n - 1; i++) {
            original[i + 1] = original[i] ^ derived[i];
        }
        if (original[n - 1] ^ original[0] == derived[n - 1]) {
            return true;
        }
        return false;
    }
};


class Solution {
public:
    bool doesValidArrayExist(vector<int>& derived) {
        int XOR = 0;

        for(int &x : derived) {
            XOR  = (XOR ^ x);
        }

        return XOR == 0;
    }
};