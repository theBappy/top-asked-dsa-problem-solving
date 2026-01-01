//T.C : O(n) 
//S.C : O(1)
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();

        int i = n-1; //Start from LSB like usual math addition

        while(i >= 0) {
            if(digits[i] < 9) {
                digits[i] += 1;
                return digits;
            }

            //else we did get 9
            digits[i] = 0; //9+1 = 10
            i--;
        }

        digits.insert(begin(digits), 1); //1 is the carry forwarded till the end

        return digits;


    }
};