package shy;

public class _38 {
	public String countAndSay(int n) {
		StringBuilder curr = new StringBuilder("1");
		StringBuilder pre = new StringBuilder();
		int count;
		char say;
		for (int i = 1; i < n; i++) {
			pre = curr;
			curr = new StringBuilder();
			count = 1;
			say = pre.charAt(0);
			for (int j = 1, len = pre.length(); j < len; j++) {
				if (say != pre.charAt(j)) {
					curr.append(count).append(say);
					say = pre.charAt(j);
					count = 1;
				} else
					count++;
			}
			curr.append(count).append(say);
		}
		return curr.toString();
	}
}
