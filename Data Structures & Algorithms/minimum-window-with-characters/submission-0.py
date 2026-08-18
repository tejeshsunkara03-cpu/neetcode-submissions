class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}

        have = 0
        need_count = len(need)

        left = 0

        best_length = float("inf")
        best_left = 0
        best_right = 0

        for right in range(len(s)):

            char = s[right]

            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == need_count:

                window_length = right - left + 1

                if window_length < best_length:
                    best_length = window_length
                    best_left = left
                    best_right = right

                left_char = s[left]

                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_left:best_right + 1]
