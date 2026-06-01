class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    #Create stack to hold elements until an operand seen,
    #pop 2 elements from stack 
    #calculate using operand and push back into stack 
    #pop last element remaining which is result
        polishStack = []
        for token in tokens: 
            if (token not in "+-*/"):
                polishStack.append(int(token))
            else:
                rightOp = polishStack.pop()
                leftOp = polishStack.pop()
                if(token == "+"):
                    newCalc = leftOp + rightOp
                    polishStack.append(newCalc)
                elif(token == "-"):
                    newCalc = leftOp - rightOp
                    polishStack.append(newCalc)
                elif(token == "*"):
                    newCalc = leftOp * rightOp
                    polishStack.append(newCalc)
                else:
                    newCalc = int(leftOp/rightOp)
                    polishStack.append(newCalc)
        return polishStack.pop()