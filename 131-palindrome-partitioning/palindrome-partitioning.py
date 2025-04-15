class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if (len(s) == 1):
            return [[s]]
        if len(s) == 0:
            return []

        palendromicCache = [[] for idx in range(len(s) + 1)]
        palendromicCache[0].append([])

        for idx in range(1, len(s) + 1):
            strEndIdx = idx - 1
            for idx2 in range(idx, 0, -1):
                strStartIdx = idx2 - 1
                if isPalindrome(s[strStartIdx: strEndIdx + 1]):
                    prefixPalendroms = palendromicCache[idx2 - 1]
                    for palendrom in prefixPalendroms:
                        palendromicCache[idx].append(palendrom + [s[strStartIdx: strEndIdx + 1]])
        return palendromicCache[-1]


def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
