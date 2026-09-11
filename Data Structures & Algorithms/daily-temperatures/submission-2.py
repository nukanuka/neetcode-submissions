class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stackTemps = []
        out = [0] * len(temperatures)
        for t in range(len(temperatures)): 
        # While stack is not empty AND the current temp is      greater  # than the temp of the day at the top of the stack
            while(len(stackTemps) and temperatures[t] > temperatures[stackTemps[-1]]):
                prev = stackTemps.pop()
                out[prev] = t - prev
            
            stackTemps.append(t)
        
        return out

                