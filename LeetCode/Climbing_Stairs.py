import math

class Solution(object):
    def count_num(self, n): # n = 7
        addends = []
        count_2 = n // 2
        if count_2 * 2 != n:
            addends.extend([2] * count_2)
            addends.append(1)
        else:
            addends.extend([2] * count_2)
        return addends

    def climbStairs(self, number):
        addends = self.count_num(number)
        answer = 0
        while 2 in addends:
            count_2 = addends.count(2)
            count_1 = addends.count(1)
            current_answer = math.factorial(len(addends)) / (math.factorial(count_1) * math.factorial(count_2))
            answer += current_answer
            addends.remove(2)
            addends.extend([1] * 2)
        return int(answer + 1)