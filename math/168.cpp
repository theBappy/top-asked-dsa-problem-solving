class Solution {
public:
    string convertToTitle(int columnNumber) {
        string result;
        while(columnNumber > 0){
           columnNumber--; // excel column start at 1 (not 0), so decrement column number by 1 before taking the modulo, so adjusting the number zero based indexing
           int remainder = columnNumber%26;
           char ch = remainder + 'A';
           result.push_back(ch);

           columnNumber = columnNumber / 26; 
        }
        reverse(begin(result), end(result));
        return result;
    }
};
