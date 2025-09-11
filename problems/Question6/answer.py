Python Solution

from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            anagrams[key].append(word)

        return list(anagrams.values())
        

Python Solution - Frequency Map Solution

from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)

        for word in strs:
            #Frequency Map
            f_map = [0] * 26
            for ch in word:
                f_map[ord(ch)-ord('a')] += 1

            key = tuple(f_map)
            anagrams[key].append(word)

        return list(anagrams.values())



        
        