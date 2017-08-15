package shy;

public class _160 {
	public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
		if (headA == null || headB == null)
			return null;
		ListNode a = headA;
		ListNode b = headB;
		while (a != null || b != null) {
			if (a == b)
				return a;
			if (a == null)
				a = headB;
			else
				a = a.next;
			if (b == null)
				b = headA;
			else
				b = b.next;
		}
		return null;
	}
}
