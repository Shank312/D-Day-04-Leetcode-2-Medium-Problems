
from collections import defaultdict

class Solution:

  def characterReplacement(s: str, k: int) -> int:
    

    left = 0                                     # left pointer
    max_count = 0                                # max frequency of a single char in current window
    freq = defaultdict (int)                     # frequency of each char
    result = 0                                   # result to store max length

    for right in range(len(s)):
        freq[s[right]]    += 1
        max_count = max(max_count, freq[s[right]])

        print(f"Window: {s[left:right+1]}, freq: {dict(freq)}, max_count: {max_count}")

        # If we need to replace more than k characters, shrink the window
        while(right-left+1) - max_count > k:
            print(f"Shrinking Window: too many replacements needed")
            freq[s[left]] -= 1
            left += 1

        current_window_size = right - left + 1
        result = right - left + 1
        result = max(result, current_window_size)
        print(f"Updated result: {result}, Current window: {s[left:right+1]}\n")

    return result

  characterReplacement("AABABBA", 1)




# Uploaded on leetcode

from collections import defaultdict

class Solution:
    def characterReplacement(self, s, k):
        left = 0
        max_count = 0
        freq = defaultdict(int)
        result = 0

        for right in range(len(s)):
            freq[s[right]] += 1
            max_count = max(max_count, freq[s[right]])

            while (right - left + 1) - max_count > k:
                freq[s[left]] -= 1
                left += 1

            current_window_size = right - left + 1
            result = max(result, current_window_size)

        return result