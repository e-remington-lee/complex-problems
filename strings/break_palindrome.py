class SolutionGood:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        replacement_index = 0
        replacement_char = None
        middle = len(palindrome) // 2
        for i, s in enumerate(palindrome[:middle]):
            if s != "a":
                replacement_index = i
                replacement_char = "a"
                break
        
        if not replacement_char:
            replacement_index = len(palindrome) - 1
            replacement_char = "b"
        
        li = list(palindrome)
        li[replacement_index] = replacement_char
        return "".join(li)

class SolutionCustom:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        even = None
        replacement_index = 0
        replacement_char = None
        if len(palindrome) % 2 == 0:
            even = True
        else:
            even = False
            middle = len(palindrome) // 2
            
        if even:
            for i, s in enumerate(palindrome, start=0):
                if s != "a":
                    replacement_index = i
                    replacement_char = "a"
                    break
                if i == len(palindrome) - 1:
                    replacement_index = i
                    replacement_char = "b"
                    break
        else:
            for i, s in enumerate(palindrome, start=0):
                if s != "a":
                    if i != middle:
                        replacement_index = i
                        replacement_char = "a"
                        break
                    else:
                        replacement_index = len(palindrome) - 1
                        replacement_char = "b"
                        break
                if i == len(palindrome) - 1:
                    replacement_index = i
                    replacement_char = "b"
                    break
                    
        li = list(palindrome)
        li[replacement_index] = replacement_char
        return "".join(li)

from utilities import to_string
flashcard=to_string.file_to_string(__file__)
print(flashcard)