class Solution {
public:
    typedef pair<int, int> P; // freq, element
    int findTopXSum(unordered_map<int, int>& mp, int x) {
        // min-heap
        priority_queue<P, vector<P>, greater<P>> pq;
        for (auto& it : mp) { //O(k) -> k size subarray + log(k)-> for pq push
            pq.push({it.second, it.first});
            if (pq.size() > x) {
                pq.pop();
            }
        }
        int sum = 0;
        while (!pq.empty()) { //O(k)
            auto [freq, val] = pq.top();
            pq.pop();
            sum += freq * val;
        }
        return sum;
    }
    vector<int> findXSum(vector<int>& nums, int k, int x) {
        int n = nums.size();
        unordered_map<int, int> mp;
        vector<int> result;
        int i = 0;
        int j = 0;
        //Tc = O(n*klogk)
        //Sc = O(k)
        while (j < n) { //O(n)
            mp[nums[j]]++;
            if (j - i + 1 == k) {
                result.push_back(findTopXSum(mp, x));
                mp[nums[i]]--;
                if (mp[nums[i]] == 0) {
                    mp.erase(nums[i]);
                }
                i++;
            }
            j++;
        }
        return result;
    }
};