package shy;

public class _67 {
	public String addBinary(String a, String b) {
		StringBuilder sb = new StringBuilder();
		int m = a.length() - 1, n = b.length() - 1, tmp = 0;
		while (m >= 0 || n >= 0) {
			int sum = tmp;
			if (m >= 0)
				sum += a.charAt(m--) - '0';
			if (n >= 0)
				sum += b.charAt(n--) - '0';
			sb.append(sum % 2);
			tmp = sum / 2;
		}
		if (tmp != 0)
			sb.append('1');
		return sb.reverse().toString();
	}
}
