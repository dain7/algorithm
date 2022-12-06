# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # head가 존재하지 않으면 return
        if head is None :
            return None
            
        odd = head # 홀수
        even = head.next # 짝수
        evenHead = head.next # 짝수의 head를 담는 evenHead
 

        while even and even.next is not None:
            odd.next = odd.next.next #홀수의 다음은 홀수의 다다음 (1->2->3인 경우 1의 뒤에 3을 넣는다)
            even.next = even.next.next # 짝수의 다음은 짝수의 다다음 (1->2->3->4인 경우 2의 뒤에 4를 넣는다)

            # 다음을 처리하기 위해 재할당
            odd = odd.next 
            even = even.next 
        
        # 쭉 반복후 (1->3->5로 정리된 홀수의 다음에 2->4인 evenHead를 넣는다)
        odd.next = evenHead
        return head