'''
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''
# Attempt 1
def longestPalindrome(s: str) -> str:
    pal_tracker = ''
    pals = []
    pals.append(s[0])
    for char in s:
        if char not in pal_tracker:
            pal_tracker += char
        else:
            char_index = [i for i, x in enumerate(pal_tracker) if x == char]
            for index in char_index:
                candidate = pal_tracker[index:] + char
                if candidate == candidate[::-1]:
                    pals.append(candidate)
            pal_tracker += char

    return max(pals, key=len)

#Attempt 2
def longestPalindrome(s: str) -> str:
    longest_pal = s[0]
    for start_index in range(len(s)):
        print(f'First Value = {s[start_index:]}')
        print(f'Second Value = {s[start_index:][::-1]}')
        # if s[start_index:] == s[start_index::-1]:
        #     longest_pal = max(s[start_index:], longest_pal)