Python Solution

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #If the length of the two words are not the same
        if len(s)!=len(t):
            return False
        mp1,mp2={},{}
        for ch in s:
            mp1[ch] = 1+mp1.get(ch,0)
        for ch in t:
            mp2[ch] = 1+mp2.get(ch,0)
        return (mp1==mp2)


Java Solution

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length()!= t.length())
        {
            return false;
        }
        Map<Character,Integer> mp1 = new HashMap<Character,Integer>();
        for(int i=0;i<s.length();i++)
        {
            char ch = s.charAt(i);
            mp1.put(ch,mp1.getOrDefault(ch,0)+1);
        }
        Map<Character,Integer> mp2 = new HashMap<Character,Integer>();
        for(int i=0;i<t.length();i++)
        {
            char ch = t.charAt(i);
            mp2.put(ch,mp2.getOrDefault(ch,0)+1);
        }
        return mp1.equals(mp2);
    }
}