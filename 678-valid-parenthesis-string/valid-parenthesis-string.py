class Solution:
    # def checkValidString(self, s: str) -> bool:
    #     n = len(s)
    #     memo = [[-1] * n for _ in range(n)]
    #     return self.is_valid_string(0, 0, s, memo)

    # def is_valid_string(self, index: int, open_count: int, s: str, memo: List[List[int]]) -> bool:
        
    #     if index == len(s):
    #         return open_count == 0

        
    #     if memo[index][open_count] != -1:
    #         return memo[index][open_count] == 1

    #     is_valid = False
        
    #     if s[index] == '*':
    #         is_valid |= self.is_valid_string(index + 1, open_count + 1, s, memo)  # Treat '*' as '('
    #         if open_count > 0:
    #             is_valid |= self.is_valid_string(index + 1, open_count - 1, s, memo)  # Treat '*' as ')'
    #         is_valid |= self.is_valid_string(index + 1, open_count, s, memo)  # Treat '*' as empty
    #     else:
            
    #         if s[index] == '(':
    #             is_valid = self.is_valid_string(index + 1, open_count + 1, s, memo)  # Increment count for '('
    #         elif open_count > 0:
    #             is_valid = self.is_valid_string(index + 1, open_count - 1, s, memo)  # Decrement count for ')'

       
    #     memo[index][open_count] = 1 if is_valid else 0
    #     return is_valid

    def checkValidString(self, s: str) -> bool:
        left = []
        star = []

        for idx in range(len(s)):
            if s[idx] == '(':
                left.append(idx)
            elif s[idx] == '*':
                star.append(idx)
            else:
                if len(left) > 0:
                    left.pop()
                elif len(star) > 0:
                    star.pop()
                else:
                    return False
        
        while len(left) > 0 and len(star) > 0:
            if left.pop() > star.pop():
                return False
        return len(left) == 0


