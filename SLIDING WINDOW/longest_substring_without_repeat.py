# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

def longest_substring_without_repeat(s):
    seen = set()
    left = 0 
    right = 0 
    d = 0 
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left=+1
            
        seen.add(s[right])
        d = max(d, right - left + 1)
    return d