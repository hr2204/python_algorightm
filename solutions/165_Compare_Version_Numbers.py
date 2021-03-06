# 165. Compare Version Numbers
# Difficulty: Easy
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
#
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of
# the second first-level revision.
#
# Here is an example of version numbers ordering:
#
# 0.1 < 1.1 < 1.2 < 13.37


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        pre1 = version1.split(".")
        pre2 = version2.split(".")

        if len(pre1)>len(pre2):
            pre2 += [0] * (len(pre1) - len(pre2))
        if len(pre1)<len(pre2):
            pre1 += [0] * (len(pre2) - len(pre1))


        print pre1,pre2
        for i in range(min(len(pre1),len(pre2))):
            if int(pre1[i])>int(pre2[i]):
                return 1
            if int(pre1[i])<int(pre2[i]):
                return -1
        return 0


if __name__ == '__main__':
    print Solution().compareVersion("01","1")