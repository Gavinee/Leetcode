/*
  给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

  最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

  你可以假设除了整数 0 之外，这个整数不会以零开头。

  示例 1:
  输入: [1,2,3]
  输出: [1,2,4]
  解释: 输入数组表示数字 123。
  
  示例 2:
  输入: [4,3,2,1]
  输出: [4,3,2,2]
  解释: 输入数组表示数字 4321。
*/

//author = Qiufeng

//程序一   8ms
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        
        int index = digits.size()-1;
        int on = 0;
        while(index>=0)
        {
            
            if(index == digits.size()-1)
                digits[index] = digits[index] + 1;
            digits[index] = digits[index]+on;
            on = digits[index]/10;
            if(on<1)
                return digits;
            digits[index]%=10;
            if(index==0)
            {
                vector<int> temp;
                temp.push_back(1);
                for(int i = 0;i<digits.size();i++)
                {
                    temp.push_back(digits[i]);
                }
                return temp;
            }
            index--;
        }
        return digits;
    }
};


//程序二   4ms

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        
        int index = digits.size()-1;
        int on = 0;
        while(index>=0)
        {
            
            if(index == digits.size()-1)
                digits[index] = digits[index] + 1;
            digits[index] = digits[index]+on;
            on = digits[index]/10;
            if(on<1)
                return digits;
            digits[index]%=10;
            if(index==0)
            {
                digits.insert(digits.begin(),1);
                return digits;
            }
            index--;
        }
        return digits;
    }
};
