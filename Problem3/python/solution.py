
def lengthOfLongestSubstring(s: str) -> int:
    ans = 0
    sub = ''
    for char in s:
        if char not in sub:
            sub += char
            ans = max(ans, len(sub))
        else:
            print('character duplicated')
            print(f'sub before: {sub}')
            cut = sub.index(char)
            sub = sub[cut+1:] + char
            print(f'sub after: {sub}')
    return ans
    

print('length of longest substring for anviaj')
print(lengthOfLongestSubstring('anviaj'))