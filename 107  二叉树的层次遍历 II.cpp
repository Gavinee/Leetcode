/*
  给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

  例如：
  给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
  返回其自底向上的层次遍历为：

  [
    [15,7],
    [9,20],
    [3]
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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> temp;
        vector<vector<int>> cmt;
        int deep = 1;
        deepOrder(root, deep, temp);
        
        for(int i = 0;i<temp.size();i++)
        {
            cmt.push_back(temp[temp.size()-1-i]);
        }
        return cmt;
        
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
