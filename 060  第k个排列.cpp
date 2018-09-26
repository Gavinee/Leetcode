/*
  给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

  按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

  "123"
  "132"
  "213"
  "231"
  "312"
  "321"
  给定 n 和 k，返回第 k 个排列。

  说明：

  给定 n 的范围是 [1, 9]。
  给定 k 的范围是[1,  n!]。
  示例 1:

  输入: n = 3, k = 3
  输出: "213"
*/

//author = Qiufeng

class Solution {
public:
    string getPermutation(int n, int k) {

        string tt="";
        string count="";
        int temp = k;
        vector<int> index;
        index.push_back(0);
        string Finally="";
        for (int i = 0; i < n; i++)
            tt+=('1'+i);
        Permutation(tt,count,Finally,temp,index);
        return Finally;
    }

    void Permutation(string tt, string& count,string& Finally,int temp, vector<int>& index)
    {
        if (tt.length() == 0)
        {
            index[0]++;
            if (index[0] == temp)
            {
                for (int i = 0; i < count.length(); i++)
                    Finally += count[i];
            }

            return;
        }

        for (int i = 0; i < tt.length(); i++)
        {
            string cmt="";
            for (int j = 0; j < tt.length(); j++)
            {
                if (i != j)
                    cmt += tt[j];
                else
                    count += tt[j];
            }
            Permutation(cmt, count,Finally, temp,index);
            count = count.substr(0, count.length() - 1);
            if (index[0] == temp)
                return;
        }
    }
};
