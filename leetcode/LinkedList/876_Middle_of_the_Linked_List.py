# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import copy
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _head = copy.deepcopy(head) # 깊은 복사를 한다
        node_list = [] # node의 갯수를 셀 리스트
        new_node : Optional[ListNode] # return 할 리스트

        # 노드의 갯수를 센다
        while _head:
            node_list.append(_head.val)
            _head = _head.next
        
        # 절반에 도달하면 new_node에 넣어주고 끝남
        a = 0
        while a <= len(node_list)//2 :
            if a < len(node_list)//2 :
                a += 1
                head = head.next
                continue
            a += 1
            new_node = head
            return new_node
 

# 투 포인터 기법을 활용함
# fast (두칸씩 이동)
# slow (한칸씩 이동)
# fast가 끝에 도달했을 때 slow는 절반만큼 이동
 class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        slow, fast = head, head
        
        while fast:
            
            fast = fast.next
            if fast: # 두칸씩 이동 로직
                fast = fast.next
            else:
                # fast has reached the end of linked list
                # slow is on the middle point now
                break
        
            slow = slow.next
        
        return slow