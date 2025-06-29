/*
 * LeetCode Problem: Partition String
 * Submission ID: sub_1751164601644
 * Runtime: N/A
 * Memory: N/A
 * Submitted: 2025-06-29T02:36:41.646Z
 * Difficulty: Medium
 * Category: Unknown
 */

class Solution:
    def partitionString(self, s: str) -> List[str]:
        left=0
        seg=[]
        for right in range(len(s)):
            curr_seg=set(s[left:right+1])
            if len(curr_seg)<(right-left+1):
                seg.append(s[left:right])
                left=right
        #remaining add
        seg.append(s[left:])
        return seg