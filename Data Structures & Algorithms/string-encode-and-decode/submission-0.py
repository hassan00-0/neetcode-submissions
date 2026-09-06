class Solution:
    # ["Oo", "hi", "3#hi"] => 2#Oo2#hi4#3#hi
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string))
            encoded += "#"
            encoded += string
        return encoded
    def decode(self, s: str) -> List[str]:
        number = ""
        arr = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                number += s[i]
                i += 1
            elif s[i] == "#":
                arr.append(s[i+1: i+1+int(number)])
                i+= int(number) + 1
                number = ""
        return arr
