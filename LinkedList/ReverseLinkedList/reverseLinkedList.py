import unittest

class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def reverseLinkedList(self, head: 'ListNode') -> 'ListNode':
        """
        Reverse a singly linked list.
        """
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def _build_linked_list(self, values):
        """Helper to build a linked list from a list of values"""
        if not values:
            return None
        head = self.solution.ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = self.solution.ListNode(val)
            current = current.next
        return head

    def _list_to_values(self, head):
        """Helper to convert linked list to list of values"""
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values

    def test_reverse_single_element(self):
        head = self._build_linked_list([1])
        result = self.solution.reverseLinkedList(head)
        self.assertEqual(self._list_to_values(result), [1])

    def test_reverse_two_elements(self):
        head = self._build_linked_list([1, 2])
        result = self.solution.reverseLinkedList(head)
        self.assertEqual(self._list_to_values(result), [2, 1])

    def test_reverse_multiple_elements(self):
        head = self._build_linked_list([1, 2, 3, 4, 5])
        result = self.solution.reverseLinkedList(head)
        self.assertEqual(self._list_to_values(result), [5, 4, 3, 2, 1])

    def test_reverse_empty_list(self):
        head = None
        result = self.solution.reverseLinkedList(head)
        self.assertIsNone(result)

    def test_reverse_negative_values(self):
        head = self._build_linked_list([-1, -2, -3])
        result = self.solution.reverseLinkedList(head)
        self.assertEqual(self._list_to_values(result), [-3, -2, -1])


if __name__ == '__main__':
    unittest.main()
    
    
