class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([x for x in s if x.isalpha() or x.isnumeric()])
        return s.lower() == s[::-1].lower()



            


            
            
        