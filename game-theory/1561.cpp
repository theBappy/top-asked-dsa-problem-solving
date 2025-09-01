

class Solution {
public:
    int maxCoins(vector<int>& piles) {
        int n = piles.size();
        int result = 0;
        sort(begin(piles), end(piles));
        int bob = 0;
        int me = n - 2;
        // int alice = n - 1;
        while (me > bob) {
            result += piles[me];
            me -= 2;
            bob++;
            // alice -= 2;
        }
        return result;
    }
};

class Solution {
public:
    int maxCoins(vector<int>& piles) {
        int n = piles.size();
        int result = 0;
        sort(begin(piles), end(piles));
        for(int M = n/3; M < n; M += 2){
            result += piles[M];
        }
        return result;
    }
};