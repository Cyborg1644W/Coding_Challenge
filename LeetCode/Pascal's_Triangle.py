class Solution(object):
    def getRow(self, rowIndex):
        nth_row = [[1]]
        for _ in range(rowIndex):
            current_row = []
            if len(nth_row[-1]) >= 2:
                number = len(nth_row[-1]) - 1
                for i in range(0, number):
                    add = nth_row[-1][i] + nth_row[-1][i + 1]
                    current_row.append(add)
            current_row.append(1)
            current_row.insert(0, 1)
            nth_row.append(current_row)
        return nth_row[rowIndex]
    
class Solution(object):
    def generate(self, numRows):
        nth_row = [[1]]
        for _ in range(numRows-1):
            current_row = []
            if len(nth_row[-1]) >= 2:
                number = len(nth_row[-1]) - 1
                for i in range(0, number):
                    add = nth_row[-1][i] + nth_row[-1][i + 1]
                    current_row.append(add)
            current_row.append(1)
            current_row.insert(0, 1)
            nth_row.append(current_row)
        return nth_row
