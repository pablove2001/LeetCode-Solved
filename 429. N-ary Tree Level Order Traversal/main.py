"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        res = []
        lvl = 0
        queue = [root]
        
        while queue:
            res.append([])
            newq = []
            for r in queue:
                res[lvl].append(r.val)
                newq += r.children
            queue = newq
            lvl += 1
        
        return res