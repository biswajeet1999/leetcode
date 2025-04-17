class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cache = {}

        for idx in range(len(s)):
            char = s[idx]
            cache[char] = idx

        res = []
        maxIdxTillNow = 0
        length = 0
        for idx in range(len(s)):
            char = s[idx]
            maxIdxTillNow = max(maxIdxTillNow, cache[char])
            length += 1

            if maxIdxTillNow == idx:
                res.append(length)
                length = 0

        return res