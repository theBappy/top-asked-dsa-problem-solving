// any number falls [a-k, a + k] can be converted to a
// always better to have element (max freq) which already exists in num array

class Solution
{
public:
    int maxFrequency(vector<int> &nums, int k, int numOperations)
    {
        int maxEl = *max_element(begin(nums), end(nums)) + k;
        vector<int> freq(maxEl + 1, 0);
        for (int &num : nums)
        {
            freq[num]++;
        }
        // Tc = O(maxEl)
        //  Sc = O(maxEl)
        //  cumulative sum of freq
        for (int i = 1; i <= maxEl; i++)
        {
            freq[i] += freq[i - 1];
        }
        int result = 0;
        for (int target = 0; target <= maxEl; target++)
        {
            if (freq[target] == 0)
            {
                continue;
            }
            int leftNum = max(0, target - k);
            int rightNum = min(maxEl, target + k);

            int totalCount = freq[rightNum] - (leftNum > 0 ? freq[leftNum - 1] : 0);

            int targetCount =
                freq[target] - (target > 0 ? freq[target - 1] : 0);

            int needConversion = totalCount - targetCount;
            int maxPossibleFreq =
                targetCount + min(needConversion, numOperations);
            result = max(result, maxPossibleFreq);
        }
        return result;
    }
};