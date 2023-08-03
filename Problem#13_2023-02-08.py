""" 
Problem :
Given an integer k and a string s, find the length of the longest substring 
that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, 
the longest substring with k distinct characters is "bcb".
"""

class Solution:
    def longest_substring_with_k_distinct_chars(s, k):
        if k == 0:
            return 0

        window_start = 0
        max_length = 0
        char_frequency = {}

        for window_end in range(len(s)):
            right_char = s[window_end]
            char_frequency[right_char] = char_frequency.get(right_char, 0) + 1

            # Shrink the window until we have at most k distinct characters in the window
            while len(char_frequency) > k:
                left_char = s[window_start]
                char_frequency[left_char] -= 1
                if char_frequency[left_char] == 0:
                    del char_frequency[left_char]
                window_start += 1

            # Update the maximum length of the window
            max_length = max(max_length, window_end - window_start + 1)

        return max_length

#__main__
s = "abcba"
k = 2
result = Solution.longest_substring_with_k_distinct_chars(s, k)
print("Length of the longest substring with at most 2 distinct characters:", result)  # Output: 3 ("bcb")