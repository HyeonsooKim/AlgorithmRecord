# 내 풀이(풀었음)
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         ls = [0] * (ord('z')+1)
#         if ransomNote in magazine:
#             return True
#         else:
#             for i in magazine:
#                 ls[ord(i)] += 1
#             for i in ransomNote:
#                 ls[ord(i)] -= 1
#             for i in range(ord('a'), ord('z')+1):
#                 if ls[i] < 0:
#                     return False
#             else:
#                 return True

from itertools import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = Counter(magazine)
        ransomNote = Counter(ransomNote)
        return all(magazine[c] >= ransomNote[c] for c in ransomNote)
