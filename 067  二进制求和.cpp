/*
  给定两个二进制字符串，返回他们的和（用二进制表示）。

  输入为非空字符串且只包含数字 1 和 0。

  示例 1:

  输入: a = "11", b = "1"
  输出: "100"
  示例 2:

  输入: a = "1010", b = "1011"
  输出: "10101"
*/

//author = Qiufeng

#include<stack>
#include<vector>

class Solution {
    public:
    string addBinary(string a, string b) {
        stack<int> aa;
        stack<int> bb;

        for(int i = 0;i<a.length();i++)
        {
            aa.push(a[i] - '0');
        }

        for (int j = 0;j<b.length();j++)
        {
            bb.push(b[j] - '0');
        }

        stack<int> cc;

        int temp = 0;
        while (aa.size() != 0 || bb.size() != 0)
        {
            if (aa.size() == 0)
                aa.push(0);
            if (bb.size() == 0)
                bb.push(0);

            cc.push((aa.top() + bb.top()+temp)%2);
            temp = (aa.top() + bb.top() + temp) / 2;
            aa.pop();
            bb.pop();
            if (aa.size() == 0 && bb.size() == 0)
                if (temp == 1)
                    cc.push(1);
        }

        string result;
        while (cc.size())
        {
            result += cc.top()+'0';
            cc.pop();
        }

        return result;
    }
};
