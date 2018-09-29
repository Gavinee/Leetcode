/*
  给出一个区间的集合，请合并所有重叠的区间。

  示例 1:
  输入: [[1,3],[2,6],[8,10],[15,18]]
  输出: [[1,6],[8,10],[15,18]]
  解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
  
  示例 2:
  输入: [[1,4],[4,5]]
  输出: [[1,5]]
  解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
*/

//author = Qiufeng

/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals) {
        if (intervals.size() == 0)
            return intervals;

        BubbleSort(intervals);
        vector<Interval> result;

        result.push_back(intervals[0]);
        for (int i = 1; i < intervals.size(); i++)
        {
            if (result[result.size() - 1].end >= intervals[i].start)
            {
                if (result[result.size() - 1].end < intervals[i].end)
                {
                    result[result.size() - 1].end = intervals[i].end;
                }
            }
            else
            {
                result.push_back(intervals[i]);
            }
        }
        return result;
    }

    void BubbleSort(vector<Interval>& intervals)
    {

        for (int i = 0; i < intervals.size(); i++)
        {
            for (int j = 0; j < intervals.size() - i - 1; j++)
            {
                if (intervals[j].start > intervals[j + 1].start)
                {
                    Interval temp;
                    temp = intervals[j];
                    intervals[j] = intervals[j + 1];
                    intervals[j + 1] = temp;
                }
            }
        }
    }
};
