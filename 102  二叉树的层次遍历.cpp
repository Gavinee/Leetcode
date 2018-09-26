/*
  给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

  例如:
  给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
   
  返回其层次遍历结果：
  [
    [3],
    [9,20],
    [15,7]
  ]
*/

//author = Qiufeng

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) 
    {
        vector<vector<int>> temp;
        int deep = 1;
        deepOrder(root, deep, temp);
        return temp;
    }

    void deepOrder(TreeNode* root, int deep, vector<vector<int>>& temp)
    {
        if (root == NULL)
            return;
        if (deep > temp.size())
        {
            vector<int> tt;
            for (int i = temp.size(); i < deep; i++)
                temp.push_back(tt);
        }
        temp[deep-1].push_back(root->val);
        deepOrder(root->left, deep + 1, temp);
        deepOrder(root->right, deep + 1, temp);
    }
};
