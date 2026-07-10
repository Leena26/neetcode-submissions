class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([x for x in s.lower() if x.isalpha()])
        print(s, s[::-1])
        return s == s[::-1]



            


            
            
        