class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n = s1.length();
        int m = s2.length();
        if(n > m){
            return false;
        }
        sort(begin(s1), end(s1));
        // T.C : O((m-n)*logn)
        // S.C : O(1) 
        for(int i = 0; i <= m-n; i++){
            string substring = s2.substr(i, n);
            sort(begin(substring), end(substring));
            if(s1 == substring){
                return true;
            }
        }
        return false;
    }
};


//T.C : O(m+n)
//S.C : O(26) => O(1)
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n = s1.length();
        int m = s2.length();
        if (n > m) {
            return false;
        }
        vector<int> s1_freq(26, 0);
        vector<int> s2_freq(26, 0);
        for (char& ch : s1) { //O(n)
            s1_freq[ch - 'a']++;
        }
        int i = 0;
        int j = 0;
        while (j < m) { //O(m)
            s2_freq[s2[j] - 'a']++;
            if (j - i + 1 > n) {
                // time to shrink the window
                s2_freq[s2[i] - 'a']--;
                i++;
            }
            if (s1_freq == s2_freq) {
                return true;
            }
            j++;
        }
        return false;
    }
};