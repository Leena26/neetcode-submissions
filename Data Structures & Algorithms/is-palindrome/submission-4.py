class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s)
        new = "".join([x for x in s if x.isalpha() or x.isnumeric()]).lower()
        length = len(new)
        print(new," len: ", length)
        if length%2 == 0:
            bottom = new[0:(length//2)]
            top = new[length//2:length]
        else:
            bottom = new[0:(length//2)]
            top = new[1 + length//2 :length]
        bottom = bottom[::-1]
        return bottom == top



            


            
            
        