//Approach-1 (Recur + Memo)
//T.C : O(n*k + m*k)
//S.C : O(m*k)

class Solution {
public:
    int m;
    int k;
    const int MOD = 1e9+7;
    int t[1001][1001];
    
    int solve(int i, int j, vector<vector<long long>>& freq, string &target) {
        if(i == m)
            return 1;
        
        if(j == k)
            return 0;
        
        if(t[i][j] != -1)
            return t[i][j];
        
        int not_taken = solve(i, j+1, freq, target)%MOD;
        
        int taken     = (freq[target[i] - 'a'][j] * solve(i+1, j+1, freq, target))%MOD;
        
        
        return t[i][j] = (not_taken + taken)%MOD;
    }
    
    int numWays(vector<string>& words, string target) {
        
        k = words[0].size();
        m = target.length();
        
        vector<vector<long long>> freq(26, vector<long long>(k));
        
        for(int col = 0; col < k; col++) {
            
            for(string &word : words) {
                
                char ch = word[col];
                freq[ch-'a'][col]++;
                
            }
            
        }
        memset(t, -1, sizeof(t));
        return solve(0, 0, freq, target);
    }
};