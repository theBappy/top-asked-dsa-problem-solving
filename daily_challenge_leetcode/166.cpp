//T.C : O(denominator) approximately
//S.C : O(1)

class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0)
            return "0";
        string result;
        if ((long long)numerator * (long long)denominator < 0)
            result += '-';
        long long absNumerator = labs(numerator);
        long long absDenominator = labs(denominator);

        long long integerDiv = absNumerator / absDenominator;
        result += to_string(integerDiv); //log(10(integerDiv))

        long long remainder = absNumerator % absDenominator;
        if (remainder == 0)
            return result;
        result += '.';

        unordered_map<int, int> mp;
        // 0 <= remainder <= denominator
        // O(denominator + length) [insert only once]
        while (remainder != 0) {
            if (mp.count(remainder)) {
                result.insert(mp[remainder], "("); //O(length)
                result += ")";
                break;
            }
            mp[remainder] = result.length();
            remainder *= 10;
            int digit = remainder / absDenominator;
            result += to_string(digit); //O(1)

            remainder = remainder % absDenominator;
        }
        return result;
    }
};