package com.ehborisov.algorithms.playground;

import java.util.Iterator;
import java.util.LinkedHashSet;

/**
 * https://leetcode.com/problems/longest-substring-without-repeating-characters
 */


public class LengthOfLongestSubstringWithoutRepeatingCharacters {

    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) {
            return 0;
        }
        LinkedHashSet<Character> substringHolder = new LinkedHashSet<>();
        int maxLen = 0;
        for (char ch : s.toCharArray()) {
            if (substringHolder.contains(ch)) {
                if (substringHolder.size() > maxLen) {
                    maxLen = substringHolder.size();
                }
                Iterator<Character> iter = substringHolder.iterator();
                while (iter.hasNext()) {
                    Character cur = iter.next();
                    iter.remove();
                    if (cur == ch) {
                        break;
                    }
                }
            }
            substringHolder.add(ch);
        }
        if (substringHolder.size() > maxLen) {
            maxLen = substringHolder.size();
        }
        return maxLen;
    }
}
