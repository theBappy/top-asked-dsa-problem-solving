class Solution {
public:
    int countOneBit(int num){
        int count = 0;
        while(num != 0){
            count += num & 1;
            num >>= 1;
        }
        return count;
    }
    vector<int> sortByBits(vector<int>& arr) {
        auto lambda= [&](int &a, int&b){
            int CA = countOneBit(a);
            int CB = countOneBit(b);
            if(CA == CB)
                return a < b;
            return CA < CB;
        };
        sort(begin(arr), end(arr), lambda);
        return arr;
    }
};



// Tc = O(n.logn)
class Solution {
public:
    vector<int> sortByBits(vector<int>& arr) {
        auto lambda= [&](int &a, int&b){
            int CA = __builtin_popcount(a);
            int CB = __builtin_popcount(b);
            if(CA == CB)
                return a < b;
            return CA < CB;
        };
        sort(begin(arr), end(arr), lambda);
        return arr;
    }
};