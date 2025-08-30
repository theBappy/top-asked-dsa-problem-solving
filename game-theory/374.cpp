// Google, Microsoft


class Solution {
public:
    int guessNumber(int n) {
        int l = 1;
        int r = n;
        while(l <= r){
            int guess_no = l + ( r-l ) / 2;
            int val = guess(guess_no);
            if(val == 0)
                // we found the pick
                return guess_no;
            else if(val == -1)
                r = guess_no - 1;
            else
                l = guess_no + 1;
        }
        return -1;
    }
};