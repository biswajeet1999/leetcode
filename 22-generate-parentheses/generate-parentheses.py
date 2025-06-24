class Solution:
    # O((2 ^ 2n) * n) time, O((2 ^ n) * 2n) space
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curParenthesis = []
        self.generateParenthesisUtil(n, n, curParenthesis, res)
        return res

    def generateParenthesisUtil(self, openCount, closeCount, cur, res):
        if openCount == 0 and closeCount == 0:
            res.append("".join(cur))
            return
        
        if openCount > 0:
            cur.append("(")
            self.generateParenthesisUtil(openCount - 1, closeCount, cur, res)
            cur.pop()
        
        if closeCount > openCount:
            cur.append(")")
            self.generateParenthesisUtil(openCount, closeCount - 1, cur, res)
            cur.pop()
        












