# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         def linked_list_to_list(node):
#             digits = []
#             while node:
#                 digits.append(str(node.val))
#                 node = node.next
#             return digits

#         digits1 = linked_list_to_list(l1)
#         digits2 = linked_list_to_list(l2)

#         num1 = int("".join(reversed(digits1)))
#         num2 = int("".join(reversed(digits2)))
#         total = num1 + num2

#         dummy = ListNode(0)  # Use their ListNode class
#         current = dummy
#         for d in str(total)[::-1]:
#             current.next = ListNode(int(d))
#             current = current.next

#         return dummy.next 
