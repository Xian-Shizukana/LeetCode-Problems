class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        arr = []
        
        for char in s:
            if char in ['(', '[', '{']:
                arr.append(char)
            elif char in [')', ']', '}']:
                if len(arr) == 0:
                    return False
                match arr.pop():
                    case '(':
                        if char == ')':
                            continue
                    case '[':
                        if char == ']':
                            continue
                    case '{':
                        if char == '}':
                            continue
                return False
            
        if len(arr) == 0:
            return True
        else:
            return False
        
       
    
# For Testing (not part of the solution)

leet = Solution()

s = "["

print(leet.isValid(s))




            
        