/*
  给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

  例如：
  给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
  返回锯齿形层次遍历如下：

  [
    [3],
    [20,9],
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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> temp;
        vector<vector<int>> cmt;
        int deep = 1;
        deepOrder(root, deep, temp);

        for(int i = 0;i < temp.size(); i++)
        {
            vector<int> tty;
            for(int j = 0;j<temp[i].size();j++)
            {
                if(i%2==0)
                    tty.push_back(temp[i][j]);            
                else
                    tty.push_back(temp[i][temp[i].size()-1-j]);
            }
            cmt.push_back(tty);
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
