package shy;

import java.util.ArrayList;

public class _234 {
	public boolean isPalindrome(ListNode head) {
		if (head == null)
			return true;
		ArrayList<Integer> arrayList = new ArrayList<Integer>();
		while (head != null) {
			arrayList.add(head.val);
			head = head.next;
		}
		int len = arrayList.size() / 2;
		for (int i = 0; i < len; i++) {
			if (arrayList.get(i).intValue() != arrayList.get(arrayList.size() - 1 - i).intValue())
				return false;
		}
		return true;
	}
}
