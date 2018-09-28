/*
  给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

  示例 1:

  输入: num1 = "2", num2 = "3"
  输出: "6"
  示例 2:

  输入: num1 = "123", num2 = "456"
  输出: "56088"
  说明：

  num1 和 num2 的长度小于110。
  num1 和 num2 只包含数字 0-9。
  num1 和 num2 均不以零开头，除非是数字 0 本身。
  不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
*/

//author = Qiufeng

class Solution {
public:
	string multiply(string num1, string num2) {
		int num1Length = num1.length();			//将字符串的长度
		int num2Length = num2.length();
		vector<int> num1array;					//将字符串转换为的数组
		vector<int> num2array;

		if (num1 == "0")						//若相乘数为0,则直接返回为"0"的数
			return num1;
		if (num2 == "0")
			return num2;

		int i = 0;

		while (num1Length > i)				   //将字符转换为int类型的数字存储在数组中
		{
			num1array.push_back(num1[i] - '0');
			i++;
		}

		i = 0;
		while (num2Length > i)					//将字符转换为int类型的数字存储在数组中
		{
			num2array.push_back(num2[i] - '0');
			i++;
		}

		int Length = num1Length + num2Length;	//相乘的两数的位数

		vector<int> Sum(Length);				//相乘两数的数组
		for (int i = 0; i < Length; i++)		//将数组各个位初始化为0
		{
			Sum[i] = 0;
		}

		for (int j = num2Length - 1; j >= 0; j--)		
		{
			int add = 0;						//每一位数相乘后的进位值
			int add1 = 0;						//数组中的数的进位值
			int b = 0;							//每一位相乘后的数后面需要添加的0的个数
			for (int k = num1Length - 1; k >= 0; k--)
			{
				int temp = num1array[k] * num2array[j];			//相乘值
				Sum[Length - b - 1 - (num2Length - 1 - j)] += temp % 10 + add1 + add;		//相乘后的每一位的值，可能会大于10
				add = temp / 10;								//进位值
				add1 = Sum[Length - b - 1 - (num2Length - 1 - j)] / 10;			//数组中的数的进位值
				Sum[Length - b - 1 - (num2Length - 1 - j)] %= 10;				//只保留个位数
				b++;															
				if (k == 0)						//最高位的值
				{
					if (Sum[Length - b - 1 - (num2Length - 1 - j)] == 0)
					{
						Sum[Length - b - 1 - (num2Length - 1 - j)] = add + add1;
					}
				}
			}
		}
        }

        string cct = "";
        int ant = 0;
        while (Sum.size() > ant)
        {
            if (ant == 0 && Sum[ant] == 0)
            	;
            else
                cct += (Sum[ant] + '0');
            ant++;
        }
        
        return cct;
    }
};
