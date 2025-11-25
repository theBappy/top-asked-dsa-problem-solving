
class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        int maxSum = INT_MIN;
        int resultLevel = 0;
        queue<TreeNode*> q;
        q.push(root);
        int currLevel = 1;
        while (!q.empty()) {
            int n = q.size();
            int sum = 0;
            while (n--) {
                TreeNode* temp = q.front();
                q.pop();

                sum += temp->val;
                if (temp->left) {
                    q.push(temp->left);
                }
                if (temp->right) {
                    q.push(temp->right);
                }
            }
            if (sum > maxSum) {
                maxSum = sum;
                resultLevel = currLevel;
            }
            currLevel++;
        }
        return resultLevel;
    }
};





class Solution {
public:
    map<int, int> mp;
    void DFS(TreeNode* root, int level) {
        if (root == NULL) {
            return;
        }
        mp[level] += root->val;
        DFS(root->left, level + 1);
        DFS(root->right, level + 1);
    }
    int maxLevelSum(TreeNode* root) {
        mp.clear();
        DFS(root, 1);
        int maxSum = INT_MIN;
        int result_level = 0;
        for (auto& it : mp) {
            int level = it.first;
            int sum = it.second;
            if (sum > maxSum) {
                maxSum = sum;
                result_level = level;
            }
        }
        return result_level;
    }
};