class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Create res and stack
        res = [0] * len(temperatures)
        monoStack = []

        for i in range(len(temperatures)):
            while(monoStack != [] and (temperatures[i]>temperatures[monoStack[-1]])):
                prev_day = monoStack.pop()
                res[prev_day] = i-prev_day
            monoStack.append(i)
        return res