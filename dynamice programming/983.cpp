// Top-down(Recur+Memo)

class Solution {
public:
    int t[366];
    int solve(vector<int>& days, vector<int>& costs, int n, int i){
      if(i >= n)
        return 0; // can't travel so no costs
      if(t[i] != -1)
        return t[i];

      // 1 day pass
      int cost_1 = costs[0] + solve(days, costs, n, i+1);

      // 7 day pass
       int j = i;
       int max_day = days[i] + 7;
       while(j < n && days[j] < max_day){
        j++;
       }
       int cost_7 = costs[1] + solve(days, costs, n, j);

       // 30 day pass
       j = i;
       max_day = days[i] + 30;
       while(j < n && days[j] < max_day){
        j++;
       }
       int cost_30 = costs[2] + solve(days, costs, n, j);

        return t[i] min({cost_1, cost_7, cost_30});
    }
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int n = days.size();
        memset(t, -1, sizeof(t));
        return solve(days, costs, n, 0);
    }
};