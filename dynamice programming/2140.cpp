class Solution {
public:
    int n;
    long long solve(int i, vector<vector<int>>& q, vector<long long>& t) {
        if (i >= n)
            return 0;
        if (t[i] != -1)
            return t[i];
        
        // Points if we take the current question
        long long taken = q[i][0] + solve(i + (q[i][1] + 1), q, t);
        // Points if we do not take the current question
        long long not_taken = solve(i + 1, q, t);
        
        // Store the result in memoization array
        return t[i] = max(taken, not_taken);
    }

    long long mostPoints(vector<vector<int>>& q) {
        n = q.size();
        vector<long long> t(n, -1);  // Correct size for memoization
        return solve(0, q, t);
    }
};


    
//  Bottom up
// State definition, t[i] = max points gained by questions from [i -> n-1]
// return t[0] -> [0 to n-1]
// Bottom up
class Solution {
public:

    long long mostPoints(vector<vector<int>>& questions) {
        int n = questions.size();
        
        if(n == 1)
            return questions[0][0];
        
        vector<long long> t(200001);
        //t[i] = Max points gained by Questions from questions[i to n-1]
        //return t[0] - from 0 to n-1

        
        for(int i = n-1; i >= 0; i--) {
            t[i] = max(questions[i][0] + t[i + questions[i][1] + 1], t[i+1]);
        }
        
        return t[0];
    }
};