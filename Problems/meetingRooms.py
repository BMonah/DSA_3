"""
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (
start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]

Output: false
Explanation:

(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict
Example 2:

Input: intervals = [(5,8),(9,15)]

Output: true
Note:

(0,8),(8,10) is not considered a conflict at 8

"""
# we first sort the the contents of the array using the start time nlogn
# we sort so that we do not end up comparing each interval with each other but rather each interval with the previous one
# After sorting we just start at the beginning and skip through
# next we just compare the end time of the first interval to the start time of the next interval
# key parameter allows us to use the lambda function using a comparison key extracted from each element in the list


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solutions:
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False

        return True


intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
intervals2 = [Interval(0, 4), Interval(4, 10), Interval(15, 20)]
print(Solutions().canAttendMeetings(intervals))
