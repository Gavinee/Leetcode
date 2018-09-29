/*
  实现 int sqrt(int x) 函数。

  计算并返回 x 的平方根，其中 x 是非负整数。

  由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

  示例 1:
  输入: 4
  输出: 2
  
  示例 2:
  输入: 8
  输出: 2
  
  说明: 8 的平方根是 2.82842..., 
  由于返回类型是整数，小数部分将被舍去。
*/

//author = Qiufeng

class Solution {
public:
    int mySqrt(int x) {
        int start = 0;
        int end = x;

        while (end - start > 1)
        {
            long temp = (end + start) / 2;
            if (temp*temp > x)
            {
                end = temp;
            }
            else
            {
                start = temp;
            }
        }
        if (start*start == x)
            return start;
        if (end*end == x)
            return end;
        return start;
    }
};
