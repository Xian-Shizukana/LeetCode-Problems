def isAnagram(s: str, t: str) -> bool:
    if ''.join(sorted(s)) == ''.join(sorted(t)):
        return True
    return False

print(isAnagram('anagram', 'nagaram'))
