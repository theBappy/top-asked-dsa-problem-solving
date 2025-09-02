class Solution {
public:
    int sum = 0;
    
    int getCountDigits(int num) {
        sum = 0;
        int count = 0;
        
        while(num) {
            sum += num % 10;
            num /= 10;
            count++;
        }
        
        return count;
        
    }
    
    int addDigits(int num) {
        
        while(getCountDigits(num) > 1) {
            num = sum;
        }
        
        return sum;
        
    }
};


class Solution {
public:
    int addDigits(int num) {
        if(num == 0)
            return 0;
        if(num % 9 == 0)
            return 9;
        else 
            return num % 9;
    }
};