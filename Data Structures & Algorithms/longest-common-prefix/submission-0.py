class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []

        for m in range(len(strs[0])):

            for i in range(1, len(strs)):

                if m >= len(strs[i]) or strs[i][m] != strs[0][m]:
                    return "".join(res)

            res.append(strs[0][m])

        return "".join(res)