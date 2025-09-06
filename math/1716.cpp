
// Tc = O(n)
class Solution {
public:
    int totalMoney(int n) {
        int result = 0;
        int monday_money = 1;
        while(n > 0){
            int money = monday_money;
            for(int day = 1; day <= min(n, 7); day++){
                result += money;
                money++;
            }
            n -= 7;
            monday_money++;
        }
        return result;
    }
};

// Tc = O(1)
class Solution {
public:
    int totalMoney(int n) {
        int terms = n / 7;

        int first = 28;
        int last = first + (terms - 1) * 7;
        int result = terms * (first + last) / 2; //formula use so O(1)

        int start_money = 1 + terms;
        for (int day = 1; day <= (n % 7); day++) {
            // n % 7 constant, it can be 1, 2,3,4, 5, 6 less than 7 week day, so it is constant => O(6) => O(1)
            result += start_money;
            start_money++;
        }
        return result;
    }
};