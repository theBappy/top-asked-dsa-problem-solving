// Google

// A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
// a, a + d, a + 2d, a + 3d + ... + (a+(n-1)d)

class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        sort(begin(arr), end(arr)); // O(n.logn)
        int n = arr.size();
        int d = arr[1] - arr[0];
        for(int i = 2; i < n; i++){ // O(n)
            if(arr[i] - arr[i-1] != d){
                return false;
            }
        }
        return true;
    }
};

// first element always minimum and last element always max
// TC = O(n)
// Sc = O(n)
class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        int n = arr.size();
        unordered_set<int> st(begin(arr), end(arr));
        int min_el = *min_element(begin(arr), end(arr));
        int max_el = *max_element(begin(arr), end(arr));
        if((max_el - min_el) % (n-1) != 0)
            return false;
        int d = (max_el - min_el) / (n-1);
        int i = 0;
        while(i < n){
            int num = min_el + i*d;
            if(st.find(num) == st.end())
                return false;
            i++;
        }
        return true;
    }
};

// Approach-3
// Tc = O(n)
// Sc = O(1)
class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        int n = arr.size();
        int min_el = *min_element(begin(arr), end(arr));
        int max_el = *max_element(begin(arr), end(arr));
        if ((max_el - min_el) % (n - 1) != 0)
            return false;
        int d = (max_el - min_el) / (n - 1);
        int i = 0;
        while (i < n) {
            int val = arr[i];
            if (arr[i] == min_el + i * d)
                i++;
            else {
                if ((val - min_el) % d != 0)
                    return false;
                int j = (val - min_el) / d;
                if (val == arr[j])
                    return false;
                swap(arr[i], arr[j]);
            }
        }
        return true;
    }
};