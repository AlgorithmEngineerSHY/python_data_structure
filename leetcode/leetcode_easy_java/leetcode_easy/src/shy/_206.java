package shy;

public class _206 {
	public ListNode reverseList(ListNode head) {
		if (head == null)
			return null;
		ListNode r = cuishuo(head);
		head.next = null;
		return r;
	}

	public ListNode cuishuo(ListNode head) {
		if (head == null)
			return null;
		if (head.next == null)
			return head;
		else {
			ListNode tmp = head.next;
			ListNode r = reverseList(head.next);
			tmp.next = head;
			return r;
		}
	}
}
