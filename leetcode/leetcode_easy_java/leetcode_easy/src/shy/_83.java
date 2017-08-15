package shy;

public class _83 {
	public ListNode deleteDuplicates(ListNode head) {
		if (head == null || head.next == null)
			return head;
		head.next = deleteDuplicates(head.next);
		return head.next.val == head.val ? head.next : head;
	}
}
