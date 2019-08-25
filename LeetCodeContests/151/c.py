# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def to_list(h):
    ans = []
    while h:
        ans.append(h.val)
        h = h.next
    return ans


def to_link(l):
    n = ListNode(None)
    h = n
    for node in l:
        n.next = ListNode(node)
        n = n.next
    return h.next


class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l = to_list(head)
        ans = list()
        for n in l:
            ans.append(n)
            s = 0
            for k in reversed(xrange(len(ans))):
                s += ans[k]
                if s == 0:
                    ans = ans[:k]
                    break
        return to_link(ans)


/**
* Definition for singly-linked list.
* struct ListNode {
*     int val;
*     ListNode *next;
*     ListNode(int x) : val(x), next(NULL) {}
* };
*/
class Solution {
public:
    ListNode* removeZeroSumSublists(ListNode* head) {
        ListNode* fst = new ListNode(0);
        fst->next = head;
        bool update = 1;
        while(update) {
            update = 0;
            for(auto p = fst; p != NULL; p = p->next) {
                int tot = 0;
                for(auto q = p->next; q != NULL; q = q->next) {
                    tot += q->val;
                    if(!tot) {
                        update = 1;
                        p->next = q->next;
                        break;
                    }
                }
                if(update)break;
            }
        }
        return fst->next;
    }
};