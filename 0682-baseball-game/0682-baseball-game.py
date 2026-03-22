class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack =[]
        for op in operations:
            if op not in ("C","D","+"):
                stack.append(int(op))

            elif op == "C":
                if not stack:
                    continue
                else:
                    stack.pop()
            elif op == "D":
                num = stack[-1]
                stack.append(2*num)
            elif op == "+":
                num1 = stack[-1]
                num2 = stack[-2]
                stack.append(num1+num2)

        return sum(stack)