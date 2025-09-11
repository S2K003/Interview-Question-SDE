Python Solution

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""
        
        prefix = strs[0]#flower
        for word in strs[1:]:#flow
            while not word.startswith(prefix):#flow starts with (flow)
                prefix = prefix[:-1]    
                if not prefix:
                    return ""
        
        return prefix
                

Java Solution

class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length==0)
        {
            return "";
        }

        String prefix = strs[0];

        for(String word:strs)
        {
            while(!word.startsWith(prefix))
            {
                prefix = prefix.substring(0,prefix.length()-1);
            }
            if(prefix.length()==0)
            {
                return "";
            }
        }

        return prefix;

    }
}