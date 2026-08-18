class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = [0] * 128

        for c in t:
            need[ord(c)] += 1

        left = 0
        count = len(t)

        best_start = 0
        best_len = float("inf")

        for right in range(len(s)):
            r = ord(s[right])

            if need[r] > 0:
                count -= 1

            need[r] -= 1

            while count == 0:
                window_len = right - left + 1

                if window_len < best_len:
                    best_len = window_len
                    best_start = left

                l = ord(s[left])
                need[l] += 1

                if need[l] > 0:
                    count += 1

                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_start:best_start + best_len]
