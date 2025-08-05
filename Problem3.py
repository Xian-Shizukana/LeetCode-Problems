def lenghtofLongestSubstring(s:str) -> int:
    longest = 0
    left = 0
    curr_substring = set()
    s_len = len(s)

    for right in range(s_len):
        while (s[right] in curr_substring):
            curr_substring.remove(s[left])
            left += 1

        curr_substring.add(s[right])
        longest = max(longest, (right - left + 1))

    return longest

print(lenghtofLongestSubstring("abcabcbb"))
