# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverseList( head):
            if head and head.next:
                nxt  = head.next
                head.next = None
                rev = reverseList(nxt)
                nxt.next = head
                return rev
            return head
        
        def middleNode(head: ListNode) -> ListNode:
            if head:
                s = head
                f = head
                while f.next and f.next.next:
                    s = s.next
                    f=  f.next.next
                if f.next:
                    return s.next
                return s
            return head
        
        if head and head.next and head.next.next:
        
            mid = middleNode(head)
            l2 = mid.next
            mid.next = None
            l1 = head

            l2 = reverseList(l2)

            nh = ListNode('head')
            tail = nh

            while l1 and l2:
                tail.next = l1
                l1 = l1.next
                tail = tail.next

                tail.next = l2
                l2 = l2.next
                tail = tail.next
            tail.next = l1
            l1 = l1.next
            tail = tail.next
        return head
        
#Explanation
# Input
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> None 

# Find middle and divide
# l1 = 1 -> 2 -> 3 -> 4 -> None
# l2 = 5 -> 6 -> 7 -> 8 -> None 

# Reverse l2
# l1 = 1 -> 2 -> 3 -> 4 -> None
# l2 = 8 -> 7 -> 6 -> 5 -> None 


# nh = ()
# pass1
# l1 = 1    2 -> 3 -> 4 -> None
#      |   ^
#      |  /
#      v/
# l2 = 8    7 -> 6 -> 5 -> None 


# pass2
# l1 = 1    2    3 -> 4 -> None
#      |   ^|   ^
#      |  / |  /
#      v/   v/
# l2 = 8    7    6 -> 5 -> None 

# last pass
# l1 = 1    2    3    4    None
#      |   ^|   ^|   ^|   ^
#      |  / |  / |  / |  /
#      v/   v/   v/   v/
# l2 = 8    7    6    5    None 

# Answer is 

# 1 -> 8 -> 2 -> 7 -> 3 -> 6 -> 4 -> 5 -> None 