class Solution {
public:
    bool hasDuplicate(string &s1, string &s2){
        int arr[26] = {0};
        // check also this: {'aa', 'bb'}
        for(char &ch: s1){
            if(arr[ch-'a'] > 0)
                return true;
            arr[ch-'a']++;
        }
        for(char &ch: s2){
            if(arr[ch-'a'] > 0)
                return true;
        }
    return false; // no duplicate found at all
    }
    unordered_map<string, int> mp;
    int solve(int i, vector<string>& arr, string temp, int n){
        if(i >= n)
            return temp.length();
        int include = 0; 
        int exclude = 0;
        if(mp.find(temp) != mp.end()){
            return mp[temp];
        }
        if(hasDuplicate(arr[i], temp)){ // exclude only
            exclude = solve(i + 1, arr, temp, n);
        }
        else{ // include and exclude
            exclude = solve(i+1, arr, temp, n);
            include = solve(i+1, arr, temp+arr[i], n);
        }
        return mp[temp]=max(include, exclude);
    }
    int maxLength(vector<string>& arr) {
        string temp = ""; // no concatenation till now
        mp.clear();
        int n = arr.size();
        int i = 0;
        return solve(i, arr, temp, n);
    }
};