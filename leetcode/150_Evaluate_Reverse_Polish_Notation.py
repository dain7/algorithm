class Solution(object):
    def evalRPN(self, tokens):
        stack = [] # 숫자 담는 스택
        for t in tokens:
            if t not in "+-*/": # 기호가 아니면 숫자를 넣음
                stack.append(int(t))
            else: # 기호일 경우엔
                r, l = stack.pop(), stack.pop() # 두개를 뺌
                # 기호 맞게 연산함
                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else:
                    stack.append(int(float(l)/r))
        return stack.pop()