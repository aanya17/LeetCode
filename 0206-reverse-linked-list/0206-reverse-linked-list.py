class Solution:
    def reverseList(self, head):
        curr = head
        rev = None
        while curr:
            new_node = curr.next
            curr.next = rev
            rev = curr
            curr = new_node
        return rev
