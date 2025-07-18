def isPalindrome(s:str) -> bool:
    text = ''.join(char for char in s.lower() if char.isalnum())
    reversed_text = text[::-1]
    
    if text == reversed_text:
        return True
    return False

isPalindrome("man, a plan, a canal: Panama")
