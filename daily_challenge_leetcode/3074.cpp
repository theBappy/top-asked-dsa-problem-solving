//Approach-1 (Using std::sort so that we can Simply assign the apples to largest boxes first)
//T.C : O(n + mlogm) 
//S.C : O(1)

class Solution {
public:
    int minimumBoxes(vector<int>& apple, vector<int>& capacity) {
        sort(begin(capacity), end(capacity), greater<int>());
        int totalApple = accumulate(begin(apple), end(apple), 0);
        int count = 0;
        int i = 0;
        while (totalApple > 0) {
            totalApple -= capacity[i];
            count++;
            i++;
        }
        return count;
    }
};


//Approach-2 (Using counting sort so that we can Simply assign the apples to largest boxes first)
//T.C : O(n + m) 
//S.C : O(1)
class Solution {
public:
    int minimumBoxes(vector<int>& apple, vector<int>& capacity) {
        int totalApples = accumulate(begin(apple), end(apple), 0);
        vector<int> freq(51, 0);
        for (int cap : capacity) {
            freq[cap]++;
        }
        int count = 0;
        for (int cap = 50; cap >= 1 && totalApples > 0; cap--) {
            while (freq[cap] > 0 && totalApples > 0) {
                totalApples -= cap;
                freq[cap]--;
                count++;
            }
        }
        return count;
    }
};