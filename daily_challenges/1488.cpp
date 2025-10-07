//Approach (Binary search along with map and set and greedy)
//T.C : O(n*logn)
//S.C : O(n)
class Solution {
public:
    vector<int> avoidFlood(vector<int>& rains) {
        int n = rains.size();

        unordered_map<int, int> map;   // lake -> last day it was filled
        set<int> dryDays;              // indices of dry days (rains[day] == 0)
        vector<int> ans(n, 1);         // default all dry days to dry lake 1

        for (int day = 0; day < n; day++) {
            int lake = rains[day];

            if (lake == 0) {
                dryDays.insert(day);                     // record this dry day
            } else {
                ans[day] = -1;                           // raining day — can't dry any lake

                if (map.count(lake)) {
                    // lake already filled previously
                    auto it = dryDays.lower_bound(map[lake] + 1);   // next dry day after it was last filled

                    if (it == dryDays.end()) {
                        // no dry day available to empty this lake before raining again → flood
                        return {};
                    }

                    ans[*it] = lake;                     // use this dry day to dry the lake
                    dryDays.erase(it);
                }

                map[lake] = day;                         // record latest day this lake was filled
            }
        }

        return ans;
    }
};
