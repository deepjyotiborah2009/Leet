class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans = float('inf')
        for i in range(len(words)):
                if words[i] == target:
                    direct = abs(i - startIndex)
                    circular = len(words) - direct
                    ans = min(ans, min(direct, circular))
        return ans if ans != float('inf') else -1
        