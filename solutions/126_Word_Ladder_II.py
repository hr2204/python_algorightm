# 126. Word Ladder II
# Difficulty: Hard
# Contributors: Admin
# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s)
# from beginWord to endWord, such that:
#
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# For example,
#
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
# Note:
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# UPDATE (2017/1/20):
# The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code
# definition to get the latest changes.

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        res = [[beginWord]]
        cur_word = beginWord
        no_exit_flag = True
        while no_exit_flag:
            no_exit_flag = False
            for cur_list in res:
                cur_word = cur_list[-1]
                for i in xrange(len(cur_word)):
                    part1 = cur_word[:i]
                    part2 = cur_word[i+1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = part1 + j + part2
                        if next_word in wordList:
                            cur_list.append(next_word)
                            wordList.remove(next_word)
                            no_exit_flag = True
        print res



if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print Solution().findLadders(beginWord, endWord, wordList)