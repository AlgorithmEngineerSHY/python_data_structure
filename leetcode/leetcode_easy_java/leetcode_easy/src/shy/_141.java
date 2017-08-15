package shy;

public class _141 {
	public boolean hasCycle(ListNode head) {
		if (head == null)
			return false;
		ListNode walker = head;
		ListNode runner = head;
		while (runner.next != null && runner.next.next != null) {
			runner = runner.next.next;
			walker = walker.next;
			if (walker == runner)
				return true;
		}
		return false;
	}
}
