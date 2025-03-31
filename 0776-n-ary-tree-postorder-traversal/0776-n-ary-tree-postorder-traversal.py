"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        if not root:
            return []

        stack = [(root,False)]

        while stack:
            node, vis = stack.pop()

            if vis:
                res.append(node.val)

            else:
                stack.append((node, True))

                for c in node.children[::-1]:
                    stack.append((c, False))

        return res
