def reverseWords(s:str) -> str:
    separated = s.split()
    reversed = []

    for word in separated:
        reversed.append(word[::-1])

    return " ".join(reversed)

print(reverseWords("Let's take LeetCode contest"))

